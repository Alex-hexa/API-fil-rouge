from pydantic import BaseModel, Field
from typing import Literal

class SinistreRequest(BaseModel):
    identifiant_sinistre: str
    type_sinistre: Literal["automobile", "habitation", "responsabilité civile"]
    montant_estime_euros: float = Field(ge=0)
    anciennete_contrat_mois: int = Field(ge=0)
    nombre_sinistres_anterieurs: int = Field(ge=0)
    age_assure: int = Field(ge=0)

class ScoringResponse(BaseModel):
    identifiant_sinistre: str
    score: int
    decision: str