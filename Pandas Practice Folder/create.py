import pandas as pd
import mysql.connector 
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

create_server_connection("localhost", "root", "2003", "rams_roster")


def read(file):
    df = pd.read_csv(file)
    dfRename = df.rename(columns={"fullname": "name", "school":"college"})
    print(dfRename)
    
    
csv = "rams.csv"
print(read(csv))
