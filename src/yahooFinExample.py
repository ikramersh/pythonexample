from yahoo_fin.stock_info import get_live_prices, get_live_price, 
tickers_nasdaq


stockList = ['CBA.AX', 'TLS.AX', 'amp.ax', 'ori.ax', 'bxb.ax']
livePrices = get_live_prices(stockList)
for livePrice in livePrices.items():
    print(livePrice[0], livePrice[1])

for ticker in stockList:
    print(f'{ticker}: {get_live_price(ticker):.3f}')
stockList = tickers_nasdaq()

print("Done")
