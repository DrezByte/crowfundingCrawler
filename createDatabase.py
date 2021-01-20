import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="root", password="root", host="localhost", port="5432", database="test")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE Platforms ( platform_name VARCHAR PRIMARY KEY, agrement TEXT ); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table Platforms created successfully in PostgreSQL ")

    create_table_query = '''CREATE TABLE Promoters ( promoter_name VARCHAR PRIMARY KEY ); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table Promoters created successfully in PostgreSQL ")

    create_table_query = '''CREATE TABLE Projects (
                    project_name VARCHAR PRIMARY KEY,
                    platform_name VARCHAR REFERENCES Platforms(platform_name),
                    promoter_name VARCHAR REFERENCES Promoters(promoter_name),
                    collected_amount INT,
                    amount INT,
                    status VARCHAR NOT NULL,
                    project_link TEXT
                    ); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table Projects created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
