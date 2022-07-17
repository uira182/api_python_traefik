from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

store = {
    'demo': 'this is important data!'
}

@app.get('/')
def read_keys():
    return store

@app.post('/')
def create_key(key: str, value: str):
    store[key] = value
    return {key: store[key]}