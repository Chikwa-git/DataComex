# app/comexstat.py
import urllib.request
import urllib.error
import json
from cache import get, set

BASE_URL = "https://api-comexstat.mdic.gov.br"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def _post(endpoint: str, payload: dict) -> dict:
    """Função interna que faz todas as chamadas POST à API."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}{endpoint}",
        data=data,
        headers=HEADERS,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        raise Exception(f"Erro na API: {e.code} {e.reason}")


def buscar_por_ncm(ncm: str, ano_inicio: str, ano_fim: str, fluxo: str = "export") -> list:
    """Retorna dados mensais de um NCM em um período."""
    chave = f"{fluxo}_{ncm}_{ano_inicio}_{ano_fim}_mensal"

    cached = get(chave)
    if cached:
        return cached

    payload = {
        "flow": fluxo,
        "monthDetail": True,
        "period": {
            "from": f"{ano_inicio}-01",
            "to": f"{ano_fim}-12"
        },
        "filters": [
            {"filter": "ncm", "values": [ncm]}
        ],
        "details": ["ncm"],
        "metrics": ["metricFOB"]
    }
    resultado = _post("/general", payload)
    dados = resultado["data"]["list"]
    set(chave, dados)
    return dados


def buscar_por_pais(ncm: str, ano: str, fluxo: str = "export") -> list:
    """Retorna dados por país de destino/origem para um NCM."""
    chave = f"{fluxo}_{ncm}_{ano}_pais"

    cached = get(chave)
    if cached:
        return cached

    payload = {
        "flow": fluxo,
        "monthDetail": False,
        "period": {
            "from": f"{ano}-01",
            "to": f"{ano}-12"
        },
        "filters": [
            {"filter": "ncm", "values": [ncm]}
        ],
        "details": ["ncm", "country"],
        "metrics": ["metricFOB"]
    }
    resultado = _post("/general", payload)
    dados = resultado["data"]["list"]
    set(chave, dados)
    return dados