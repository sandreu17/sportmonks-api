from fastapi import FastAPI
import requests

app = FastAPI()

# Clave de autenticación
SPORTMONKS_API_KEY = "c5Axt3Jxa4GRd82UUbHLIjhE4xeqQMinHdceCUaBos6rjessx40YHc50RXQk"
BASE_URL = "https://api.sportmonks.com/v3/football"

def fetch_data(endpoint, params=None):
    """ Función genérica para hacer llamadas a Sportmonks con autenticación. """
    if params is None:
        params = {}
    
    # Agregar API Key automáticamente
    params["api_token"] = SPORTMONKS_API_KEY
    url = f"{BASE_URL}{endpoint}"
    
    response = requests.get(url, params=params)
    return response.json()

# Obtener lista de ligas disponibles
@app.get("/get_leagues/")
def get_leagues():
    return {
        "info": "Lista de Ligas Disponibles",
        "data": fetch_data("/leagues")
    }

# Obtener temporadas disponibles
@app.get("/get_seasons/")
def get_seasons():
    return {
        "info": "Lista de Temporadas",
        "data": fetch_data("/seasons")
    }

# Obtener partidos disponibles en una temporada específica
@app.get("/get_fixtures_by_season/")
def get_fixtures_by_season(season_id: int):
    return {
        "info": f"Fixtures para la temporada {season_id}",
        "data": fetch_data(f"/fixtures/seasons/{season_id}")
    }

# Obtener fixtures por fecha
@app.get("/get_fixture/")
def get_fixture(match_date: str):
    return {
        "info": f"Fixtures en la fecha {match_date}",
        "data": fetch_data(f"/fixtures/date/{match_date}")
    }
