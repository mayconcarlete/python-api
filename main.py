# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return {
#         'message': 'Hello World'
#     }

# app.run()


from bs4 import BeautifulSoup
import requests

response = requests.get( 'https://www.hltv.org/team/9215/mibr')

soup = BeautifulSoup(response.text, 'html.parser')

# names = soup.find_all(class_=['bodyshot-team g-grid']).find_all(class_=['col-custom'])
names = soup.select('div.bodyshot-team.g-grid')

names2 = names[0].find_all(class_=['col-custom'])
# names2 = names[0].select('href')
print(names2)


# for name in names:
#     split = name.contents
#     print(split[0].text, split[1].getText())


# print(names)
# print(names[0].getText()) 

# players = []
# for name in names:
#     players.append(name.getText())

# print(players)

# from src.repository.hltv.hltv import HLTV

# hltv = HLTV()

# players = hltv.get_players()
# print(players)

# team_stats = hltv.get_team_stats()
# print(team_stats)