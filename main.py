import streamlit as st
import pandas as pd
import Controllers.Produtocontroller as Produtocontroller

from Moldel.produto import produto


st.title("Estoque")
tipo_acao = st.selectbox("Selecione a ação:",["Adicionar Novo Produto", "Editar Produto Existente"])

if tipo_acao == "Adicionar Novo Produto":
    nome = st.text_input("Digite o nome do Produto: ")
    descricao = st.text_input("Faça uma descrição do Produto: ")
    preco = st.number_input("Digite o Preço unitario deste Produto: ", min_value=0)
    estoque = st.number_input("Digite a quantidade em Estoque", min_value=0)
