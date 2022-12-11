import json
import pandas as pd
import sqlite3

# Connecting to the database
connection = sqlite3.connect("layoffs.db")

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()


def parse_to_json(df):
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)


def query_search_all():
    # get all the data from database
    sql = """
    SELECT * FROM layoffs;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result


def query_search_industry():
    # get all the data from database
    sql = """
    SELECT Industry, sum(Laid_Off_Count) as Total_layoffs
    FROM layoffs
    WHERE Industry != "Unknown"
    group by Industry
    order by sum(Laid_Off_Count) DESC
    LIMIT 10
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result


def query_search_location():
    # get all the data from database
    sql = """
    SELECT Location, sum(Laid_Off_Count) as Total_layoffs
    FROM layoffs
    group by Location
    order by sum(Laid_Off_Count) DESC
    LIMIT 10
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result


def query_search_IPO():
    # get all the data from database
    sql = """
    SELECT Company, Location, Industry, Laid_Off_Count
    FROM(
    SELECT Company, Location, Industry, Laid_Off_Count, rank() over(partition by Industry order by Laid_Off_Count desc) as rnks
    FROM layoffs
    WHERE Stage = "IPO") a1
    WHERE rnks = 1 or rnks = 2 or rnks = 3
    ;
    """

    # executing the SQL query
    cursor.execute(sql)

    # storing the data in a variable using fetchall() method
    alldata = cursor.fetchall()  # a list of tuples
    df = pd.DataFrame(alldata)
    result = parse_to_json(df)
    return result
