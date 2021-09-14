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

print(soup.find(class_="bodyshot-team-bg"))