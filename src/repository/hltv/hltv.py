import requests
from bs4 import BeautifulSoup


class HLTV:
    def get_players(self, url = 'https://www.hltv.org/team/9215/mibr'):
        content = requests.get(url)
        data = BeautifulSoup(content.text, 'html.parser')
        names = data.find_all(class_ = 'text-ellipsis bold')
        players = [name.getText() for name in names]
        return players