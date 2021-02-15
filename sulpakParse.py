from bs4 import BeautifulSoup
import requests

def save():
    with open('sulpak_indo.txt', 'a') as file:
        file.write(f"{comp['title']} -> Price: {comp['price']} -> Link^ {comp['link']}\n")

def parse():
    URL = 'https://www.sulpak.kg/f/noutbuki'
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }
    
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'goods-tiles')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('h3', class_ = 'title').get_text(strip = True),
            'price': item.find('div', class_ = 'price').get_text(strip = True),
            'link': URL + item.find('div', class_ = 'product-container-right-side').find('a').get('href'),
        })

        global comp
        for comp in comps:
            print(f"{comp['title']} -> Price: {comp['price']} -> Link^ {comp['link']}")
            save()

parse()