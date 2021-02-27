from pandas_datareader import data as wb

tickers = ['TSLA', 'AAPL', 'PLTR']
start_date = '2020-1-1'
end_date = '2021-2-27'

for i in tickers:
    wb.DataReader(tickers, 'yahoo', start_date, end_date)['Adj Close'].to_csv(i + ".csv")
