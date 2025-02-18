import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from ta.momentum import RSIIndicator

#strategy data is red, market data is blue

ticker = 'MSCI'
start = '2020-01-01'
rsi_period = 14 

#get correct data

data = yf.download(ticker, start= start, end= date.today())
print(data)
data['RSI'] = RSIIndicator(data['Close'], window=rsi_period).rsi()

#setup buy/sell

data['Signal'] = 0
data.loc[data['RSI'] <= 30, 'Signal'] = 1
data.loc[data['RSI'] >= 70, 'Signal'] = -1

data['Position'] = data['Signal'].shift()
data['Daily'] = data['Close'].pct_change()
data['Strategy'] = data['Position'] * data['Daily']

#eval performance

cumul_strat = (1 + data['Strategy']).cumprod()
cumul_market = (1 + data['Daily']).cumprod()

plt.figure(figsize= (10, 6))
print(cumul_strat)