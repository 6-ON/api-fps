from fetching import fetcher
from flask import Flask, request

app = Flask(__name__)

""""Default route returns  """
@app.route("/")
def home():
    return fetcher.get_random_player()


""" The route returns a list of players based on the filtering params """
@app.route("/playerlist")
def playerslist():
    ALL_VALUE = "all"
    count = request.args.get(key="count", default=10,type=int)
    id_country = request.args.get(key="countryId", default=ALL_VALUE)
    id_continent = request.args.get(key="continentId", default=ALL_VALUE)
    id_tournament = request.args.get(key="tournamentId", default=ALL_VALUE)

    return fetcher.get_players_list(
        count=count,
        country_id=id_country,
        continent_id=id_continent,
        tournament_id=id_tournament,
    )

""" The route returns a list of all available countries
    NOTE: you can use thier ids to filter the players
"""
@app.route("/countries")
def countries():
    return fetcher.get_all_countries()


""" The route returns a list of all available countries based on the searching term
    NOTE: you can you thier ids to filter the players
"""
@app.route("/countries/search")
def countries():
    term = request.args.get(key="term", default="all",type=str)
    return fetcher.search_countries(term)

