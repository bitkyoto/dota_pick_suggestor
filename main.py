import requests
import pprint
from bs4 import BeautifulSoup as bs

import psycopg2

# host = "127.0.0.1"
# user = "postgres"
# password = "89215565545max"
# db_name = "postgres"
enemyTeam = ["Axe", "Dawnbreaker", "Invoker", "Vengeful Spirit", "Nature's Prophet"]
myTeam = ["Treant Protector", "Pangolier", "Omniknight", "Night Stalker"]
totalScore = dict()
# for i in range(5):
#     enemyTeam[i] = input(f"Имя {i+1} героя противника")
# for i in range(5):
#     myTeam[i] = input(f"Имя {i+1} героя союзника")
carryHeroes = ["Faceless Void",
               "Sven",
               "Naga Siren",
               "Monkey King",
               "Bloodseeker",
               "Drow Ranger",
               "Slark",
               "Phantom Assassin",
               "Morphling",
               "Phantom Lancer",
               "Troll Warlord"
               ]
urls = ["https://dota2protracker.com/hero/Faceless%20Void#",
        "https://dota2protracker.com/hero/Sven#",
        "https://dota2protracker.com/hero/Gyrocopter#",
        "https://dota2protracker.com/hero/Naga%20Siren#",
        "https://dota2protracker.com/hero/Monkey%20King#",
        "https://dota2protracker.com/hero/Bloodseeker#",
        "https://dota2protracker.com/hero/Drow%20Ranger#",
        "https://dota2protracker.com/hero/Slark#",
        "https://dota2protracker.com/hero/Phantom%20Assassin#",
        "https://dota2protracker.com/hero/Morphling#",
        "https://dota2protracker.com/hero/Phantom%20Lancer#",
        "https://dota2protracker.com/hero/Troll%20Warlord#"
        ]


def updateStats(heroNames, heroWinrates, gameAmmount):
    stringStats = []
    for i in range(len(heroNames)):
        # x = gameAmmount[i*2].getText().split('\n')[2].replace(" ","").split("-")
        # y = [int(i.replace('(', "").replace(')',"")) for i in x]
        # x2 = gameAmmount[i * 2+1].getText().split('\n')[2].replace(" ", "").split("-")
        # y2 = [int(i.replace('(', "").replace(')', "")) for i in x2]
        stringStats.append(f"{heroNames[i].a['title']} {float(heroWinrates[i * 2].get('data-order'))} {float(heroWinrates[i * 2 + 1].get('data-order'))}\n")

    with open(f"heroes/{name}.txt", 'w+') as f:
        for string in stringStats:
            f.write(string)
    return stringStats


def calculateScore(name, enemyTeam, myTeam):
    with open(f"heroes/{name}.txt", 'r') as f:
        score = 0
        for line in f:
            for enemy in enemyTeam:
                if line.find(enemy) != -1:
                    score += float("0." +line.split('.')[2])
                    #print(enemy, float("0." +line.split('.')[2]))
            for teammate in myTeam:
                if line.find(teammate) != -1:
                    score += float("0." + line.split('.')[1].replace(' 0', ''))
                    #print(teammate, float("0." + line.split('.')[1].replace(' 0', '')))

    return score


for carry in carryHeroes:
    totalScore[carry] = 0


for url in urls:
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    name = url.split("/")[4].replace('#', "").replace("%20", " ")
    heroNames = soup.find_all('td', class_='td-hero-pic')
    heroWinrates = soup.find_all('td', class_='td-record')
    gameAmmount = soup.find_all('div', class_='perc-wr')
    stats = [[0 for k in range(5)] for j in range(123)]
    #updateStats(heroNames, heroWinrates,gameAmmount)
    totalScore[name] = calculateScore(name, enemyTeam, myTeam)
    # heroNames = soup.find_all('td', class_='td-hero-pic')
    # heroWinrates = soup.find_all('td', class_='td-record')
    # gameAmmount = soup.find_all('div', class_='perc-wr')
    # score = 0
    # print(f"Статистика по герою {name}")
    # for i in range(len(heroNames)):
    #     if heroNames[i].a['title'] in enemyTeam:
    #         print(
    #             f"Винрейт против {heroNames[i].a['title']} составляет {float(heroWinrates[i * 2 + 1].get('data-order'))}")
    #         score += float(heroWinrates[i * 2 + 1].get('data-order'))
    #     if heroNames[i].a['title'] in myTeam:
    #         print(f"Винрейт c {heroNames[i].a['title']} составляет {float(heroWinrates[i * 2].get('data-order'))}")
    #         score += float(heroWinrates[i * 2].get('data-order'))
    # totalScore[name] = score
    # print("#########################################################")

totalScore = sorted(totalScore.items(), key=lambda x: x[1], reverse=1)
pprint.pprint(totalScore)

# try:
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT version();"
#         )
#         print(f"Server version: {cursor.fetchone()}")
#     with connection.cursor() as cursor:
#         # cursor.execute(
#         #     """CREATE TABLE users """
#         # )
#         pass
# except Exception as ex:
#     print(ex)
