from pathlib import Path
import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

def mostra_tabela_produtos():
     st.dataframe(df_produtos)

def mostra_tabela_filiais():
     st.dataframe(df_filiais)
    
def mostra_tabela_vendas():
     st.dataframe(df_vendas)

st.sidebar.markdown('## Seleção de Tabelas')
tabela_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:',
                                          ['Vendas','Produtos','Filiais'])

if tabela_selecionada == 'Produtos':
   mostra_tabela_produtos()
elif tabela_selecionada == 'Filiais':
   mostra_tabela_filiais()
elif tabela_selecionada == 'Vendas':
   mostra_tabela_vendas()



