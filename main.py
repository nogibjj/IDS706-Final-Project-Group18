from db import init_db
from fastapi import FastAPI
import uvicorn
from queries import (
    query_search_all,
    query_search_industry,
    query_search_location,
    query_search_IPO,
    query_search_country,
    query_search_portion
)

app = FastAPI()


@app.get("/")
async def root():
    init_db()
    return {"message": "Database initialized"}


@app.get("/query/searchAll")
async def search_all():
    search_result = query_search_all()
    return search_result


@app.get("/query/searchIndustry")
async def search_industry():
    search_result = query_search_industry()
    return search_result


@app.get("/query/searchLocation")
async def search_location():
    search_result = query_search_location()
    return search_result


@app.get("/query/searchIPO")
async def search_IPO():
    search_result = query_search_IPO()
    return search_result

@app.get("/query/searchCountry")
async def search_country(country: str = "United States"):
    search_result = query_search_country(country)
    return search_result

@app.get("/query/searchPortion")
async def search_portion():
    search_result = query_search_portion()
    return search_result

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
