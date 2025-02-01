from fastapi import FastAPI, Query
from pydantic import BaseModel
import requests

app = FastAPI()

SPORTMONKS_API_KEY = "c5Axt3Jxa4GRd82UUbHLIjhE4xeqQMinHdceCUaBos6rjessx40YHc50RXQk"
BASE_URL = "https://api.sportmonks.com/v3/football"

# 📌 Estructura esperada por ChatGPT
class APIResponse(BaseModel):
    info: str
    data: dict

@app.get("/get_league_id/", response_model=APIResponse)
def get_league_id(league_name: str):
    url = f"{BASE_URL}/leagues/search/{league_name}"
    params = {"api_token": SPORTMONKS_API_KEY}
    response = requests.get(url, params=params).json()
    
    return APIResponse(
        info="League search result",
        data=response
    )

@app.get("/get_fixture/", response_model=APIResponse)
def get_fixture(match_date: str):
    url = f"{BASE_URL}/fixtures/date/{match_date}"
    params = {"api_token": SPORTMONKS_API_KEY}
    response = requests.get(url, params=params).json()
    
    return APIResponse(
        info="Fixture data",
        data=response
    )
