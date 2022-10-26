import os
from bs4 import BeautifulSoup
import requests


def main(args1):
    teamsInOrder = []
    index = 1
    url = f"https://www.ncaa.com/stats/football/fbs/current/team/{args1}"
    req = requests.get(url)
    text = req.text

    parser = BeautifulSoup(text, 'html.parser')
    title = parser.find(class_="stats-header__lower__title")
    teamsInOrder.append(title.text)

    print(f"Starting to scrape stats for {title.text}")

    url = f"https://www.ncaa.com/stats/football/fbs/current/team/{args1}"
    req = requests.get(url)
    text = req.text

    parser = BeautifulSoup(text, 'html.parser')
    teams = parser.find_all(class_="school")
    for team in teams:
        x = f"{index}: {team.text}"
        teamsInOrder.append(x)
        index += 1

    url2 = f"https://www.ncaa.com/stats/football/fbs/current/team/{args1}/p2"
    req2 = requests.get(url2)
    text2 = req2.text

    parser2 = BeautifulSoup(text2, 'html.parser')
    teams2 = parser2.find_all(class_="school")
    for team2 in teams2:
        x = f"{index}: {team2.text}"
        teamsInOrder.append(x)
        index += 1

    url3 = f"https://www.ncaa.com/stats/football/fbs/current/team/{args1}/p3"
    req3 = requests.get(url3)
    text3 = req3.text

    parser3 = BeautifulSoup(text3, 'html.parser')
    teams3 = parser3.find_all(class_="school")
    for team3 in teams3:
        x = f"{index}: {team3.text}"
        teamsInOrder.append(x)
        index += 1
    return teamsInOrder