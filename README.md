# 🏥 MedRoute Pro — Medical Report Intelligence System

MedRoute Pro is a clinical decision support prototype that uses Natural Language Processing (NLP) to classify medical reports and automatically assign patients to appropriate hospital specialties.

---

## 🚀 Features

- 🧠 AI-based medical report classification
- 📊 Confidence scoring visualization
- 🏥 Automatic department assignment
- 👨‍⚕️ Patient management dashboard
- ⚡ FastAPI backend with real-time predictions

---

## 🛠️ Tech Stack

- Backend: FastAPI, Scikit-learn, NLTK
- Frontend: HTML, CSS, JavaScript
- Model: TF-IDF + Linear SVC

---

## 📂 Project Structure

medroute-pro/
│
├── backend/ → API + ML model
├── frontend/ → UI interface
├── requirements.txt
├── README.md

---

## ▶️ How to Run

```bash
git clone https://github.com/Pranavg812/medroute-pro.git
cd medroute-pro

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.app:app --reload
```

Open:
http://127.0.0.1:8000

---

## 🧪 Demo Flow

1. Enter patient details
2. Paste medical transcription
3. Click "Classify"
4. View predicted specialty and confidence
5. Patient appears in dashboard

---

## ⚠️ Disclaimer

This project is for academic demonstration purposes only and not intended for real clinical use.

---

## 👨‍💻 Author

Pranav Goyal
