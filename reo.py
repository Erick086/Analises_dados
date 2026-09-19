import pandas as pd
import streamlit as st

tabela = pd.read_csv("vendas_regioes.csv")

#TITULO
st.title("Dashboard de Vendas")

#CAMPO DE SELECAO E FILTRO DOS DADOS
regioes = st.multiselect("Selecione as regioes", tabela["regiao"].unique())

if regioes:
    tabela = tabela[tabela["regiao"].isin(regioes)]

#2 METRICAS

#FATURAMENTO TOTAL
st.metric("Faturamento Total", f"R${tabela['valor_venda'].sum()}")

#TICKET MEDIO
st.metric("Ticket Medio", f"R${tabela['valor_venda'].mean()}")

#GRAFICO FATURAMENTO POR REGIAO
st.bar_chart(tabela.groupby("regiao")["valor_venda"].sum())

#GRAFICO FATURAMENTO POR PRODUTO
st.bar_chart(tabela.groupby("produto")["valor_venda"].sum())