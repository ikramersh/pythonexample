#from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_data, get_live_price

stockList = ['CBA.AX', 'TLS.AX']
#stockList = si.tickers_sp500()
for ticker in stockList:
    print(f'{ticker}: {get_live_price(ticker):.2f}')
#si.get_dividends('cba.ax')
