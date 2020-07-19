from bs4 import BeautifulSoup
import requests

def scrape_beer(base):
    """
    Get the link of the individual beers on the chart.
    """

    base_url = 'https://www.beeradvocate.com'
    url = base_url + base

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    table = soup.find('table')
    rows = [row for row in table.find_all('tr')]

    link_beer = []
    for row in rows[1:]:
        items = row.find_all('td')

        link = items[1].find('a')['href']
        link_beer.append(link)

    return link_beer


def get_beer_dict(base):
    """
    Get the information of the beer.
    """

    base_url = 'https://www.beeradvocate.com'
    url = base_url + base

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    headers = ['Type', 'ABV', 'Rank', 'Average Rating', 'Reviews', '# of Ratings', 'Brewery', 'State',
               'Availability', 'Want', 'Got', 'Name']

    brew_name = soup.find(class_='titleBar').find('h1').next_element
    beer_page = soup.find(class_='beerstats')
    new_beers = [one.text for one in beer_page.find_all('dd')] + [brew_name]
    beer_dict_new = dict(zip(headers, new_beers))

    return beer_dict_new


def get_brewery_name(brewery):
    """
    Get the link of the brewery of that beer.
    """
    base_url = 'https://www.beeradvocate.com'
    url = base_url + brewery

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    brew_page = soup.find(class_='beerstats')
    brew_link = brew_page.find_all('dd')[6].find('a')['href']
    return brew_link


def brewery_stats(brew):
    """
    Get the number of beers the brewery makes.
    """
    base_url = 'https://www.beeradvocate.com'
    url = base_url + brew

    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")

    brew_num = soup.find(id="item_stats").find_all('dd')[1].text
    return brew_num