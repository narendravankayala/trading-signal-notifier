import os
import yfinance as yf
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Get environment variables
GMAIL_USER = os.environ.get('GMAIL_USER')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

# Trading Strategy Parameters
STOCKS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 
    'JNJ', 'V', 'PG', 'UNH', 'HD', 'DIS', 'MA', 'PYPL', 'ADBE', 
    'NFLX', 'CRM', 'NKE', 'INTC', 'VZ', 'KO', 'PFE', 'MRK', 'T', 
    'WMT', 'CSCO', 'ABT', 'PEP', 'TMO', 'CVX', 'XOM', 'BAC', 'WFC',
    'GS', 'ENPH'
]
