import requests
import pprint
from bs4 import BeautifulSoup as bs
from functions import *
import psycopg2

enemyTeam = ["Axe", "Dawnbreaker", "Invoker", "Vengeful Spirit", "Nature's Prophet"]
myTeam = ["Treant Protector", "Pangolier", "Omniknight", "Night Stalker"]
totalScore = dict()
# for i in range(5):
#     enemyTeam[i] = input(f"Имя {i+1} героя противника")
# for i in range(5):
#     myTeam[i] = input(f"Имя {i+1} героя союзника")

for carry in carryHeroes:
    totalScore[carry] = calculateScore(carry, enemyTeam, myTeam)
# updateStats(urls, heroNames, heroWinrates,gameAmmount)
totalScore = sorted(totalScore.items(), key=lambda x: x[1], reverse=1)
pprint.pprint(totalScore)


