import requests
from bs4 import BeautifulSoup


class HLTV:
    def get_players(self, url = 'https://www.hltv.org/team/9215/mibr'):
        content = requests.get(url)
        data = BeautifulSoup(content.text, 'html.parser')
        raw_players = data.find_all(class_ = 'text-ellipsis bold')
        players = [name.getText() for name in raw_players]
        return players

    def get_team_stats(self, url = 'https://www.hltv.org/team/9215/mibr'):
        content = requests.get(url)
        data = BeautifulSoup(content.text, 'html.parser')
        raw_team_stats = data.find_all(class_=['profile-team-stat'])
        team_stats = []
        for stats in raw_team_stats:
            parse_stats_to_content = stats.contents
            team_stats.append([parse_stats_to_content[0].text, parse_stats_to_content[1].text])
        return team_stats