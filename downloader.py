import time

class Downloader():
	""" This class will be performing GET requests from the Yahoo API and will
	be responsible for grabbing the raw XML content from the stat endpoints
	"""

	def __init__(self, client, league_key):
		self.client = client
		self.league_key = league_key

	# Uses client to access Yahoo stats endpoint and returns a Response object
	def get_stats(self, team_id, week_number):
		yahoo_stats_endpoint = (
			"https://fantasysports.yahooapis.com/fantasy/v2/team/"
			+ self.league_key 
			+ ".t." 
			+ str(team_id)
			+ "/stats;type=week;week=" 
			+ str(week_number)
		)
		response = self.client.get(yahoo_stats_endpoint)
		print(response.text)
		return response

	# Gets the start and end dates for each Week of the League
	def get_week_calendar(self):
		yahoo_week_calendar_endpoint = (
			"https://fantasysports.yahooapis.com/fantasy/v2/"
			"game/nba/game_weeks"
		)

		response = self.client.get(yahoo_week_calendar_endpoint)
		return response

def main():
	pass


if __name__ == "__main__":
	main()