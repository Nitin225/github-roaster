import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class RoastRequest(BaseModel):
    username: str
    intensity: str = "Savage"


class CompareRequest(BaseModel):
    username1: str
    username2: str
    intensity: str = "Savage"


def fetch_github_data(username):
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    try:
        user = requests.get(f"https://api.github.com/users/{username}", headers=headers, timeout=10).json()
        repos = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers, timeout=10).json()
        return user, repos
    except requests.exceptions.Timeout:
        return {"message": "Connection timed out."}, []
    except requests.exceptions.ConnectionError:
        return {"message": "Cannot connect. Check internet."}, []
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, []


def process_data(user, repos):
    if not isinstance(repos, list):
        repos = []
    total_repos = len(repos)
    empty_repos = sum(1 for r in repos if r.get("size") == 0)
    languages = list(set(r["language"] for r in repos if r.get("language")))
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    funny_names = [r["name"] for r in repos if any(x in r["name"].lower() for x in ["test", "demo", "final", "asdf", "temp"])]
    no_description = sum(1 for r in repos if not r.get("description"))
    top_repos = sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)[:5]

    return {
        "name": user.get("name") or user.get("login"),
        "login": user.get("login"),
        "bio": user.get("bio") or "No bio found",
        "avatar_url": user.get("avatar_url", ""),
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "total_repos": total_repos,
        "empty_repos": empty_repos,
        "languages": languages,
        "total_stars": total_stars,
        "funny_names": funny_names,
        "no_description": no_description,
        "top_repos": [{"name": r["name"], "stars": r.get("stargazers_count", 0), "language": r.get("language") or "Unknown"} for r in top_repos],
    }


def generate_roast(data, intensity="Savage"):
    intensity_map = {
        "Gentle": "Be kind and funny, very light roast, mostly compliments with tiny jokes.",
        "Mild": "Moderate roast, friendly jokes, nothing too harsh.",
        "Savage": "Savage and witty roast, brutal honesty, very funny.",
        "Brutal": "Absolutely destroy them. No mercy. Maximum savage. Still funny though."
    }
    tone = intensity_map.get(intensity, intensity_map["Savage"])

    prompt = f"""
    Here is a GitHub developer's data:
    - Name: {data['name']}
    - Bio: {data['bio']}
    - Followers: {data['followers']}, Following: {data['following']}
    - Total Repos: {data['total_repos']}, Empty Repos: {data['empty_repos']}
    - Languages: {', '.join(data['languages']) if data['languages'] else 'None'}
    - Total Stars: {data['total_stars']}
    - Funny Repo Names: {', '.join(data['funny_names']) if data['funny_names'] else 'None'}
    - Repos without description: {data['no_description']}

    Tone: {tone}

    Write a funny, savage and witty roast in ENGLISH — 6-8 lines.
    Make it specific to their actual stats. End with a backhanded compliment.
    Keep it fun, not mean. No markdown, plain text only.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


@app.get("/")
def root():
    return {"status": "GitHub Roaster API running"}


@app.post("/roast")
def roast(req: RoastRequest):
    user, repos = fetch_github_data(req.username)
    if "message" in user:
        return {"error": user["message"]}
    data = process_data(user, repos)
    roast_text = generate_roast(data, req.intensity)
    return {"data": data, "roast": roast_text}


@app.post("/compare")
def compare(req: CompareRequest):
    user1, repos1 = fetch_github_data(req.username1)
    user2, repos2 = fetch_github_data(req.username2)

    if "message" in user1:
        return {"error": f"@{req.username1}: {user1['message']}"}
    if "message" in user2:
        return {"error": f"@{req.username2}: {user2['message']}"}

    data1 = process_data(user1, repos1)
    data2 = process_data(user2, repos2)

    roast1 = generate_roast(data1, req.intensity)
    roast2 = generate_roast(data2, req.intensity)

    score1 = data1['total_stars'] * 2 + data1['followers'] + data1['total_repos'] - data1['empty_repos']
    score2 = data2['total_stars'] * 2 + data2['followers'] + data2['total_repos'] - data2['empty_repos']
    winner = req.username1 if score1 >= score2 else req.username2

    return {
        "data1": data1, "roast1": roast1,
        "data2": data2, "roast2": roast2,
        "winner": winner,
        "score1": score1, "score2": score2,
    }