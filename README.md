# IDS706-Final-Project-Group18
This is final project for ids 706, which builds web microservice that has an API with Swagger Documentation that performs a query using sqlite3 and returns the following information to the user.<br>
Specifically, we find an layoff dataset from kaggle and want to get some information such as how many layoffs in the perspective of industry, location and IPO company. Using our web microservice, the user can not only get these information but also able to get the layoff info in any country that the user enter.

Dataset can be download from here [dataset source](https://www.kaggle.com/datasets/theakhilb/layoffs-data-2022)

## Team member
- Chen Bian<br>
- Kaiyuan Li<br>
- Zheng Zhang<br>
- Jiankai Xu<br>

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

## To start with make install
```
make install
```

## How to use the project
```
python main.py
```

In the new web page, add `/docs` to the url and take the advantage of the swagger.
![docs](/home/picture/docs.png)

or 

```
curl -X 'GET' \
  '[Your localhost or other IP address]/query/searchAll' \
  -H 'accept: application/json'
```
for the first GET method in Search. </br>
For example,
```
curl -X 'GET' \
  'https://apple-pie-smile-probable-guacamole-w9g5r5vr9wjc5prp-8080.preview.app.github.dev/query/searchAll' \
  -H 'accept: application/json'
```

The response from 3rd GET method, which is use for querying the search of top 10 location with most laid offs, should look like this:</br>

```
{\n        \"0\": \"SF Bay Area\",\n        \"1\": 79840.0\n    },\n    {\n        \"0\": \"New York City\",\n        \"1\": 21986.0\n    },\n    {\n        \"0\": \"Bengaluru\",\n        \"1\": 17450.0\n    },\n    {\n        \"0\": \"Seattle\",\n        \"1\": 16051.0\n    },\n    {\n        \"0\": \"Boston\",\n        \"1\": 7311.0\n    },\n    {\n        \"0\": \"Sao Paulo\",\n        \"1\": 6637.0\n    },\n    {\n        \"0\": \"Los Angeles\",\n        \"1\": 5743.0\n    },\n    {\n        \"0\": \"Singapore\",\n        \"1\": 5663.0\n    },\n    {\n        \"0\": \"Mumbai\",\n        \"1\": 5525.0\n    },\n    {\n        \"0\": \"Gurugram\",\n        \"1\": 5351.0\n    }
```



which response body is in the form of json.



