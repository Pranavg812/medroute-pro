# 🏥 MedRoute Pro — Medical Report Intelligence System

MedRoute Pro is an AI-powered clinical decision support prototype designed to assist hospitals in automatically classifying medical reports into appropriate specialties.

---

## 🚀 Features

- 🧠 NLP-based medical report classification
- 📊 Confidence scoring with visualization
- 🏥 Automatic department assignment
- 👨‍⚕️ Patient management dashboard
- ⚡ FastAPI backend + clean frontend UI

---

## 🛠️ Tech Stack

- Backend: FastAPI, Scikit-learn, NLTK
- Frontend: HTML, CSS, JavaScript
- Model: TF-IDF + Linear SVC

---

## 📂 Project Structure

medroute-pro/
│
├── backend/
│ ├── app.py
│ ├── final_pipeline.joblib
│
├── frontend/
│ └── index.html
│
├── requirements.txt
├── README.md
├── .gitignore

## ▶️ How to Run

```bash
git clone https://github.com/Pranavg812/medroute-pro.git
cd medroute-pro

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.app:app --reload
```
