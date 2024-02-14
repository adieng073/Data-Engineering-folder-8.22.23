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

create_server_connection("localhost", "root", "2003")


def analyze_position_group(csv_file, position_prompt, avg_weight_prompt):
    rams_pd = pd.read_csv(csv_file)
    rams_pd.rename(columns={"fullname": "Name", "years pro": "years_pro"}, inplace=True)

    position_Query = rams_pd.query(f'position == "{position_prompt}"')
    rows_num = position_Query.shape[0]

    avg_weight = input(avg_weight_prompt)
    try:
        avg_weight = float(avg_weight)
    except ValueError:
        print("Please enter a valid number for the average weight.")

    below_avg = position_Query[position_Query["weight"] < avg_weight]
    if below_avg.empty:
        print(f"0.0% are under the league's avg weight for their position group\n")
    else:
        print(f"\nHere are the players below average weight\n{below_avg}")
        below_percent = format((below_avg.shape[0] / rows_num) * 100)
        print(f"{below_percent}% are under the league's avg weight for their position group\n")

    above_avg = position_Query[position_Query["weight"] >= avg_weight]
    if above_avg.empty:
        print(f"0.0% are at or above the league's avg weight for their position group\n")
    else:
        print(f"Here are the players at or above average weight\n{above_avg}")
        above_percent = format((above_avg.shape[0] / rows_num) * 100)
        print(f"{above_percent}% are at or above the league's avg weight for their position group\n")
        

    
    
csv_file = "rams.csv"
position_prompt = input("Type a position group to get info on all in that group: ")
avg_weight_prompt = "What is the current avg weight this year at this position group?: "

analyze_position_group(csv_file, position_prompt, avg_weight_prompt)
