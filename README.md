# GitHub Roaster 🔥

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

🚀 **Live Demo:** https://git-roast.streamlit.app/

An AI-powered application that analyzes GitHub profiles and generates witty, context-aware roasts using real-time GitHub statistics and LLaMA 3.

---

## ✨ Features

- 🤖 AI-powered GitHub profile roasting using **LLaMA 3 (Groq API)**
- 📊 Real-time GitHub profile analysis
- ⭐ Repository, Stars & Followers insights
- 🔥 Adjustable roast intensity (Gentle → Brutal)
- ⚔️ Developer vs Developer comparison
- 🖥️ FastAPI REST API backend
- 🌐 React frontend
- 🎈 Streamlit prototype (Live Deployment)
- ⚡ Fast response using Groq inference
- 🔒 Environment variable support for API keys

---

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | React.js |
| Backend | FastAPI |
| Prototype UI | Streamlit |
| AI Model | LLaMA 3 (Groq API) |
| Data Source | GitHub REST API |
| Languages | Python, JavaScript |

---

# 🏗 Architecture

```text
               React Frontend
                     │
                     ▼
              FastAPI Backend
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
 GitHub REST API             Groq API
                              (LLaMA 3)
                     │
                     ▼
             AI Generated Roast
```

---

# 📂 Project Structure

```text
github-roaster/
│
├── backend/
│   └── main.py
│
├── frontend/
│
├── streamlit-version/
│   ├── app.py
│   └── backend.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Live Demo

### 🌍 Try it here

https://git-roast.streamlit.app/

---

# 📸 Screenshots

> Add screenshots here after deployment.

### Home Page

```
images/home.png
```

### Roast Result

```
images/result.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Nitin225/github-roaster.git
cd github-roaster
```

---

## Backend

```bash
cd backend

pip install -r ../requirements.txt

uvicorn main:app --reload
```

Runs on

```
http://localhost:8000
```

---

## React Frontend

```bash
cd frontend

npm install

npm start
```

Runs on

```
http://localhost:3000
```

---

## Streamlit Version

```bash
cd streamlit-version

pip install -r ../requirements.txt

streamlit run app.py
```

Runs on

```
http://localhost:8501
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /roast | Roast a GitHub profile |
| POST | /compare | Compare two GitHub profiles |
| GET | /docs | FastAPI Swagger Documentation |

---

# 💻 Usage

1. Open the application.
2. Enter a GitHub username.
3. Select roast intensity.
4. Generate an AI roast.
5. Compare developers.

---

# 🎯 Future Improvements

- GitHub profile score
- Roast history
- Share roast on X/LinkedIn
- Dark mode
- Download roast as image
- Multi-language support
- Leaderboard

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a Pull Request.

---

# ⚠ Disclaimer

This project is intended purely for entertainment purposes.

All outputs are AI-generated and should not be taken personally.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Nitin Kumar**

GitHub

https://github.com/Nitin225

LinkedIn

(Add your LinkedIn profile here)

⭐ If you like this project, don't forget to star the repository!
