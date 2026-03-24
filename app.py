import streamlit as st
from backend import fetch_github_data, process_data, generate_roast
import time

# Page configuration
st.set_page_config(page_title="GitHub Roaster", page_icon="🔥", layout="centered")

# GitHub-like CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    * { font-family: 'Inter', sans-serif !important; }

    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }

    .gh-header {
        text-align: center;
        padding: 40px 0 10px 0;
    }

    .gh-title {
        font-size: 2em;
        font-weight: 700;
        color: #e6edf3;
        letter-spacing: -0.5px;
    }

    .gh-subtitle {
        color: #8b949e;
        font-size: 0.95em;
        margin-top: 6px;
    }

    .gh-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 20px;
        margin: 12px 0;
    }

    .gh-card-title {
        color: #8b949e;
        font-size: 0.78em;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 14px;
        border-bottom: 1px solid #21262d;
        padding-bottom: 8px;
    }

    .gh-profile {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .gh-name {
        font-size: 1.2em;
        font-weight: 700;
        color: #e6edf3;
    }

    .gh-username {
        color: #8b949e;
        font-size: 0.9em;
        margin-top: 2px;
    }

    .gh-bio {
        color: #c9d1d9;
        font-size: 0.88em;
        margin-top: 6px;
    }

    .gh-stat-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #21262d;
        font-size: 0.9em;
        color: #8b949e;
    }

    .gh-stat-row:last-child { border-bottom: none; }

    .gh-stat-value {
        color: #e6edf3;
        font-weight: 600;
    }

    .gh-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 3px;
        font-size: 0.78em;
        font-weight: 600;
        background: #21262d;
        color: #58a6ff;
        border: 1px solid #30363d;
    }

    .gh-repo {
        padding: 10px 0;
        border-bottom: 1px solid #21262d;
        font-size: 0.88em;
        color: #8b949e;
    }

    .gh-repo:last-child { border-bottom: none; }

    .gh-repo-name {
        color: #58a6ff;
        font-weight: 600;
    }

    .gh-roast {
        background: #161b22;
        border: 1px solid #f78166;
        border-radius: 6px;
        padding: 24px;
        margin: 16px 0;
        color: #e6edf3;
        font-size: 0.95em;
        line-height: 1.9;
    }

    .gh-roast-title {
        font-size: 1em;
        font-weight: 700;
        color: #f78166;
        margin-bottom: 14px;
        padding-bottom: 10px;
        border-bottom: 1px solid #30363d;
    }

    .stButton > button {
        background: #21262d !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        padding: 8px 20px !important;
        font-size: 0.9em !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.2s;
    }

    .stButton > button:hover {
        background: #30363d !important;
        border-color: #8b949e !important;
    }

    .stTextInput > div > div > input {
        background: #0d1117 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        padding: 8px 14px !important;
        font-size: 0.9em !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 3px #1f6feb33 !important;
    }

    hr { border-color: #21262d !important; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="gh-header">
    <div class="gh-title">🔥 GitHub Roaster</div>
    <div class="gh-subtitle">Enter any GitHub username — we'll let the AI do the talking</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Controls
intensity = st.select_slider(
    "Roast Intensity",
    options=["😇 Gentle", "😏 Mild", "😈 Savage", "💀 Brutal"],
    value="😈 Savage"
)

mode = st.radio("Mode", ["🔥 Single Roast", "⚔️ Compare Developers"], horizontal=True)

st.divider()

# ─── SINGLE ROAST MODE ───────────────────────────────────────────
if mode == "🔥 Single Roast":
    col1, col2 = st.columns([3, 1])
    with col1:
        username = st.text_input("", placeholder="Search GitHub username...", key="single_user")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        roast_btn = st.button("🔥 Roast", use_container_width=True)

    if roast_btn:
        if username.strip() == "":
            st.warning("Please enter a username.")
        else:
            with st.spinner("Fetching profile..."):
                time.sleep(0.3)
                user, repos = fetch_github_data(username.strip())

            if "message" in user:
                st.error("User not found. Check the username.")
            else:
                data = process_data(user, repos)
                avatar_url = user.get("avatar_url", "")
                bio = user.get("bio") or "No bio provided."

                # Profile card
                st.markdown(f"""
                <div class="gh-card">
                    <div class="gh-card-title">Profile</div>
                    <div class="gh-profile">
                        <img src="{avatar_url}" width="72"
                             style="border-radius:50%; border: 1px solid #30363d;">
                        <div>
                            <div class="gh-name">{data['name']}</div>
                            <div class="gh-username">@{username}</div>
                            <div class="gh-bio">{bio}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Stats card
                st.markdown(f"""
                <div class="gh-card">
                    <div class="gh-card-title">Stats</div>
                    <div class="gh-stat-row"><span>Repositories</span><span class="gh-stat-value">{data['total_repos']}</span></div>
                    <div class="gh-stat-row"><span>Empty repositories</span><span class="gh-stat-value">{data['empty_repos']}</span></div>
                    <div class="gh-stat-row"><span>Total stars earned</span><span class="gh-stat-value">{data['total_stars']}</span></div>
                    <div class="gh-stat-row"><span>Followers</span><span class="gh-stat-value">{data['followers']}</span></div>
                    <div class="gh-stat-row"><span>Following</span><span class="gh-stat-value">{data['following']}</span></div>
                </div>
                """, unsafe_allow_html=True)

                # Languages
                if data['languages']:
                    badges = "".join([f'<span class="gh-badge">{lang}</span>' for lang in data['languages']])
                    st.markdown(f"""
                    <div class="gh-card">
                        <div class="gh-card-title">Languages</div>
                        {badges}
                    </div>
                    """, unsafe_allow_html=True)

                # Top repos
                if repos:
                    repo_items = "".join([
                        f'''<div class="gh-repo">
                            <span class="gh-repo-name">{r["name"]}</span>
                            &nbsp;·&nbsp; ⭐ {r["stargazers_count"]}
                            &nbsp;·&nbsp; {r.get("language") or "Unknown"}
                        </div>'''
                        for r in sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)[:5]
                    ])
                    st.markdown(f"""
                    <div class="gh-card">
                        <div class="gh-card-title">Top Repositories</div>
                        {repo_items}
                    </div>
                    """, unsafe_allow_html=True)

                # Generate roast
                with st.spinner("Generating roast..."):
                    roast = generate_roast(data, intensity)

                # Roast output
                st.markdown(f"""
                <div class="gh-roast">
                    <div class="gh-roast-title">🔥 Roast — @{username}</div>
                    {roast.replace(chr(10), '<br>')}
                </div>
                <p style="color:#484f58; font-size:0.78em; text-align:center; margin-top:8px;">
                    All in good fun · No developers were harmed
                </p>
                """, unsafe_allow_html=True)


# COMPARE MODE 
elif mode == "⚔️ Compare Developers":
    col1, col2 = st.columns(2)
    with col1:
        username1 = st.text_input("", placeholder="First developer...", key="u1")
    with col2:
        username2 = st.text_input("", placeholder="Second developer...", key="u2")

    compare_btn = st.button("⚔️ Compare & Roast Both", use_container_width=True)

    if compare_btn:
        if not username1.strip() or not username2.strip():
            st.warning("Enter both usernames!")
        else:
            with st.spinner("Fetching both profiles..."):
                user1, repos1 = fetch_github_data(username1.strip())
                user2, repos2 = fetch_github_data(username2.strip())

            if "message" in user1:
                st.error(f"User @{username1} not found!")
            elif "message" in user2:
                st.error(f"User @{username2} not found!")
            else:
                data1 = process_data(user1, repos1)
                data2 = process_data(user2, repos2)

                # Side by side profiles
                col1, col2 = st.columns(2)
                for col, data, uname, user in [
                    (col1, data1, username1, user1),
                    (col2, data2, username2, user2)
                ]:
                    with col:
                        avatar = user.get("avatar_url", "")
                        st.markdown(f"""
                        <div class="gh-card">
                            <div style="text-align:center;">
                                <img src="{avatar}" width="60"
                                     style="border-radius:50%; border:1px solid #30363d;">
                                <div style="color:#e6edf3; font-weight:700; margin-top:8px;">{data['name']}</div>
                                <div style="color:#8b949e; font-size:0.85em;">@{uname}</div>
                            </div>
                            <div style="margin-top:14px;">
                                <div class="gh-stat-row"><span>Repos</span><span class="gh-stat-value">{data['total_repos']}</span></div>
                                <div class="gh-stat-row"><span>Empty</span><span class="gh-stat-value">{data['empty_repos']}</span></div>
                                <div class="gh-stat-row"><span>Stars</span><span class="gh-stat-value">{data['total_stars']}</span></div>
                                <div class="gh-stat-row"><span>Followers</span><span class="gh-stat-value">{data['followers']}</span></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                # Winner
                score1 = data1['total_stars'] * 2 + data1['followers'] + data1['total_repos'] - data1['empty_repos']
                score2 = data2['total_stars'] * 2 + data2['followers'] + data2['total_repos'] - data2['empty_repos']
                winner = data1['name'] if score1 > score2 else data2['name']
                winner_handle = username1 if score1 > score2 else username2

                st.markdown(f"""
                <div class="gh-card" style="text-align:center; border-color:#f78166; margin-top:8px;">
                    <div style="color:#f78166; font-size:0.78em; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Winner</div>
                    <div style="color:#e6edf3; font-size:1.3em; font-weight:700;">🏆 {winner}</div>
                    <div style="color:#8b949e; font-size:0.85em; margin-top:4px;">@{winner_handle} wins with score {max(score1, score2)}</div>
                </div>
                """, unsafe_allow_html=True)

                # Roast both
                with st.spinner("Roasting both developers... 💀"):
                    roast1 = generate_roast(data1, intensity)
                    roast2 = generate_roast(data2, intensity)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div class="gh-roast">
                        <div class="gh-roast-title">🔥 @{username1}</div>
                        {roast1.replace(chr(10), '<br>')}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div class="gh-roast">
                        <div class="gh-roast-title">🔥 @{username2}</div>
                        {roast2.replace(chr(10), '<br>')}
                    </div>
                    """, unsafe_allow_html=True)