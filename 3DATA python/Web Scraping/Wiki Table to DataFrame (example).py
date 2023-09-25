import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Characters_in_the_Animal_Crossing_series"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})
#  table = soup.find("table", {"id": "the_id"})

df = pd.read_html(str(table))
df = pd.DataFrame(df[0])
print(df)

