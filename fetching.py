"""
    CREATED BY : AMINE HATIM AKA 6-ON 
    GITHUB : https://github.com/6-ON 
    
    fetching is a library helps to get football players information and filter them based thier contintnents ,countries ,
    and the tournements where they playing
    
    NOTE : i created this library for testing and educational purposes 
    
    NOTE : i'm not responsible for any illegal or commercial usage 

"""


from random import randint
import requests


class fetcher:
    """
    fetcher class is the main class in fetching module
    """

    COUNTRIES_URL = (
        "https://www.footballtransfers.com/en/players/actions/overview/countries"
    )
    PLAYERS_URL = (
        "https://www.footballtransfers.com/en/players/actions/overview/overview"
    )
    CONTINENTS_URL = (
        "https://www.footballtransfers.com/en/players/actions/overview/continents"
    )
    TOURNEMENTS_URL = (
        "https://www.footballtransfers.com/en/tournaments/actions/search"
    )
    TEAMS_URL = (
        "https://www.footballtransfers.com/en/teams/actions/overview/overview"
    )
    def __request_post__(
        _url,
        _page,
        _count,
        _continent_id,
        _country_id,
        _tournament_id,
        _order_by,
        _desc,
    ):
        payload = {
            "orderBy": _order_by,
            "orderByDescending": int(_desc),
            "page": _page,
            "pages": 6988,
            "pageItems": _count,
            "continentId": _continent_id,
            "countryId": _country_id,
            "tournamentId": _tournament_id,
        }
        res = requests.post(url=_url, data=payload)
        return {"results": res.json()["records"]}

    def get_players_list(
        page=1,
        count=10,
        continent_id="all",
        country_id="all",
        tournament_id="all",
        desc=True,
    ):
        """
        this Method fetch the players from the url that contains them as json list
        NOTE:
        the list of players has a key named records
        """
        ORDER_BY = "ft_most_valuable_players.estimated_value"
        return fetcher.__request_post__(
            fetcher.PLAYERS_URL,
            page,
            count,
            continent_id,
            country_id,
            tournament_id,
            ORDER_BY,
            desc,
        )

    def get_countries(term=""):
        """this method to fetch countries by name"""
        return fetcher.__fetch_all_pages__(
            term, fetcher.COUNTRIES_URL, fetcher.__fetch_page_by_term__
        )

    def __fetch_page_by_term__(term: str, page: int, data_url: str) -> dict:
        """this Method fetch page based on filtring params"""
        res = requests.get(url=data_url, params={"term": term, "page": page})
        return res.json()

    def __fetch_all_pages__(TERM: str, DATA_URL: str, fetching_method):
        """this method fetch the all the pages with diferent fectching methods"""
        results = list()
        page_index = 1
        while True:
            response_json = fetching_method(TERM, page_index, DATA_URL)
            more = response_json["pagination"]["more"]
            results += response_json["results"]
            if not (more):
                break
            page_index += 1

        return {"results": results}

    def get_random_player():
        return fetcher.get_players_list(page=randint(1, 100), count=1)[0]

    def get_continents(term=""):
        """this Method fetch continents by name"""
        return fetcher.__fetch_all_pages__(
            term, fetcher.CONTINENTS_URL, fetcher.__fetch_page_by_term__
        )

    def get_tournaments(term=""):
        return fetcher.__fetch_all_pages__(
            term, fetcher.TOURNEMENTS_URL, fetcher.__fetch_page_by_term__
        )

    def get_teams(
        page=1,
        count=10,
        continent_id="all",
        country_id="all",
        tournament_id="all",
        desc=True,
    ):
        ORDER_BY = "total_current_player_value"
        return fetcher.__request_post__(
            fetcher.TEAMS_URL,
            page,
            count,
            continent_id,
            country_id,
            tournament_id,
            ORDER_BY,
            desc,
        )


# testlines
# print(fetcher.get_players_list(count=4, continent_id=1))
# print(fetcher.get_countries())
# print(fetcher.get_continents())
# print(fetcher.get_teams())
