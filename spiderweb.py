import lib.globals as globals
from lib.getStockInfo import (getStockPrice,getLastDay,getMarketCap,getChartData,getCompsData,get1YearReturn,
                              getDividendInfo,getSplitInfo,getElementData,getMinMaxForOneYear,getDividendPaid)
from lib.getFinStat import getCompanyIdentity,updateFinancialStatement,getKPI




globals.initialize()

#updateFinancialStatement()
#getDividendInfo()
#getElementData()
#getSplitInfo()

symbol= ""
while symbol=="":
    ticker = input("Quote search:")
    results = getCompanyIdentity(ticker)
    if results!= None:
        symbol=results[0]
        sector=results[1]
    else:
        print("Quote is not valid")


getChartData(ticker)


stock = getStockPrice(ticker)
stockPrice = stock[0]
priceChange = stock[1]

oneYearReturn = get1YearReturn(stockPrice)

print("Ticker:"+ticker)
print("Current Price:"+stockPrice)
print("Change in Price (%):"+priceChange)

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

price_range = getMinMaxForOneYear()

price_max = price_range[0]
price_min = price_range[1]
print("52 week range: ["+str(price_min)+" - "+str(price_max)+"]")

capData= getMarketCap(ticker)

marketCap = capData[0]
shares = capData[1]
print("Market Capital:"+marketCap)


#getChartData(ticker)
kpi = getKPI(ticker,float(stockPrice),float(shares))
dividend = getDividendPaid(ticker)

eps = kpi[0]
peRatio = kpi[1]
ptobookRatio = kpi[2]
ptoSales = kpi[3]
fiscYear = kpi[4]
print("-----------Key Stat----")
print("EPS:"+eps)
print("P/E Ratio:"+peRatio)
print("1 Year return (%):"+oneYearReturn)


print("Shares Outstanding:"+shares)
print("Price to Book Ratio:"+ptobookRatio)
print("Price to Sales Ratio:"+ptoSales)
print("Dividend Yield (%):"+str(dividend[2]))
print("Last Dividend Reported ("+str(dividend[0])+"): "+str(dividend[1]))

print("Earnings Announcement for fiscal period ending in "+fiscYear)

print("-----------COMPARE 1 DAY performance (%)----")

compsData = getCompsData(sector,globals.market_indice)
sector_change = compsData[0]
market_change = compsData[1]

print("EQUITY\n"+ticker+" : "+priceChange)
print("SECTOR\n"+sector+" : "+sector_change)
print("MARKET\n"+globals.market_indice+" : "+market_change)

print("-----------ABOUT THE COMPANY----")
