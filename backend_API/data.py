import yfinance as yf
from datetime import datetime
import json
from model import predict_data

yf.pdr_override()


def fetchdata(symbol):
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)

    res = yf.download(symbol, start, end)
    to_predict_data = res.filter(["Close"])
    parsed_data = res.to_json()
    actual_data = json.loads(parsed_data)
    closeres = list(actual_data["Close"].values())
    closelst = [float(format(i, ".2f")) for i in closeres]
    dateres = list(actual_data["Close"].keys())
    datelst = [int(i) for i in dateres]
    p_value = predict_data(to_predict_data)
    # final = closelst[90:] + p_value[159:]

    data = {
        "c": closelst[60:],
        "h": [0, 1],
        "l": [0, 1],
        "o": [221.03, 218.55, 220],
        "s": "ok",
        "t": datelst[60:],
        "p": p_value,
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
    c, o = closelst[-1], openlst[-1]
    diff = c - o
    d = format(diff, ".2f")
    percent = (diff / o) * 100
    dp = format(percent, ".2f")
    pc_value = format(closelst[-1], ".2f")

    quotedata = {
        "c": c,
        "h": 263.31,
        "l": 260.68,
        "o": o,
        "pc": pc_value,
        "t": 328364823,
        "d": d,
        "dp": dp,
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
    "AAL": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Airlines",
        "ipo": "2013-12-09",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/AAL.svg",
        "marketCapitalization": 8418.575118615176,
        "name": "American Airlines Group Inc",
        "phone": "16822789000.0",
        "shareOutstanding": 653.36,
        "ticker": "AAL",
        "weburl": "https://americanairlines.gcs-web.com/",
    },
    "ADBE": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Technology",
        "ipo": "1986-08-20",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/ADBE.svg",
        "marketCapitalization": 240596.45018638566,
        "name": "Adobe Inc",
        "phone": "14085366000.0",
        "shareOutstanding": 455.3,
        "ticker": "ADBE",
        "weburl": "https://www.adobe.com/",
    },
    "ADEA": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Technology",
        "ipo": "2003-11-13",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/XPER.svg",
        "marketCapitalization": 965.4776273268066,
        "name": "Adeia Inc",
        "phone": "14084732500.0",
        "shareOutstanding": 106.75,
        "ticker": "ADEA",
        "weburl": "https://adeia.com/",
    },
    "ADP": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Professional Services",
        "ipo": "1961-09-01",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/ADP.svg",
        "marketCapitalization": 101700.98499903498,
        "name": "Automatic Data Processing Inc",
        "phone": "19739745000.0",
        "shareOutstanding": 411.97,
        "ticker": "ADP",
        "weburl": "https://www.adp.com/",
    },
    "ACN": {
        "country": "IE",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Technology",
        "ipo": "2001-07-19",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/ACN.svg",
        "marketCapitalization": 198214.82489857703,
        "name": "Accenture PLC",
        "phone": "35316462000.0",
        "shareOutstanding": 664.31,
        "ticker": "ACN",
        "weburl": "https://www.accenture.com/ie-en/",
    },
    "ALTO": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Chemicals",
        "ipo": "2005-03-24",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/ALTO.svg",
        "marketCapitalization": 302.1308502177215,
        "name": "Alto Ingredients Inc",
        "phone": "19164032123.0",
        "shareOutstanding": 75.91,
        "ticker": "ALTO",
        "weburl": "https://www.altoingredients.com/",
    },
    "META": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Media",
        "ipo": "2012-05-18",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/FB.svg",
        "marketCapitalization": 811652.307553223,
        "name": "Meta Platforms Inc",
        "phone": "16505434800.0",
        "shareOutstanding": 2573.16,
        "ticker": "META",
        "weburl": "https://investor.fb.com/",
    },
    "TSLA": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Automobiles",
        "ipo": "2010-06-09",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/TSLA.svg",
        "marketCapitalization": 826920.7182461714,
        "name": "Tesla Inc",
        "phone": "15125168177.0",
        "shareOutstanding": 3173.99,
        "ticker": "TSLA",
        "weburl": "https://www.tesla.com/",
    },
    "CSCO": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NASDAQ NMS - GLOBAL MARKET",
        "finnhubIndustry": "Communications",
        "ipo": "1990-02-16",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/950800186156.svg",
        "marketCapitalization": 216732.1410022254,
        "name": "Cisco Systems Inc",
        "phone": "14085264000.0",
        "shareOutstanding": 4054.86,
        "ticker": "CSCO",
        "weburl": "https://www.cisco.com/",
    },
    "V": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Financial Services",
        "ipo": "2008-03-25",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/V.svg",
        "marketCapitalization": 478391.3287040891,
        "name": "Visa Inc",
        "phone": "16504323200.0",
        "shareOutstanding": 2035.36,
        "ticker": "V",
        "weburl": "https://usa.visa.com/",
    },
    "XOM": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Energy",
        "ipo": "1980-03-17",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/XOM.svg",
        "marketCapitalization": 427233.3012838722,
        "name": "Exxon Mobil Corp",
        "phone": "19729406000.0",
        "shareOutstanding": 4003.19,
        "ticker": "XOM",
        "weburl": "https://corporate.exxonmobil.com/",
    },
    "JPM": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Banking",
        "ipo": "1969-03-05",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/JPM.svg",
        "marketCapitalization": 421672.9452460938,
        "name": "JPMorgan Chase \u0026 Co",
        "phone": "12122706000.0",
        "shareOutstanding": 2906.09,
        "ticker": "JPM",
        "weburl": "https://www.jpmorganchase.com/",
    },
    "WMT": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Retail",
        "ipo": "1972-08-25",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/WMT.svg",
        "marketCapitalization": 420987.48640100186,
        "name": "Walmart Inc",
        "phone": "14792734000.0",
        "shareOutstanding": 2691.56,
        "ticker": "WMT",
        "weburl": "https://corporate.walmart.com",
    },
    "MA": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Financial Services",
        "ipo": "2006-05-25",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/MA.svg",
        "marketCapitalization": 374972.2583083466,
        "name": "Mastercard Inc",
        "phone": "19142492000.0",
        "shareOutstanding": 942.21,
        "ticker": "MA",
        "weburl": "https://www.mastercard.us/",
    },
    "ORCL": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Technology",
        "ipo": "1986-03-12",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/ORCL.svg",
        "marketCapitalization": 301221.7781411607,
        "name": "Oracle Corp",
        "phone": "17378671000.0",
        "shareOutstanding": 2739.38,
        "ticker": "ORCL",
        "weburl": "https://www.oracle.com/",
    },
    "KO": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Beverages",
        "ipo": "1950-01-26",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/KO.svg",
        "marketCapitalization": 229795.70940229247,
        "name": "Coca-Cola Co",
        "phone": "14046762121.0",
        "shareOutstanding": 4324.34,
        "ticker": "KO",
        "weburl": "https://www.coca-colacompany.com/",
    },
    "PFE": {
        "country": "US",
        "currency": "USD",
        "estimateCurrency": "USD",
        "exchange": "NEW YORK STOCK EXCHANGE, INC.",
        "finnhubIndustry": "Pharmaceuticals",
        "ipo": "1944-01-17",
        "logo": "https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/PFE.svg",
        "marketCapitalization": 187050.64415128357,
        "name": "Pfizer Inc",
        "phone": "12127332323.0",
        "shareOutstanding": 5645.96,
        "ticker": "PFE",
        "weburl": "https://www.pfizer.com/",
    },
}

