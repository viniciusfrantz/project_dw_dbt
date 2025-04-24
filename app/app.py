# import

from sqlalchemy import create_engine
from dotenv import load_dotenv
import yfinance as yf
import os
import pandas as pd
import streamlit as st

#import environment vars

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT
        *
    FROM
        public.dm_commodities;
    """
    df = pd.read_sql(query, engine)
    return df

# Configuração da página
st.set_page_config(page_title="📊 Dashboard de Commodities", layout="wide")

# Título
st.title("📈 Visão Geral de Commodities")
st.markdown("Explore as ordens de commodities com base na base de dados atualizada.")

# Obter dados
df = get_data()

# Verifica se há dados
if not df.empty:
    st.subheader("📋 Tabela de Dados")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado na tabela.")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Vinicius Frantz | Powered by Streamlit & PostgreSQL")


