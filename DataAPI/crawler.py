import requests
from bs4 import BeautifulSoup

URL = "http://www.bb-team.org/trenirovki/exercises/"
BEGGINER = '?experience=747'
INTERMEDIATE = '?experience=748'
ADVANCED = '?experience=749'
URL_EXERCISES = 'http://www.bb-team.org/exercise'


def get_html(url):
    return requests.get(url).text


def get_muscle_groups():
    soup = BeautifulSoup(get_html(URL))

    muscle_groups = {link.get("href"): link.text
                     for link in soup.find_all("a")
                     if link.get("href") is not None
                     and link.get("href").startswith(URL)
                     and not link.text.startswith('Упражнения')}
    return muscle_groups


def get_beginners_exercises():
    muscle_groups = get_muscle_groups()
    begginer_dict = {}
    for link, name in muscle_groups.items():
        soup = BeautifulSoup(get_html(link + BEGGINER))
        exercises = [link.get("title") for link in soup.find_all("a")
                     if link.get("href") is not None
                     and link.get("title") is not None
                     and link.get("href").startswith(URL_EXERCISES)]
        begginer_dict[name] = exercises
    return begginer_dict


def get_intermediate_exercises():
    muscle_groups = get_muscle_groups()
    intermediate_dict = {}
    for link, name in muscle_groups.items():
        soup = BeautifulSoup(get_html(link + INTERMEDIATE))
        exercises = [link.get("title") for link in soup.find_all("a")
                     if link.get("href") is not None
                     and link.get("title") is not None
                     and link.get("href").startswith(URL_EXERCISES)]
        intermediate_dict[name] = exercises
    return intermediate_dict


def get_advanced_exercises():
    muscle_groups = get_muscle_groups()
    advanced_dict = {}
    for link, name in muscle_groups.items():
        soup = BeautifulSoup(get_html(link + ADVANCED))
        exercises = [link.get("title") for link in soup.find_all("a")
                     if link.get("href") is not None
                     and link.get("title") is not None
                     and link.get("href").startswith(URL_EXERCISES)]
        advanced_dict[name] = exercises
    return advanced_dict
