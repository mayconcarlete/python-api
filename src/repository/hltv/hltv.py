import requests
from bs4 import BeautifulSoup


class HLTV:
    def __init__(self, url = 'https://www.hltv.org/team/9215/mibr'):
        self.url = url
        self.data = self.get_raw_data()
        
    def get_raw_data(self):
        content = requests.get(self.url)
        data = BeautifulSoup(content.text, 'html.parser')
        return data
    
    def get_team_name(self):
        raw_team_name = self.data.find_all(class_='profile-team-name')
        team_name = raw_team_name[0].text
        return team_name
        
    def get_players(self, url = 'https://www.hltv.org/team/9215/mibr'):
        raw_players = self.data.find_all(class_ = 'text-ellipsis bold')
        players = [name.getText() for name in raw_players]
        return players

    def get_team_stats(self, url = 'https://www.hltv.org/team/9215/mibr'):
        raw_team_stats = self.data.find_all(class_=['profile-team-stat'])
        team_stats = []
        for stats in raw_team_stats:
            parse_stats_to_content = stats.contents
            team_stats.append([parse_stats_to_content[0].text, parse_stats_to_content[1].text])
        print(team_stats)
        return self.parse_team_stats_dict(team_stats)
    
    def parse_team_stats_dict(self, team_stats):
        team_stats_dict = {}
        for stats in team_stats:
            team_stats_dict[stats[0]] = stats[1]
        return team_stats_dict
