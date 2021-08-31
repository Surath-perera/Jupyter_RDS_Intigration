#Install pyodbc & pandas

!pip install pyodbc
!pip install pandas

#Import libraries 
import pyodbc
import pandas as pd

 

# Define Paramaters

server = '<RDS Endpoint' 
database = '<DB Name>' 
username = 'Username' 
password = 'password'  

#Making the connection with RDS
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+'; DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


# select rows from SQL table to insert in dataframe.
query = "SELECT * FROM <Table Name>>;"
df = pd.read_sql(query, cnxn)
print(df)
