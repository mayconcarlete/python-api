# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return {
#         'message': 'Hello World'
#     }

# app.run()


# from bs4 import BeautifulSoup
# import requests

# response = requests.get( 'https://www.hltv.org/team/9215/mibr')

# soup = BeautifulSoup(response.text, 'html.parser')

# names = soup.find_all(class_="text-ellipsis bold")

# # print(names)
# # print(names[0].getText()) 

# players = []
# for name in names:
#     players.append(name.getText())

# print(players)

from src.repository.hltv.hltv import HLTV

hltv = HLTV()

players = hltv.get_players()

print(players)