import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Home_video_game_console#List_of_home_video_game_consoles"
table_class = "wikitable sortable jquery-tablesorter"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})

df = pd.read_html(str(table))
df = pd.DataFrame(df[0])
print(df)
