import uvicorn
if __name__ == "__main__":
    uvicorn.run("API:app", port=8001, reload=True)