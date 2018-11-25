"""
Project results of the current matchup
"""

import os
import sys
from authentication import Authenticator
from downloader import Downloader
from parser import Parser 
from team import Team
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Immediately launches OAuth2 protocol
    oauth = Authenticator()
    client = oauth.client
    league_id = '36697'
    league_key = 'nba.l.' + league_id
    downloader = Downloader(client, league_key)
    parser = Parser()

    stats_mapping  = {
            '5':'FG%',
            '8':'FT%',
            '10':'3PTM',
            '12':'PTS',
            '15':'REB',
            '16':'AST',
            '17':'ST',
            '18':'BLK',
            '19':'TO',
        }

    stat_dict = {}

    for stat in stats_mapping.keys():
        stat_dict[stat] = {}

    weeks = range(1,5)
    teams = []

    for id in range(1, 15):
        teams.append(Team(id))

    for team in teams:
        for stat in stats_mapping.keys():
            stat_dict[stat][team.id] = list()

        for week in weeks:
            response = downloader.get_stats(team.id, week)
            week_stats = parser.parse_stats(response, team, week)
            for stat in stats_mapping.keys():
                stat_dict[stat][team.id].append(week_stats[stat])

    for stat in stats_mapping.keys():
        for team in teams:
            plt.plot(weeks,stat_dict[stat][team.id], label=team.name)

        plt.ylabel(stats_mapping[stat])
        plt.xlabel('week')
        plt.legend(prop={'size': 6})
        plt.show()






