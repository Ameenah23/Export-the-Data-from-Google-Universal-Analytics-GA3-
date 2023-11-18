# Importing Data from a Pandas to a PostgreSQL using SQLAlchemy
This script shows how to send and write table (data) from Pandas DataFrame to PostgreSQL using SQLAlchemy by two methods.

- The first method: create database, schema, table and write df.to_sql.
- The second method: if database and schema are created, we should select them firstly. Then create a table as the desired format or write dataframe directly to postgreSQL using SQAlchemy.

Steps To Follow:
- Create Connection
- Create Cursor
- Actual SQL
- Commit
- Close Connection

