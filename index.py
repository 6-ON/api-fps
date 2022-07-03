from fetching import fetcher
from flask import Flask, request

app = Flask(__name__)

# Default route returns randonm player
@app.route("/")
def home():
    return fetcher.get_random_player()

#-------------------------------------------------------
# This route returns a list of players based on the filtering params 
@app.route("/players")
def players():
    ALL_VALUE = "all"
    count = request.args.get(key="count", default=10,type=int)
    id_country = request.args.get(key="countryId", default=ALL_VALUE)
    id_continent = request.args.get(key="continentId", default=ALL_VALUE)
    id_tournament = request.args.get(key="tournamentId", default=ALL_VALUE)

    return fetcher.get_players(
        count=count,
        country_id=id_country,
        continent_id=id_continent,
        tournament_id=id_tournament,
    )


#-------------------------------------------------------
# This route returns a list of Teams based on the filtering params 
@app.route("/teams")
def teams():
    ALL_VALUE = "all"
    count = request.args.get(key="count", default=10,type=int)
    id_country = request.args.get(key="countryId", default=ALL_VALUE)
    id_continent = request.args.get(key="continentId", default=ALL_VALUE)
    id_tournament = request.args.get(key="tournamentId", default=ALL_VALUE)

    return fetcher.get_teams(
        count=count,
        country_id=id_country,
        continent_id=id_continent,
        tournament_id=id_tournament,
    )

#-------------------------------------------------------
# This route returns a list of national Teams based on the filtering params 
@app.route("/teams/national")
def nationalteams():
    ALL_VALUE = "all"
    count = request.args.get(key="count", default=10,type=int)
    id_continent = request.args.get(key="continentId", default=ALL_VALUE)
    id_tournament = request.args.get(key="tournamentId", default=ALL_VALUE)

    return fetcher.get_national_teams(
        count=count,
        continent_id=id_continent,
        tournament_id=id_tournament,
    )



#-------------------------------------------------------
# This route returns a list of all available countries
# NOTE: you can use thier ids to filter  players or teams
@app.route("/countries")
def countries():
    return fetcher.get_countries()

#-------------------------------------------------------

#  This route returns a list of all available countries based on the searching term
#  NOTE: you can you thier ids to filter the players or teams
@app.route("/countries/search")
def search_countries():
    term = request.args.get(key="term", default="",type=str)
    return fetcher.get_countries(term)

#-------------------------------------------------------
# this route returns a list of all available continents
# NOTE: you can use thier ids to filter players or teams
@app.route("/continents")
def continents():
    return fetcher.get_continents()

#-------------------------------------------------------

#  This route returns a list of all available continents based on the searching term
#  NOTE: you can you thier ids to filter the players or teams
@app.route("/continents/search")
def search_continents():
    term = request.args.get(key="term", default="",type=str)
    return fetcher.get_continents(term)
#-------------------------------------------------------
# this route returns a list of all available tournaments
# NOTE: you can use thier ids to filter players or teams
@app.route("/tournaments")
def tournaments():
    return fetcher.get_tournaments()

#-------------------------------------------------------

#  This route returns a list of all available continents based on the searching term
#  NOTE: you can you thier ids to filter the players or teams
@app.route("/tournaments/search")
def search_continents():
    term = request.args.get(key="term", default="",type=str)
    return fetcher.get_tournaments(term)
