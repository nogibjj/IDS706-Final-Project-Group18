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

# Initialize the database
@app.get(path="/", summary='init the datavase', description='Initialize the database using given csv file', tags=['Init'])
async def root():
    init_db()
    return {"message": "Database initialized"}

# Search all
@app.get(path='/query/searchAll', summary='search all', description='Search all of the information', tags=['Search'])
async def search_all():
    search_result = query_search_all()
    return search_result


@app.get(path="/query/searchIndustry", summary='search industry', description='Search top 10 industry with most laid offs', tags=['Search'])
async def search_industry():
    search_result = query_search_industry()
    return search_result


@app.get(path="/query/searchLocation", summary='search location', description='Search top 10 location with most laid offs', tags=['Search'])
async def search_location():
    search_result = query_search_location()
    return search_result


@app.get(path="/query/searchIPO", summary='search IPO', description='Search the top 3 companies which has done the IPO', tags=['Search'])
async def search_IPO():
    search_result = query_search_IPO()
    return search_result

@app.get(path="/query/searchCountry", summary='search country', description='Given specific country, search the top 10 companies with the most laid offs', tags=['Search'])
async def search_country(country: str = "United States"):
    search_result = query_search_country(country)
    return search_result

@app.get(path="/query/searchPortion", summary='search portion', description='Search the top 10 companies with the highest portion of layoffs', tags=['Search'])
async def search_portion():
    search_result = query_search_portion()
    return search_result

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