searchdata = {
    "count": 10,
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
        {
            "description": "AMERICAN AIRLINES",
            "displaySymbol": "AAL",
            "symbol": "AAL",
            "type": "Common Stock",
        },
        {
            "description": "ADOBE INC",
            "displaySymbol": "ADBE",
            "symbol": "ADBE",
            "type": "Common Stock",
        },
        {
            "description": "ADEIA INC",
            "displaySymbol": "ADEA",
            "symbol": "ADEA",
            "type": "Common Stock",
        },
        {
            "description": "AUTOMATIC DATA PROCESSING",
            "displaySymbol": "ADP",
            "symbol": "ADP",
            "type": "Common Stock",
        },
        {
            "description": "ACCENTURE PLC",
            "displaySymbol": "ACN",
            "symbol": "ACN",
            "type": "Common Stock",
        },
        {
            "description": "ALTO INGREDIENTS, INC.",
            "displaySymbol": "ALTO",
            "symbol": "ALTO",
            "type": "Common Stock",
        },
        {
            "description": "Meta Platforms Inc",
            "displaySymbol": "META",
            "symbol": "META",
            "type": "Common Stock",
        },
        {
            "description": "Tesla Inc.",
            "displaySymbol": "TSLA",
            "symbol": "TSLA",
            "type": "Common Stock",
        },
        {
            "description": "Cisco Systems Inc",
            "displaySymbol": "CSCO",
            "symbol": "CSCO",
            "type": "Common Stock",
        },
        {
            "description": "Visa Inc",
            "displaySymbol": "V",
            "symbol": "V",
            "type": "Common Stock",
        },
        {
            "description": "Exxon Mobil Corp",
            "displaySymbol": "XOM",
            "symbol": "XOM",
            "type": "Common Stock",
        },
        {
            "description": "JPMorgan Chase Co",
            "displaySymbol": "JPM",
            "symbol": "JPM",
            "type": "Common Stock",
        },
        {
            "description": "Walmart Inc",
            "displaySymbol": "WMT",
            "symbol": "WMT",
            "type": "Common Stock",
        },
        {
            "description": "Mastercard Inc",
            "displaySymbol": "MA",
            "symbol": "MA",
            "type": "Common Stock",
        },
        {
            "description": "Oracle Corp",
            "displaySymbol": "ORCL",
            "symbol": "ORCL",
            "type": "Common Stock",
        },
        {
            "description": "Coca-Cola Co",
            "displaySymbol": "KO",
            "symbol": "KO",
            "type": "Common Stock",
        },
        {
            "description": "Pfizer Inc",
            "displaySymbol": "PFE",
            "symbol": "PFE",
            "type": "Common Stock",
        },
    ],
}
