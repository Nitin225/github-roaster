# 🔥 GitHub Roaster

> An AI-powered tool that analyzes any GitHub profile and generates a savage, witty roast based on real stats.

---

## Overview

GitHub Roaster fetches real data from any public GitHub profile and uses LLaMA 3 70B via Groq API to generate a humorous, fact-based roast. Fast, free, and no local setup required.

---

## Features

- **Real Data** — Pulls live stats from the GitHub API
- **AI-Generated Roasts** — Powered by LLaMA 3 70B via Groq API
- **Adjustable Intensity** — From Gentle to Brutal
- **Developer Comparison** — Roast two developers head-to-head with a winner declaration

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | LLaMA 3 70B via Groq API |
| Data Source | GitHub REST API |
| Language | Python 3.10+ |

---

## Getting Started

### Prerequisites
- Python 3.10+
- GitHub Personal Access Token (optional but recommended)
- Groq API Key — free at [console.groq.com](https://console.groq.com)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Nitin225/github-roaster
cd github-roaster
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the root directory:
```
GITHUB_TOKEN=your_github_personal_access_token
GROQ_API_KEY=your_groq_api_key
```

**4. Run the application**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## Project Structure
```
github-roaster/
├── app.py          # Streamlit UI
├── backend.py      # GitHub API + Groq integration
├── .env            # Environment variables (not committed)
├── .gitignore      # Ignores .env and cache files
├── requirements.txt
└── README.md
```

---

## Usage

1. Select roast intensity using the slider
2. Choose **Single Roast** or **Compare Developers** mode
3. Enter a GitHub username and click **Roast**
4. Watch the AI tear them apart — respectfully 😄

---

## Requirements
```
streamlit
requests
groq
python-dotenv
rich
```

---

## Disclaimer

All roasts are AI-generated and intended purely for entertainment.
No developers were harmed in the making of this project.

---

## License

MIT License — feel free to use, modify, and share.