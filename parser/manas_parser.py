from bs4 import BeautifulSoup as bs
import requests

URL = 'http://www.manascinema.com/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}


# connect parsing
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='short_movie_info')
    manas_film = []

    for item in items:
        manas_film.append(
            {
                'title': item.find('div', class_='m_title').get_text(),
                'image': URL + item.find('div', class_='m_thumb').find('img').get('src'),
                'time': item.find('div', class_='m_time').get_text(),
            }
        )

    return manas_film


# finish parsing
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_manas_film = []
        for page in range(0, 1):
            html = get_html(f'http://www.manascinema.com/movies', params=page)
            all_manas_film.extend(get_data(html.text))
        return all_manas_film
    else:
        raise Exception('Ошибка в коде')


if __name__ == "__main__":
    print(parser())