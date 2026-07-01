# GitHub Roaster 🔥

An AI-powered full-stack application that analyzes GitHub profiles and generates witty, data-driven roasts using real-time statistics.

---

## Overview

GitHub Roaster combines GitHub’s public API with large language models to create humorous, context-aware roasts of developer profiles.
The project includes both a modern web interface and a lightweight prototype version.

---

## Features

* Real-time GitHub data analysis (repositories, stars, followers)
* AI-generated roasts using LLaMA 3 (via Groq API)
* Adjustable roast intensity (Gentle to Brutal)
* Developer comparison with scoring and winner selection
* Dual interface: React web app and Streamlit prototype

---

## Tech Stack

| Layer        | Technology         |
| ------------ | ------------------ |
| Frontend     | React.js           |
| Backend      | FastAPI            |
| Prototype UI | Streamlit          |
| AI Model     | LLaMA 3 (Groq API) |
| Data Source  | GitHub REST API    |
| Languages    | Python, JavaScript |

---

## Project Structure

```bash
github-roaster/
├── backend/             # FastAPI backend
├── frontend/            # React application
├── streamlit-version/   # Streamlit prototype
├── requirements.txt
├── package.json
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/github-roaster
cd github-roaster
```

---

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on: `http://localhost:8000`

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on: `http://localhost:3000`

---

### 4. Streamlit (Optional)

```bash
cd streamlit-version
pip install -r requirements.txt
streamlit run app.py
```

---

## Environment Variables

Create a `.env` file in the root or backend directory:

```
GROQ_API_KEY=your_api_key
GITHUB_TOKEN=your_github_token
```

---

## API Endpoints

* `POST /roast` — Generate roast for a single user
* `POST /compare` — Compare and roast two users
* `GET /docs` — Interactive API documentation

---

## Usage

1. Open the React app in the browser
2. Enter a GitHub username
3. Select roast intensity
4. Generate a roast or compare developers

---

## Disclaimer

This project is intended for entertainment purposes only.
All outputs are AI-generated and not meant to offend.

---

## License

MIT License
