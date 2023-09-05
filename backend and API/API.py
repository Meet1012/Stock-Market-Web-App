from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import detaildata,searchdata,fetchdata,fetchquote

app = FastAPI()
origins = [
    # "http://192.168.1.5",
    # "https://192.168.1.5",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stock/profile2")
def get_profile(symbol: str):
    return detaildata[symbol]


@app.get("/quote")
def get_qoute(symbol:str):
    return fetchquote(symbol)


@app.get("/search")
def search():
    return searchdata


@app.get("/stock/candle")
def get_candle(symbol: str = "", resolution: int = 0, fromm: int = 1, to: int = 10):
    return fetchdata(symbol)
