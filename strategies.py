import numpy as np
import pandas_datareader as pdr
import datetime
import pandas as pd
from trend import indis

def get_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol=['^GSPC', '^IXIC', '^DJI', '^N225', '^FCHI', '^GDAXI', '^RUT', 'EPOL', 'EWC', 'TUR', '^NSEI', 'MCHI', 'EWY', 'EWT', 'EWZ', 'EWA', 'EWW', 'EWL', 'EWN', 'EZA', 'EWU']):
    data = pdr.get_data_yahoo(symbol, start, end)
    data = data[['Adj Close']].pct_change(periods=252) * 100
    data = round(data, 2)
    data = data[['Adj Close']]
    data = data.dropna()   
    return data

if indis.error == None:

    data = get_data()

    class Indices:

        def __init__(self):
            
            self.indices = {
                'US/S&P 500' : data['Adj Close']['^GSPC'][-1],
                'US/NASDAQ' : data['Adj Close']['^IXIC'][-1],
                'US/DOW JONES' : data['Adj Close']['^DJI'][-1],
                'JAPAN/NIKKEI' : data['Adj Close']['^N225'][-1],
                'FRANCE/CAC 40' : data['Adj Close']['^FCHI'][-1],
                'GERMANY/DAX' : data['Adj Close']['^GDAXI'][-1],
                'US/RUSSELL 2000' : data['Adj Close']['^RUT'][-1],
                'POLAND/MSCI' : data['Adj Close']['EPOL'][-1],
                'CANADA/MSCI' : data['Adj Close']['EWC'][-1],
                'TURKEY/MSCI' : data['Adj Close']['TUR'][-1],
                'INDIA/NIFTY' : data['Adj Close']['^NSEI'][-1],
                'CHINA/MSCI' : data['Adj Close']['MCHI'][-1],
                'SOUTH KOREA/MSCI' : data['Adj Close']['EWY'][-1],
                'TAIWAN/MSCI' : data['Adj Close']['EWT'][-1],
                'BRAZIL/MSCI' : data['Adj Close']['EWZ'][-1],
                'AUSTRALIA/MSCI' : data['Adj Close']['EWA'][-1],
                'MEXICO/MSCI' : data['Adj Close']['EWW'][-1],
                'SWITZERLAND/MSCI' : data['Adj Close']['EWL'][-1],
                'NETHERLANDS/MSCI' : data['Adj Close']['EWN'][-1],
                'SOUTH AFRICA/MSCI' : data['Adj Close']['EZA'][-1],
                'UK/MSCI' : data['Adj Close']['EWU'][-1]
            }
            
            self.top_index = sorted([(v, k) for k, v in self.indices.items()], reverse=True)

    indices = Indices()

else:

    pass



    