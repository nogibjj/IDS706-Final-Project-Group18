# IDS706-Final-Project-Group18
This is final project for ids 706, which builds web microservice that has an API with Swagger Documentation that performs a query using sqlite3 and returns the following information to the user.

Dataset can be download from here [dataset source](https://www.kaggle.com/datasets/theakhilb/layoffs-data-2022)

## Team member
Chen Bian

Kaiyuan Li

Zheng Zhang

Jiankai Xu

## our API with Swagger documentation
```
GET / Initialize the database
GET /query/searchAll Search all
GET /query/searchIndustry Search top 10 industry with most laid off 
GET /query/searchLocation Search top 10 location with most laid off
GET /query/searchIPO  Search the top3 company in every industry where has done the IPO
GET /query/searchCountry?Country=xxx Search the top 10 companies with the most laid offs by given specific country 
GET /query/searchPortion Search the top 10 companies with the highest portion of layoffs
```

