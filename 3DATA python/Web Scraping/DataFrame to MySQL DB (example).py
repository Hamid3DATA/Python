import pandas as pd
import requests
from sqlalchemy import create_engine
from bs4 import BeautifulSoup

# paste in "Wiki Table to DataFrame (example)"

# Credentials to database connection
host_name = "127.0.0.1:3306"
db_name = "consoles"
user_name = "root"
password = "Hamid"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=host_name, db=db_name, user=user_name, pw=password))

# Convert dataframe to sql table
df.to_sql('tablename', engine, index=False)
