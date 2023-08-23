// const basePath = "https://finnhub.io/api/v1"
// const token = "cikjf0pr01qsrf88u96gcikjf0pr01qsrf88u970"
const basePath = "http://localhost:8001"

// // ? Alphavantage
// const basePath = "https://www.alphavantage.co"
const token = "3D3SFNPN2WK7QN1E"

export const searchSymbols = async (query) => {
    const url = `${basePath}/search?q=${query}`;
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    return await response.json();
};

export const fetchStockDetails = async (stockSymbol) => {
    const url = `${basePath}/stock/profile2?symbol=${stockSymbol}`;
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

export const fetchHistoricalData = async(stockSymbol, from, to) => {
    const url = `${basePath}/stock/candle?symbol=${stockSymbol}&from=${from}&to=${to}&token=${token}`;
    const response = await fetch(url);

    if (!response.ok) {
        const message = `An Error has Occured: ${response.status}`;
        throw new Error(message);
    }

    return await response.json();
    
}
