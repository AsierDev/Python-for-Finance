from pandas_datareader import data as wb
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tickers = ['TSLA', 'GOOGL', 'AAPL', 'FB']
start_date = '2020-2-20'
end_date = '2021-2-27'

data = wb.DataReader(tickers, 'yahoo', start_date, end_date)['Adj Close']
returns = data.pct_change()
log_returns = np.log(1 + data.pct_change())

sns.histplot(log_returns)
plt.xlabel("Retornos diarios")
plt.ylabel("Frecuencia")
plt.show()
