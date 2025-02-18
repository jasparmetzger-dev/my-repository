import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date

startdate = input('Startdate: ')
enddate = date.today()
avg_len = int(input('Length of the Average: '))

stock1_name = input('Ticker for first stock: ').upper()
stock1_data = yf.download(stock1_name, start= startdate, end= enddate)
data1 = stock1_data['Close'].pct_change()

stock2_name = input('Ticker for second stock: ').upper()
stock2_data = yf.download(stock2_name, start= startdate, end= enddate)
data2 = stock2_data['Close'].pct_change()

avg1 = data1.rolling(window= avg_len).mean()
avg2 = data2.rolling(window= avg_len).mean()

plt.figure(figsize=(10, 6))

plt.plot(data1, color='blue')
plt.plot(avg1, color= 'lightblue')
plt.plot(data2, color= 'red')
plt.plot(avg2, color= 'orange')



plt.title(f'{stock1_name} and {stock2_name} Stock Price')
plt.xlabel('Date')
plt.ylabel('Change in %')
plt.legend()
plt.grid()
plt.show()
