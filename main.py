from fastapi import FastAPI, Query
import requests

app = FastAPI()

SPORTMONKS_API_KEY = "c5Axt3Jxa4GRd82UUbHLIjhE4xeqQMinHdceCUaBos6rjessx40YHc50RXQk"
BASE_URL = "https://api.sportmonks.com/v3/football"

@app.get("/get_league_id/")
def get_league_id(league_name: str):
    url = f"{BASE_URL}/leagues/search/{league_name}"
    params = {"api_token": SPORTMONKS_API_KEY}
    response = requests.get(url, params=params).json()
    
    # ⚠️ Ajustar la respuesta para incluir el campo "info"
    return {
        "info": "League search result",
        "data": response
    }

@app.get("/get_fixture/")
def get_fixture(match_date: str):
    url = f"{BASE_URL}/fixtures/date/{match_date}"
    params = {"api_token": SPORTMONKS_API_KEY}
    response = requests.get(url, params=params).json()
    
    # ⚠️ Ajustar la respuesta para incluir el campo "info"
    return {
        "info": "Fixture data",
        "data": response
    }

