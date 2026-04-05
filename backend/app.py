from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
pipeline = joblib.load('backend/final_pipeline.joblib')

BASE_STOP = set(stopwords.words('english'))
EXTRA_STOP = {
    'sample', 'name', 'date', 'note', 'report', 'physician',
    'doctor', 'hospital', 'clinic', 'dictated', 'transcribed',
    'electronically', 'signed',
}
ALL_STOP = BASE_STOP.union(EXTRA_STOP)

ABBREV = {
    r'\bpt\b': 'patient', r'\bhx\b': 'history',
    r'\bdx\b': 'diagnosis', r'\brx\b': 'prescription',
    r'\bsob\b': 'shortness breath', r'\bcp\b': 'chest pain',
    r'\bhtn\b': 'hypertension', r'\bchf\b': 'heart failure',
    r'\bcopd\b': 'pulmonary disease', r'\bdm\b': 'diabetes',
    r'\bcva\b': 'stroke', r'\bca\b': 'cancer',
}

def preprocess(text: str) -> str:
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = re.sub(r'\b[a-z][a-z\s/]{2,}:\s*', ' ', text)
    for pat, rep in ABBREV.items():
        text = re.sub(pat, rep, text, flags=re.IGNORECASE)
    text = re.sub(r'\d+\.?\d*\s*(mg|cc|ml|mm|cm|kg|%|mcg)?\b', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = [w for w in text.split()
              if w not in ALL_STOP and len(w) > 2]
    return ' '.join(tokens)
app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# Request/response format
class ReportRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    specialty: str
    confidence: float
    all_scores: dict

@app.post("/predict")
def predict(req: ReportRequest):
    clean  = preprocess(req.text)
    
    prediction = pipeline.predict([clean])[0]
    
    decision = pipeline.decision_function([clean])[0]
    labels   = pipeline.classes_
    
    import numpy as np
    exp_scores = np.exp(decision - np.max(decision))
    softmax    = exp_scores / exp_scores.sum()
    
    scores    = {lab: round(float(p) * 100, 1) for lab, p in zip(labels, softmax)}
    top_conf  = scores[prediction]

    return PredictResponse(
        specialty  = prediction,
        confidence = top_conf,
        all_scores = scores
    )