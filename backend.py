# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Buscador de Precatório API")

# Modelo de dados para Precatório
class Precatorio(BaseModel):
    id: int
    nome: str
    valor: float
    tribunal: str
    status: str

# Banco de dados em memória (exemplo)
db_precatorios = [
    Precatorio(id=1, nome="João Silva", valor=100000.0, tribunal="TRF1", status="Pendente"),
    Precatorio(id=2, nome="Maria Souza", valor=250000.0, tribunal="TRF2", status="Pago"),
]

@app.get("/precatorios", response_model=List[Precatorio])
def listar_precatorios(status: Optional[str] = None):
    if status:
        return [p for p in db_precatorios if p.status.lower() == status.lower()]
    return db_precatorios

@app.get("/precatorios/{precatorio_id}", response_model=Precatorio)
def obter_precatorio(precatorio_id: int):
    for p in db_precatorios:
        if p.id == precatorio_id:
            return p
    raise HTTPException(status_code=404, detail="Precatório não encontrado")

@app.post("/precatorios", response_model=Precatorio)
def criar_precatorio(precatorio: Precatorio):
    db_precatorios.append(precatorio)
    return precatorio

@app.put("/precatorios/{precatorio_id}", response_model=Precatorio)
def atualizar_precatorio(precatorio_id: int, precatorio: Precatorio):
    for idx, p in enumerate(db_precatorios):
        if p.id == precatorio_id:
            db_precatorios[idx] = precatorio
            return precatorio
    raise HTTPException(status_code=404, detail="Precatório não encontrado")

@app.delete("/precatorios/{precatorio_id}")
def deletar_precatorio(precatorio_id: int):
    for idx, p in enumerate(db_precatorios):
        if p.id == precatorio_id:
            del db_precatorios[idx]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Precatório não encontrado")