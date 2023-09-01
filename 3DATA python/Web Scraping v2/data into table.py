from bs4 import BeautifulSoup
import pandas as pd

with open("index2.html", "r") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

table = soup.findAll("div", {"class": "calendar-single"})

df = pd.read_html(data)
df = pd.DataFrame(df[0])
print(df)
