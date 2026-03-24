# 🔥 GitHub Roaster

> An AI-powered tool that analyzes any GitHub profile and generates a savage, witty roast based on real stats.

---

## Overview

GitHub Roaster fetches real data from any public GitHub profile and uses a locally running LLM to generate a humorous, fact-based roast. No paid APIs. No data leaves your machine.

---

## Features

- **Real Data** — Pulls live stats from the GitHub API
- **AI-Generated Roasts** — Powered by LLaMA 3 running locally via Ollama
- **Adjustable Intensity** — From Gentle to Brutal
- **Developer Comparison** — Roast two developers head-to-head with a winner declaration
- **Privacy First** — Fully local inference, no external AI API calls

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | LLaMA 3 8B via Ollama |
| Data Source | GitHub REST API |
| Language | Python 3.10+ |

---

## Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- GitHub Personal Access Token (optional but recommended)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/github-roaster
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
```

**4. Pull the LLaMA 3 model**
```bash
ollama pull llama3
```

**5. Run the application**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## Project Structure
```
github-roaster/
├── app.py          # Streamlit UI
├── backend.py      # GitHub API + Ollama integration
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
ollama
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