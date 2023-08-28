


#SQL related dependancies to import the data
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas as pd
import psycopg2
#Flask related dependencies
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

# open connection to database using posgress


# Create a base class for declarating class definitions to produce Table objects
Base = declarative_base()


#funtion used to call and import the sql db being used for the project
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='Project_3',
                            user='postgres',
                            password='postgres')
    return conn

#################################################
# Flask Routes
#################################################

def index():
   conn = get_db_connection()
   cur = conn.cursor()
   cur.execute('SELECT * FROM "Final_Obesity_Covid_data";')
   data0 = cur.fetchall()
   cur.execute('SELECT * FROM "Income_data_and_obesity_data";')
   data1 = cur.fetchall()
   cur.execute('SELECT * FROM "PovertyByState_clean1_data";')
   data2 = cur.fetchall()
   cur.execute('SELECT * FROM "TotalAccessbydistance_obesity_clean1_data";')
   data3 = cur.fetchall()
   data0=pd.DataFrame.from_dict(data0)
   cur.close()
   conn.close()

   #convert downloading tables into dataframes
   data0=pd.DataFrame.from_dict(data0)
   data1=pd.DataFrame.from_dict(data1)
   data2=pd.DataFrame.from_dict(data2)
   data3=pd.DataFrame.from_dict(data3)
   data_all=data0
   #merge all dataframes together for ease of access
   
   data_all=data_all.merge(data1, how="right",on=0)
   data_all=data_all.merge(data2, how="right",on=0)
   data_all=data_all.merge(data3, how="right",on=0)
   data_all=data_all.rename(columns=[])
   return jsonify(data_all)
    # return render_template('index_.html', data = data)



# Below are the lines of coded we are using to represent the data. Our data is being subdivided in two categories, health and economy.
# The home or main page will have a drop down menu to allow for a zoomed in version of the data at a per state level but for the sake of 
# our analysis, we can to represent all the data at the same time in our to tell our data driven story with all the states being present.

app = Flask(__name__)

@app.route('/')
def home():
   data=index()
   return data

@app.route('/economy')
def economy():
   return render_template('economy.html')

@app.route('/health')
def covid():
   return render_template('covid.html')



if __name__ == '__main__':
   app.run(port=5000, debug=True)

    