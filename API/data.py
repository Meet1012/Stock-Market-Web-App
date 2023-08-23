import yfinance as yf
import pandas as pd
from datetime import datetime
import json

yf.pdr_override()


def fetchdata(symbol):

    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)

    res = yf.download(symbol, start, end)

    parsed_data = res.to_json()
    actual_data = json.loads(parsed_data)
    closeres = list(actual_data["Close"].values())
    closelst = [i for i in closeres]
    dateres = list(actual_data["Close"].keys())
    datelst = [int(i) for i in dateres]

    data = {
        "c": closelst,
        "h": [0,1],
        "l": [0,1],
        "o": [221.03, 218.55, 220],
        "s": "ok",
        "t": datelst,
    }
    return data

def fetchquote(stockSymbol):
    
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)

    res = yf.download(stockSymbol, start, end)

    parsed_data = res.to_json()
    actual_data = json.loads(parsed_data)
    closeres = list(actual_data["Close"].values())
    closelst = [i for i in closeres]
    openres = list(actual_data["Open"].values())
    openlst = [int(i) for i in openres]
    c,o = closelst[-1],openlst[-1]
    diff = c-o
    d = format(diff,".2f")
    percent = (diff/o)*100
    dp = format(percent,".2f")
    
    quotedata = {
    "c": c,
    "h": 263.31,
    "l": 260.68,
    "o": o,
    "pc": 259.45,
    "t": 328364823,
    "d": d,
    "dp": dp
  }
    return quotedata



detaildata = {
    "AAPL": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Technology",
        "ipo": "1980-12-12",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/AAPL.svg",
        "marketCapitalization": 3037684.322728,
        "name": "Apple Inc",
        "phone": "14089961010.0",
        "shareOutstanding": 15728.7,
        "ticker": "AAPL",
        "weburl": "https://www.apple.com/",
    },
    "AMZN": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Retail",
        "ipo": "1997-05-15",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/AMZN.svg",
        "marketCapitalization": 1333435.6117769997,
        "name": "Amazon.com Inc",
        "phone": "12062661000.0",
        "shareOutstanding": 10260.4,
        "ticker": "AMZN",
        "weburl": "https://www.amazon.com/",
    },
    "MSFT": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Leisure Products",
        "ipo": "2015-07-17",
        "logo": "https://static.finnhub.io/logo/4dd246ac-80d2-11ea-ba13-00000000092a.png",
        "marketCapitalization": 486.54339,
        "name": "Mastercraft Boat Holdings Inc",
        "phone": "14238842221.0",
        "shareOutstanding": 17.4953,
        "ticker": "MCFT",
        "weburl": "https://investors.mastercraft.com/",
    },
    "GOOG": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Media",
        "ipo": "2004-08-19",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/GOOG.svg",
        "marketCapitalization": 1515539.992004,
        "name": "Alphabet Inc",
        "phone": "16502530000.0",
        "shareOutstanding": 12698,
        "ticker": "GOOGL",
        "weburl": "https://abc.xyz/",
    },
}

searchdata = {
    "count": 4,
    "result": [
        {
            "description": "APPLE INC",
            "displaySymbol": "AAPL",
            "symbol": "AAPL",
            "type": "Common Stock",
        },
        {
            "description": "AMAZON INC",
            "displaySymbol": "AMZN",
            "symbol": "AMZN",
            "type": "Common Stock",
        },
        {
            "description": "MICROSOFT INC",
            "displaySymbol": "MSFT",
            "symbol": "MSFT",
            "type": "Common Stock",
        },
        {
            "description": "GOOGLE INC",
            "displaySymbol": "GOOG",
            "symbol": "GOOG",
            "type": "Common Stock",
        },
    ],
}
