# app/ai.py
import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analisar_por_pais(ncm: str, descricao: str, ano: str, dados: list, fluxo: str = "export") -> str:

    fluxo_texto = "exportação" if fluxo == "export" else "importação"
    destino_texto = "destino" if fluxo == "export" else "origem"

    ranking = "\n".join(
        [f"{i+1}. {item['country']}: USD {int(item['metricFOB']):,}"
         for i, item in enumerate(dados[:10])]
    )

    prompt = f"""
Você é um especialista em comércio exterior brasileiro.

Analise os dados abaixo de {fluxo_texto} do produto NCM {ncm} ({descricao}) no ano de {ano}:

Top 10 países de {destino_texto} (valor FOB em USD):
{ranking}

Com base nesses dados, forneça:
1. Uma análise do padrão geográfico das {fluxo_texto}s
2. Inferências sobre o porquê desses países predominarem
3. Possíveis oportunidades ou riscos que esses dados sugerem

Seja direto e use linguagem acessível. Máximo 3 parágrafos.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    resposta = response.choices[0].message.content
    resposta = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', resposta)
    return resposta