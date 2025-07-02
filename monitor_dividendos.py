import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Função para buscar dividendos de um ativo
def buscar_dividendos(ticker):
    url = f"https://brapi.dev/api/quote/dividends?symbol={ticker}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados.get("dividends", [])
    return []

# Função para calcular dividendos acumulados
def calcular_total_dividendos(carteira, meses=12):
    resultados = []
    data_limite = datetime.now() - timedelta(days=30 * meses)

    for ticker, qtd in carteira.items():
        dividendos = buscar_dividendos(ticker)
        total = 0.0
        for d in dividendos:
            try:
                data_pagamento = datetime.strptime(d["paymentDate"], "%Y-%m-%d")
                if data_pagamento >= data_limite:
                    valor_por_acao = float(d["value"])
                    total += valor_por_acao * qtd
            except:
                continue
        resultados.append({"Ticker": ticker, "Quantidade": qtd, "Total R$": round(total, 2)})

    return pd.DataFrame(resultados)

# Interface Streamlit
st.set_page_config(page_title="Monitor de Dividendos", layout="wide")
st.title("📈 Monitor de Carteira com Dividendos – Gans Academy")

st.markdown("Insira os ativos da sua carteira abaixo:")

tickers_input = st.text_area("Tickers (um por linha, com quantidade. Ex: ITUB4,100)", "ITUB4,100\nTAEE11,50\nBBAS3,80")

carteira = {}
for linha in tickers_input.strip().split("\n"):
    try:
        ticker, qtd = linha.strip().split(",")
        carteira[ticker.strip().upper()] = int(qtd)
    except:
        st.warning(f"Linha ignorada: {linha}")

meses = st.slider("Período (meses):", 3, 36, 12)

if st.button("🔍 Calcular Dividendos"):
    with st.spinner("Buscando dados..."):
        df_resultado = calcular_total_dividendos(carteira, meses)
        st.success("Cálculo concluído!")
        st.dataframe(df_resultado)

        total = df_resultado["Total R$"].sum()
        st.metric("Total de dividendos acumulados (R$)", f"{total:,.2f}".replace(".", ","))

        # Gráfico
        fig, ax = plt.subplots()
        ax.bar(df_resultado["Ticker"], df_resultado["Total R$"])
        ax.set_ylabel("Total em R$")
        ax.set_title("Dividendos por Ativo")
        st.pyplot(fig)
