import os
import requests
from rich.console import Console
from rich.panel import Panel
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

console = Console()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_github_data(username):
    # Add auth header if token is available
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    try:
        # Fetch user profile and repositories with timeout
        user = requests.get(f"https://api.github.com/users/{username}", headers=headers, timeout=10).json()
        repos = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers, timeout=10).json()
        return user, repos
    except requests.exceptions.Timeout:
        return {"message": "Connection timed out. Try again."}, []
    except requests.exceptions.ConnectionError:
        return {"message": "Cannot connect. Check internet."}, []
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, []

def process_data(user, repos):
    # Calculate repo statistics
    total_repos = len(repos)
    empty_repos = sum(1 for r in repos if r["size"] == 0)
    languages = list(set(r["language"] for r in repos if r["language"]))
    total_stars = sum(r["stargazers_count"] for r in repos)
    
    # Find funny or suspicious repo names
    funny_names = [r["name"] for r in repos if any(x in r["name"].lower() for x in ["test", "demo", "final", "asdf", "temp"])]
    
    # Count repos without description
    no_description = sum(1 for r in repos if not r["description"])

    return {
        "name": user.get("name") or user.get("login"),
        "bio": user.get("bio") or "No bio found",
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "total_repos": total_repos,
        "empty_repos": empty_repos,
        "languages": languages,
        "total_stars": total_stars,
        "funny_names": funny_names,
        "no_description": no_description,
    }

def generate_roast(data, intensity = "😈 Savage"):
    
    intensity_map = {
        "😇 Gentle": "Be kind and funny, very light roast, mostly compliments with tiny jokes.",
        "😏 Mild": "Moderate roast, friendly jokes, nothing too harsh.",
        "😈 Savage": "Savage and witty roast, brutal honesty, very funny.",
        "💀 Brutal": "Absolutely destroy them. No mercy. Maximum savage. Still funny though."
    }

    tone = intensity_map.get(intensity, intensity_map["😈 Savage"])
    
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

    Write a funny, savage and witty roast in ENGLISH — 6-8 lines.
    Make it specific to their actual stats. End with a backhanded compliment.
    Keep it fun, not mean.
    """

    response = ollama.chat(
        model="llama3:latest",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

def main():
    console.print(Panel("🔥 GitHub Roaster 🔥", style="bold red"))
    username = input("\nEnter GitHub username: ").strip()

    console.print("\n[yellow]Analyzing profile...[/yellow]")

    # Fetch and process data
    user, repos = fetch_github_data(username)

    if "message" in user:
        console.print("[red]User not found! Check the username.[/red]")
        return

    data = process_data(user, repos)
    roast = generate_roast(data)

    # Display roast in styled panel
    console.print(Panel(roast, title=f"🎤 {data['name']}'s Roast", style="bold green"))

if __name__ == "__main__":
    main()