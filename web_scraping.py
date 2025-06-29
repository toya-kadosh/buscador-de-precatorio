import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir CORS para frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def scrape_trf3(cpf_cnpj: str):
    url = "https://web.trf3.jus.br/consultas/precatorios"
    params = {"cpfCnpj": cpf_cnpj}
    resp = requests.get(url, params=params, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    # Exemplo: extraia dados relevantes
    results = []
    for row in soup.select("table tr"):
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if cols:
            results.append(cols)
    return results

def scrape_trf1(cpf_cnpj: str):
    url = "https://portal.trf1.jus.br/consultas/precatorios"
    params = {"cpfCnpj": cpf_cnpj}
    resp = requests.get(url, params=params, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for row in soup.select("table tr"):
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if cols:
            results.append(cols)
    return results

@app.get("/api/precatorios")
def buscar_precatorios(cpf_cnpj: str = Query(...)):
    trf3 = scrape_trf3(cpf_cnpj)
    trf1 = scrape_trf1(cpf_cnpj)
    return {"trf3": trf3, "trf1": trf1}