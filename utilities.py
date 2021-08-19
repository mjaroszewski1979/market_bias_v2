import smtplib
import imghdr
from email.message import EmailMessage
import datetime
import numpy as np
import pandas_datareader as pdr
import pandas as pd
from pandas_datareader._utils import RemoteDataError
from os import environ

email_address = environ.get('EMAIL_ADDRESS')
email_password = environ.get('EMAIL_PASSWORD')


def send_mail(email):
    message = "Your free ebook from Market Bias"
    msg = EmailMessage()
    msg['Subject'] = 'Free Ebook'
    msg['From'] = 'Market Bias'
    msg['To'] = email
    msg.set_content(message)  

    with open('MarketBiasEbook.pdf', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def get_trend_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol='^GSPC'):
    items = {}
    try:
        data = pdr.get_data_yahoo(symbol, start, end)
        items['data'] = data
        items['high'] = data['High']
        items['low'] = data['Low']
        items['open'] = data['Open']
        items['close'] = data['Adj Close']
        items['last_close'] = data['Adj Close'][-1]
        items['error'] = None
    except RemoteDataError:
        items['error'] = 'Fetching data failed due to an error on the yahoo finance server. Please come back later.'
        
    return items

def get_strategies_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol=['^GSPC', '^IXIC', '^DJI', '^N225', '^FCHI', '^GDAXI', '^RUT', 'EPOL', 'EWC', 'TUR', '^NSEI', 'MCHI', 'EWY', 'EWT', 'EWZ', 'EWA', 'EWW', 'EWL', 'EWN', 'EZA', 'EWU']):
    try:
        data = pdr.get_data_yahoo(symbol, start, end)
        data = data[['Adj Close']].pct_change(periods=252) * 100
        data = round(data, 2)
        data = data[['Adj Close']]
        data = data.dropna()   
        return data
    except RemoteDataError:
        pass