import os
from bs4 import BeautifulSoup
import requests

url = "https://www.ncaa.com/stats/football/fbs/current/team/27"
req = requests.get(url)
text = req.text
# print(text)

parser = BeautifulSoup(text, 'html.parser')
title = parser.find(class_="stats-header__lower__title")
print(title.text)

url = "https://www.ncaa.com/stats/football/fbs/current/team/27"
req = requests.get(url)
text = req.text

parser = BeautifulSoup(text, 'html.parser')
teams = parser.find_all(class_="school")
for team in parser.find_all(class_="school"):
    x = team.text
    print(x)

url2 = "https://www.ncaa.com/stats/football/fbs/current/team/27/p2"
req2 = requests.get(url2)
text2 = req2.text

parser2 = BeautifulSoup(text2, 'html.parser')
teams2 = parser.find_all(class_="school")
for team2 in parser2.find_all(class_="school"):
    x = team2.text
    print(x)

url3 = "https://www.ncaa.com/stats/football/fbs/current/team/27/p3"
req3 = requests.get(url3)
text3 = req3.text

parser3 = BeautifulSoup(text3, 'html.parser')
teams3 = parser3.find_all(class_="school")
for team3 in parser.find_all(class_="school"):
    x = team3.text
    print(x)