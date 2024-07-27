from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai
import sqlite3

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_model(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

def connect_sqlite(query,db):
    connection=sqlite3.connect(db)
    cnx=connection.cursor()
    cnx.execute(query)
    rows=cnx.fetchall()
    for row in rows:
        if len(row)>1:
            ans=""
            for i in range(len(row)):
                ans=ans+str(row[i])+" "
        else:
            ans=row[0]
        st.info(row)
        st.header(ans)
    connection.commit()
    connection.close()


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

st.set_page_config(page_title="I can retrive any SQL query")
st.header("Gemini App to Retrive SQL Data")
question=st.text_input("Input :",key="input")
submit=st.button("Ask the question")

if submit:
    response=load_model(question,prompt)
    st.info(response)
    st.subheader("The Response is")
    db="student.db"
    connect_sqlite(response,db)
    
