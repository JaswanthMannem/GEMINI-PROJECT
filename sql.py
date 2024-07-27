from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai
import sqlite3

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_model(question,prompt):
    model=genai.GenerativeModel("google-pro")
    response=model.generate_content([question,prompt])
    return response

def connect_sqlite(query,db):
    connection=sqlite3.connect(db)
    cnx=connection.cursor()
    cnx.execute(query)
    rows=cnx.fetchall()
    for row in rows:
        print(row)

prompt=[
    """
    You are an expert in converting the english text into SQL query code!
    The SQL database has the name STUDENT with  three columns named name, class and section.
    For example 
    Example 1 : Get me the total number of records in the table?
    The sql command be like SELECT COUNT(*) FROM STUDENT;
    Example 2: Get me the name of the student who class is GenAI?
    The sql command be like SELECT * FROM STUDENT WHERE CLASS="GenAI";
    also the sql code should not have ''' in the beginning or end and sql word in output 

    """
]

