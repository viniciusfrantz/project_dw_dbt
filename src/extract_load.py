# import

from sqlalchemy import create_engine
from dotenv import load_dotenv
import yfinance as yf
import os
import pandas as pd

#import environment vars

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def data_search_commodities(simbol, period='5d', interval='1d'):
    ticker = yf.Ticker(simbol)
    data =  ticker.history(period=period, interval=interval)[['Close']]
    data['simbol'] = simbol
    return data

def search_all_commodities(commodities):
    all_data = []
    for ticker in commodities:
        data = data_search_commodities(ticker)
        all_data.append(data)
    return pd.concat(all_data)


def save_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

if __name__ == "__main__":
    concatened_data = search_all_commodities(commodities)
    save_postgres(concatened_data, schema='public')

#take the quote of actives


