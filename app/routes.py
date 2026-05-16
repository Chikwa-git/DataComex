# app/routes.py
from flask import Blueprint, render_template, request
from comexstat import buscar_por_pais, buscar_por_ncm
from ai import analisar_por_pais

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analisar', methods=['POST'])
def analisar():
    ncm = request.form.get('ncm', '').strip()
    ncm = ncm.replace('.', '') 
    ano = request.form.get('ano', '').strip()
    fluxo = request.form.get('fluxo', 'export')

    if not ncm or not ano:
        return render_template('index.html', erro="Preencha o NCM e o ano.")

    try:
        dados_pais = buscar_por_pais(ncm, ano, fluxo)
        dados_mensal = buscar_por_ncm(ncm, ano, ano, fluxo)

        # pega a descrição do produto do primeiro resultado
        descricao = dados_pais[0]['ncm'] if dados_pais else ncm

        analise = analisar_por_pais(ncm, descricao, ano, dados_pais, fluxo)

        return render_template(
            'result.html',
            ncm=ncm,
            ano=ano,
            fluxo=fluxo,
            descricao=descricao,
            dados_pais=dados_pais[:10],
            dados_mensal=sorted(dados_mensal, key=lambda x: x['monthNumber']),
            analise=analise
        )

    except Exception as e:
        return render_template('index.html', erro=f"Erro ao consultar: {str(e)}")