import os
from sys import getallocatedblocks
from bs4 import BeautifulSoup
import requests
import time
import get3rdDownConvPercent
import get3rdDownConvPercDefense
import get4thDownConvPercent
import get4thDownConvPercDefense
import getBlockedKicks
import getBlockedKicksAllowed
import getBlockedPunts
import getBlockedPuntsAllowed
import getCompletionPercentage
import getDefensiveTouchdowns
import getFewestPenalties
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv('PASSWORD')

HOST = "localhost"  
PORT=3306
USERNAME = "root"
PASSWORD = DB_PASSWORD
DATABASE = "cfb_team_stats"


db = mysql.connector.connect(
      host=HOST,
      port=PORT,
      user=USERNAME,
      password=PASSWORD,
      database=DATABASE
)

cursor = db.cursor(buffered=True)

queries = [
get3rdDownConvPercent,
get3rdDownConvPercDefense,
get4thDownConvPercDefense,
get4thDownConvPercent,
getBlockedKicks,
getBlockedKicksAllowed,
getBlockedPunts, getBlockedPuntsAllowed,
getCompletionPercentage,
getDefensiveTouchdowns,
getFewestPenalties
]

for query in queries:
    print(f"Getting {query}")
    query.main(db, cursor)
    time.sleep(1)
print("Closing Database Connection")
cursor.close()
db.close()