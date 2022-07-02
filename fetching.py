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
    NOTE: 
    """

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
        DATA_URL = (
            "https://www.footballtransfers.com/en/players/actions/overview/overview"
        )
        payload = {
            "orderBy": "ft_most_valuable_players.estimated_value",
            "orderByDescending": int(desc),
            "page": page,
            "pages": 6988,
            "pageItems": count,
            "continentId": continent_id,
            "countryId": country_id,
            "tournamentId": tournament_id,
        }
        res = requests.post(url=DATA_URL, data=payload)
        return {"results":res.json()["records"]}

    """"
        this methos to srarch for countries by name
    """

    def search_countries(name):
        DATA_URL = (
            "https://www.footballtransfers.com/en/players/actions/overview/countries"
        )

        def fetch_page(page: int) -> dict:
            res = requests.get(url=DATA_URL, params={"term": name, "page": page})
            return res.json()

        return fetcher.fetch_all_pages(fetching_method=fetch_page)

    def get_all_countries():
        DATA_URL = (
            "https://www.footballtransfers.com/en/players/actions/overview/countries"
        )

        def fetch_page(page: int) -> dict:
            res = requests.get(url=DATA_URL, params={"page": page})
            return res.json()

        return fetcher.fetch_all_pages(fetching_method=fetch_page)

    """ this method fetch the all the pages with diferent fectching methods """

    def fetch_all_pages(page_index=1, fetching_method=None):
        results = list()
        while True:
            response_json = fetching_method(page_index)
            more = response_json["pagination"]["more"]
            results += response_json["results"]
            if not (more):
                break
            page_index += 1
        
        return {"results":results}

    def get_random_player():
        return fetcher.get_players_list(page=randint(1, 100), count=1)[0]
