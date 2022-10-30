from bs4 import BeautifulSoup
import requests

def main(db, cursor):
    endpoints = ["790", "790/p2"]
    query = ("truncate blockedpunts")
    cursor.execute(query, multi=True)
    page = 1
    index = 0
    for endpoint in endpoints:
        url = f"https://www.ncaa.com/stats/football/fbs/current/team/{endpoint}"
        req = requests.get(url)
        text = req.text

        parser = BeautifulSoup(text, 'html.parser')
        teamToAdd = []
        print(f"Getting team info Page {page}..")
        teams = parser.find_all('tr')
        teams.pop(0)
        page += 1

        for team in teams:
            for stats in team:
                teamToAdd.append(stats.text.strip())
            while("" in teamToAdd):
                teamToAdd.remove("")
            if teamToAdd[0] == '-':
                add_record = ("INSERT INTO blockedpunts "
                "(ranking, team, games, punts, blocks) "
                "VALUES (%s, %s, %s, %s, %s)")
                record_data = (index, teamToAdd[1], teamToAdd[2], teamToAdd[3], teamToAdd[4])
                cursor.execute(add_record, record_data)
                db.commit()
            else:
                index = teamToAdd[0]
                add_record = ("INSERT INTO blockedpunts "
                "(ranking, team, games, punts, blocks) "
                "VALUES (%s, %s, %s, %s, %s)")
                record_data = (index, teamToAdd[1], teamToAdd[2], teamToAdd[3], teamToAdd[4])
                cursor.execute(add_record, record_data)
                db.commit()
            teamToAdd.clear()