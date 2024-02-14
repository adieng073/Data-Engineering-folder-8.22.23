import requests 
import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

database_password = "2003"

connection = create_server_connection("localhost", "atd", database_password)


url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?limit=1000&active=true"
get = requests.get(url)
player_dfs = []

if get.status_code == 200:
    nfl_data = get.json()
    data_Frame = pd.DataFrame(nfl_data)
    data_Frame.rename(columns={"items" : "player_links"}, inplace= True)
    for x in data_Frame.player_links:
        get_Player_Data = requests.get(x['$ref'])
        player_Data = get_Player_Data.json()
        player_df = pd.DataFrame([player_Data])
        player_dfs.append(player_df)
        # Concatenate all player DataFrames into a single DataFrame
        final_df = pd.concat(player_dfs, ignore_index=True)

        output_csv = pd.read_csv('output.csv')

    # Drop the "$ref" column
        output_csv = output_csv.drop("$ref", axis=1)
        output_csv = output_csv.drop("id", axis=1)
        output_csv = output_csv.drop("uid", axis=1)
        output_csv = output_csv.drop("guid", axis=1)
        output_csv = output_csv.drop("alterids", axis=1)

    # Save the modified DataFrame back to the CSV file
        output_csv.to_csv('output.csv', index=False)
        
        
        new_csv = output_csv["fullName","weight","height","age","birthPlace","college"].copy()
    
        
        
    

      
  
    
else:
    print(f"err: failed to pull inital data. status_code: {get.status_code}")



