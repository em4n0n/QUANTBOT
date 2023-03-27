

import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_sp500_instruments():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))
    return list(df[0]["Symbol"])

tickers = get_sp500_instruments()
print(tickers) # sp500 tickers obtained in a list