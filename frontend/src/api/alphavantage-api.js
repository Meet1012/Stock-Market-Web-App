// ? Alphavantage
const basePath = "https://www.alphavantage.co"
const token = "3D3SFNPN2WK7QN1E"

function parseTimeSeries(data) {
    let time_series_key = Object.keys(data)[1]
    console.log(data[time_series_key])
    
    return Object.keys(data[time_series_key]).map(e => {
        let t = data[time_series_key][e];
        console.log("==>")
        console.log(t)
        return {
            value: parseFloat(t["4. close"]).toFixed(2),
            date: e,
        }
    })
}

export const searchSymbols = async (query) => {
    const url = `${basePath}/search?q=${query}&token=${token}`;
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    return await response.json();
};

export const fetchStockDetails = async (stockSymbol) => {
    const url = `${basePath}/stock/profile2?symbol=${stockSymbol}&token=${token}`;
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    return await response.json();
};

export const fetchQuote = async (stockSymbol) => {
    const url = `${basePath}/quote?symbol=${stockSymbol}&token=${token}`;
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    return await response.json();
};

export const fetchHistoricalData = async (stockSymbol, filter) => {

    let _function = ""
    switch (filter) {
        case "1D":
            _function = "TIME_SERIES_DAILY_ADJUSTED"
            break;

        case "1W":
            _function = "TIME_SERIES_WEEKLY"
            break;

        default:
            _function = "TIME_SERIES_MONTHLY"
            break;
    }

    
    const url = `${basePath}/query?symbol=${stockSymbol}&function=${_function}&apikey=${token}`;
    console.log(url)
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    let data = await response.json();
    return await parseTimeSeries(data)
}
