# GitHub Roaster

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Live Demo:** https://git-roast.streamlit.app/

GitHub Roaster is an AI-powered application that analyzes a GitHub profile and generates a humorous roast using GitHub profile data and LLaMA 3.

---

## Features

- Analyze any public GitHub profile
- Generate AI-powered roasts using LLaMA 3 (Groq)
- Fetch profile information using the GitHub REST API
- Streamlit-based user interface
- FastAPI backend

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Model | LLaMA 3 (Groq API) |
| API | GitHub REST API |
| Language | Python |

---

## Project Structure

```text
github-roaster/
├── backend/
├── streamlit-version/
├── frontend/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/Nitin225/github-roaster.git

cd github-roaster
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
cd streamlit-version
streamlit run app.py
```

Run the FastAPI backend

```bash
cd backend
uvicorn main:app --reload
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

---

## Live Demo

https://git-roast.streamlit.app/

---

## Disclaimer

This project is intended for entertainment purposes only. The generated roasts are AI-generated.

---

## License

MIT License
