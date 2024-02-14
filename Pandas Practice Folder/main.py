
import pandas as pd
import requests 
import mysql.connector
from mysql.connector import Error

    

#Connect to MySQL server
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

# Pulling of the API
# Link to api: https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c/5e0b844e4d56d0b049747024a04bb7949c2d6c5d#file-extending-espn-api-md
url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?limit=1000&active=true"
get = requests.get(url)

player_data_frames = []
rams_players = []
players_set = set()

if get.status_code == 200:
    nfl_data = get.json()
    data_Frame = pd.DataFrame(nfl_data)
    data_Frame.rename(columns={"items" : "player_links"}, inplace= True)
    
    for x in data_Frame.player_links:
        get_Player_Data = requests.get(x['$ref'])
        player_Data = get_Player_Data.json()
        player_Data_Frame = pd.DataFrame([player_Data])
        player_data_frames.append(player_Data_Frame)
        
        for player_Data_Frame in player_data_frames:
            player_teams_ref = player_Data_Frame["team"].iloc[0]
            get_teams = requests.get(player_teams_ref['$ref'])
            #print(player_teams_ref)
        
        if get_teams.status_code == 200:
                team_data = get_teams.json()
                #print(team_data)
                team_data_frame = pd.DataFrame([team_data])
                #print(team_data_frame)
                team_ref = team_data_frame["displayName"].iloc[0]
                print(team_ref)
                if team_ref == "Los Angeles Rams":
                    player_name = player_Data_Frame["fullName"].iloc[0]
                    #print(player_name)
        else:
            print("failure to pull requested team data")
        
    

            
                        
else:
    print("failure to pull requested data")


