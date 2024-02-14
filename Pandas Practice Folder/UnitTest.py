import unittest
import pandas as pd
import requests

class TestMyCode(unittest.TestCase):

    def test_api_request(self):
        url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?limit=1000&active=true"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_csv_read(self):
        file_path = r"C:\Users\adien\Desktop\Data Engineering folder 8.22.23\Pandas Folder\rams.csv"
        df = pd.read_csv(file_path)
        self.assertIsInstance(df, pd.DataFrame)
        

    

if __name__ == '__main__':
    unittest.main()
