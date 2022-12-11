import sqlite3
import csv


def init_db():
    # Connecting to the database
    connection = sqlite3.connect("layoffs_data.db")

    # Creating a cursor object to execute
    # SQL queries on a database table
    cursor = connection.cursor()

    drop_table = """DROP TABLE IF EXISTS layoffs"""
    cursor.execute(drop_table)

    # Table Definition
    create_table = """CREATE TABLE layoffs(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Company TEXT NOT NULL,
                    Location TEXT,
                    Industry TEXT,
                    Laid_Off_Count INTEGER, 
                    Date DATETIME,
                    Source TEXT,
                    Funds_Raised DECIMAL,
                    Stage TEXT,
                    Date_Added DATETIME,
                    Country TEXT,
                    Percentage DECIMAL,
                    List_of_Employees_Laid_Off TEXT);
                    """

    # Creating the table into our
    # database
    cursor.execute(create_table)

    # Opening the fortune.csv file
    file = open("layoffs_data.csv", encoding="utf-8")

    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)

    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO layoffs (Company,Location,Industry,Laid_Off_Count,Date,Source,Funds_Raised,Stage,Date_Added,Country,Percentage,List_of_Employees_Laid_Off) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    # Importing the contents of the file
    # into our person table
    cursor.executemany(insert_records, contents)

    # Committing the changes
    connection.commit()

    # closing the database connection
    connection.close()



if __name__ == "__main__":
    init_db()