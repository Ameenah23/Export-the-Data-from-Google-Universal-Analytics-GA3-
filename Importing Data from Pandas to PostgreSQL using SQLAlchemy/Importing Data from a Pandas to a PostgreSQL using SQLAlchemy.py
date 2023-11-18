#!/usr/bin/env python
# coding: utf-8

# This script shows how to send and write table (data) from Pandas DataFrame to PostgreSQL using SQLAlchemy by two methods.
# 
# - The first method: create database, schema, table and write df.to_sql.
# - The second method: if database and schema are created, we should select them firstly. Then create a table as the desired format or write dataframe directly to postgreSQL using SQAlchemy.

# #### Steps To Follow:
# 
# 1. Create Connection
#  
# 2. Create Cursor 
#  
# 3. Actual SQL
#  
# 4. Commit
# 
# 5. Close Connection

# In[18]:


# import libraries
import psycopg2
from sqlalchemy import create_engine, text
import sqlalchemy
import configparser

import pandas as pd
from sqlalchemy import *
import os 


# ### Connection using psycopg2


# connect to created db
pgconn = psycopg2.connect(
    host='xxxxxxx',
    user='ameenah_a_202309',
    password='xxxxxx',
    database='xxxxxx')




# required code 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
pgconn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 


# ### Create Database

# drop db
pgcursor.execute('DROP DATABASE IF EXISTS wcd_db')


# create db
pgcursor.execute('CREATE DATABASE wcd_db')



# commit 
pgconn.commit()


# close
pgconn.close()




# ### Select existing Database


# cursor 
pgcursor = pgconn.cursor()


# check using db 
pgcursor.execute('SELECT current_database()')

pgcursor.fetchone()


# ### Create Schema


# drop schema
pgcursor.execute('DROP SCHEMA  IF EXISTS wcd_ga3ua_raw')


# create schema
pgcursor.execute('CREATE SCHEMA IF NOT EXISTS wcd_ga3ua_raw')



# Select SCHEMA
pgcursor.execute('SET search_path TO wcd_ga3ua_raw')


# ### Create the table


# drop table 
pgcursor.execute('DROP TABLE IF EXISTS user_activity')


pgcursor.execute('TRUNCATE TABLE user_activity')



try:
    pgcursor.execute("""CREATE TABLE IF NOT EXISTS user_activity (
                 client_id  FLOAT,
                 sessionId  INT,  
                 deviceCategory  VARCHAR(500), 
                 platform        VARCHAR(500), 
                 dataSource      VARCHAR(500), 
                 sessionDate     DATE, 
                 activityTime    VARCHAR(1000), 
                 source          VARCHAR(500), 
                 medium           VARCHAR(500), 
                 channelGrouping   VARCHAR(500), 
                 campaign          VARCHAR(1000), 
                 keyword           VARCHAR(1000), 
                 hostname          VARCHAR(500),
                 landingPagePath   VARCHAR(1000), 
                 activityType      VARCHAR(500), 
                 customDimension    VARCHAR(500), 
                 pageview_pagePath    VARCHAR(1000), 
                 pageview_pageTitle   VARCHAR(1000), 
                 event_eventCategory  VARCHAR(500), 
                 event_eventAction    VARCHAR(500),
                 event_eventLabel     VARCHAR(500),
                 event_eventCount  FLOAT);""")
except:
    pgcursor.execute("rollback")
    pgcursor.execute("""CREATE TABLE IF NOT EXISTS user_activity (
                 client_id  FLOAT,
                 sessionId  INT,  
                 deviceCategory  VARCHAR(500), 
                 platform        VARCHAR(500), 
                 dataSource      VARCHAR(500), 
                 sessionDate     DATE, 
                 activityTime    VARCHAR(1000), 
                 source          VARCHAR(500), 
                 medium           VARCHAR(500), 
                 channelGrouping   VARCHAR(500), 
                 campaign          VARCHAR(1000), 
                 keyword           VARCHAR(1000), 
                 hostname          VARCHAR(500),
                 landingPagePath   VARCHAR(1000), 
                 activityType      VARCHAR(500), 
                 customDimension    VARCHAR(500), 
                 pageview_pagePath    VARCHAR(1000), 
                 pageview_pageTitle   VARCHAR(1000), 
                 event_eventCategory  VARCHAR(500), 
                 event_eventAction    VARCHAR(500),
                 event_eventLabel     VARCHAR(500),
                 event_eventCount  FLOAT);""")



# commit 
pgconn.commit()



# close
pgconn.close()


# ### Pandas


df1 = pd.read_csv('1-User_Activity_2020_Jan_April.csv')
df1.head(1)


df1.shape


df1.info()


df1.columns


# ## SQLAlchemy


# import 
from sqlalchemy import create_engine


config = configparser.ConfigParser()
config.read('WCD_postgresql.ini')



# Compiling login info
DB_TYPE = config['postgresql']['DB_TYPE']
DB_DRIVER = config['postgresql']['DB_DRIVER']
DB_USER = config['postgresql']['DB_USER']
DB_PASS = config['postgresql']['DB_PASS']
DB_HOST = config['postgresql']['DB_HOST']
DB_PORT = config['postgresql']['DB_PORT']
DB_NAME = config['postgresql']['DB_NAME']



SQLALCHEMY_DATABASE_URI = f'{DB_TYPE}+{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
#SQLALCHEMY_DATABASE_URI = '{0}+{1}://{2}:{3}@{4}:{5}/{6}'.format(DB_TYPE,DB_DRIVER,DB_USER,DB_PASS,DB_HOST,DB_PORT,DB_NAME)

# create engine 
# connection string: dialect+driver://user:password@server/database
engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine = engine.connect()


engine




# into a PostgreSQL table

postgreSQLTable = "user_activity";

try:
    frame = df.to_sql(postgreSQLTable, con=engine, if_exists='replace', schema='wcd_ga3ua_raw', index=False);
except ValueError as vx:
    print(vx)

except Exception as ex:  
    print(ex)
else:
    print("PostgreSQL Table %s has been created successfully."%postgreSQLTable);

finally:
    connection.close();



df2 = pd.read_csv('2-User_Activity_2020_May_Aug.csv')


df2.shape



df2.to_sql('user_activity', engine, schema='wcd_ga3ua_raw', if_exists='append', index=False)






# #### Importing data from a PostgreSQL database to a Pandas DataFrame

# sql to df
import pandas.io.sql as psql
data_df = psql.read_sql_query('SELECT * FROM user_activity', engine)
data_df




engine.close()








