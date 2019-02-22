import globals
from lib.getStockInfo import getStockPrice,getLastDay,getMarketCap,getChartData,getCompsData
from lib.getFinStat import checkSymbol,updateFinData,getKPI


#updateFinData()

globals.initialize()

q=0
while q==0:
    #ticker = input("Quote search:")
    ticker = "PALC"
    sector = checkSymbol(ticker)
    if sector == None:
        print("Quote is not valid")
    else:
        q=1


getChartData(ticker)

quit()
stock = getStockPrice(ticker,sector)
stockTicker = stock[0]
stockPrice = stock[1]
priceChange = stock[2]

print("Ticker:"+stockTicker)
print("Current Price:"+stockPrice)
print("Change in Price:"+priceChange)

lastTrend = getLastDay(ticker)

stockTicker = lastTrend[0]
companyName = lastTrend[1]
stockVolume = lastTrend[2]
openPrice = lastTrend[3]
prevClose = lastTrend[4]

print("Company Name:"+companyName)
print("Volume:"+stockVolume)
print("Open Price:"+openPrice)
print("Prev Close:"+prevClose)

capData= getMarketCap(ticker)

marketCap = capData[0]
MarketCapChange = capData[1]
shares = capData[2]

print("Market Cap:"+marketCap)
print("Change in MarkCap:"+MarketCapChange)

#getChartData(ticker)
kpi = getKPI(ticker,float(stockPrice),float(shares))

eps = kpi[0]
peRatio = kpi[1]
ptobookRatio = kpi[2]
ptoSales = kpi[3]
fiscYear = kpi[4]
print("-----------Key Stat----")
print("EPS:"+eps)
print("P/E Ratio:"+peRatio)
print("Shares Outstanding:"+shares)
print("Price to Book Ratio:"+ptobookRatio)
print("Price to Sales Ratio:"+ptoSales)
print("Earnings Announcement for fiscal period ending in "+fiscYear)

print("-----------COMPARE 1 DAY performance----")

compsData = getCompsData(sector,globals.market_indice)
sector_change = compsData[0]
market_change = compsData[1]

print("EQUITY\n"+ticker+" : "+priceChange)
print("SECTOR\n"+sector+" : "+sector_change)
print("MARKET\n"+globals.market_indice+" : "+market_change)

print("-----------ABOUT THE COMPANY----")
