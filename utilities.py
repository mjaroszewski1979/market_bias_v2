# Importing smtplib for SMTP protocol implementation to send emails programmatically.
import smtplib
# Importing imghdr module to determine the type of image data from file headers.
import imghdr
# Importing EmailMessage class from email.message to construct email messages.
from email.message import EmailMessage
# Importing datetime module to handle dates and times in the code.
import datetime
# Importing numpy as np for numerical operations and array manipulations.
import numpy as np
# Importing pandas_datareader as pdr for fetching data from various sources including Yahoo Finance.
import pandas_datareader as pdr
# Importing pandas as pd for data manipulation and analysis.
import pandas as pd
# Importing RemoteDataError from pandas_datareader._utils to handle data retrieval errors.
from pandas_datareader._utils import RemoteDataError
# Importing environ function from os module to access environment variables.
from os import environ

# Retrieving email address from environment variables.
email_address = environ.get('EMAIL_ADDRESS')
# Retrieving email password from environment variables.
email_password = environ.get('EMAIL_PASSWORD')

# Function to send emails using Gmail SMTP server
def send_mail(email):
    message = "Your free ebook from Market Bias"
    
    # Creating an instance of EmailMessage
    msg = EmailMessage()
    msg['Subject'] = 'Free Ebook'  # Setting the email subject.
    msg['From'] = 'Market Bias' # Setting the sender's name.
    msg['To'] = email # Setting the recipient's email address.
    msg.set_content(message)  # Setting the email message content.

    # Attaching a PDF file to the email message using a context manager
    with open('MarketBiasEbook.pdf', 'rb') as f:
        file_data = f.read()  # Reading the file data.
        file_type = imghdr.what(f.name)  # Determining the file type using imghdr.
        file_name = f.name  # Getting the file name.

        # Adding the file as an attachment to the email message
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  

    # Establishing a secure SMTP connection with Gmail server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)  # Logging in to the SMTP server using provided credentials.
        smtp.send_message(msg)  # Sending the email message.

# Function to fetch historical data of S&P 500 index from Yahoo Finance API
def get_trend_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol='^GSPC'):
    items = {}  # Initializing a dictionary to store fetched data and metadata.
    try:
        # Fetching historical data from Yahoo Finance.
        data = pdr.get_data_yahoo(symbol, start, end)
        items['data'] = data  # Storing complete dataset.
        items['high'] = data['High']  # Storing high prices.
        items['low'] = data['Low']  # Storing low prices.
        items['open'] = data['Open']  # Storing opening prices.
        items['close'] = data['Adj Close']  # Storing adjusted closing prices.
        items['last_close'] = data['Adj Close'][-1]  # Storing the latest adjusted closing price.
        items['error'] = None  # Resetting error status to None upon successful data retrieval.
    except RemoteDataError:
        items['error'] = 'Fetching data failed due to an error on the yahoo finance server. Please come back later.'

    # Returning the dictionary containing fetched data and metadata.
    return items

# Function to fetch percentage change data of multiple stock indices from Yahoo Finance API
def get_strategies_data(start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), symbol=['^GSPC', '^IXIC', '^DJI', '^N225', '^FCHI', '^GDAXI', '^RUT', 'EPOL', 'EWC', 'TUR', '^NSEI', 'MCHI', 'EWY', 'EWT', 'EWZ', 'EWA', 'EWW', 'EWL', 'EWN', 'EZA', 'EWU']):
    try:
        data = pdr.get_data_yahoo(symbol, start, end)  # Fetching historical data of specified symbols.
        data = data[['Adj Close']].pct_change(periods=252) * 100  # Calculating annualized percentage change.
        data = round(data, 2)  # Rounding off percentage change values.
        data = data[['Adj Close']]  # Selecting only adjusted closing price percentage changes.
        data = data.dropna()  # Dropping any NaN values from the dataset.
        return data  # Returning the processed percentage change data.
    except RemoteDataError:
        print('There was an error') # Handling RemoteDataError
