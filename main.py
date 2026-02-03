from fastapi import FastAPI, HTTPException
from models import SinistreRequest, ScoringResponse
from scoring import calculer_score

app = FastAPI(title="API de Scoring de Sinistre")

db_sinistres = {}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/score", response_model=ScoringResponse)
async def post_sinistre(request: SinistreRequest):
    score, decision = calculer_score(request.model_dump())
    result = {
        "identifiant_sinistre": request.identifiant_sinistre,
        "score": score,
        "decision": decision
    }
    db_sinistres[request.identifiant_sinistre] = result
    return result

@app.get("/sinistre/{identifiant}", response_model=ScoringResponse)
async def get_sinistre(identifiant: str):
    if identifiant not in db_sinistres:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    return db_sinistres[identifiant]