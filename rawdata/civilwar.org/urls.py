"""Get list of battle URLs for all Civil War Battles at civilwar.org

I could not find a page or JSON file with the fill list of links to the URLs
of battle summaries. The website uses AJAX and pagination, with a "See More"
revealing more battles. The URL for this is like
https://www.civilwar.org/learn/battles?field_war_tid%5B%5D=1&page=1,
where the ``field_war_tid`` parameter provides the ID for the war
(Civil War, War of 1812, or Revolutionary War).  I look through page
numbers until no battles are found.

"""
import re
import requests
from bs4 import BeautifulSoup


def get_page(page=1):
    r = requests.get(f'https://www.civilwar.org/learn/battles?field_war_tid%5B%5D=1&page={page}')
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.content, "lxml")
    content = soup.find("div", {"class": "view-content"})
    for div in content.find_all("div", {"class": "panel-pane pane-node-title"}):
        link = div.find("a", {'href': re.compile("/learn/civil-war/battles/")})
        if link:
            yield link['href']


def get_all_battles():
    # Set this to a large number - it will break the loop on failure anyways
    MAX_PAGE = 100
    battles = []
    for i in range(1, MAX_PAGE + 1):
        try:
            battles += list(get_page(i))
        except AttributeError:
            break
    return battles
