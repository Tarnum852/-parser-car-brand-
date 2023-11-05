import requests
from bs4 import BeautifulSoup

def geting_imp(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    req = requests.get(url=url, headers=headers)
    src = req.content
    soup = BeautifulSoup(src, 'lxml')
    all_a = soup.find(class_="byline-left").find_all('a')
    y = []
    for item in all_a:
        y.append(item.text)
    return y  # Возвращаем список имен авторов

def main(url):
    author_list = geting_imp(url)  # Сохраняем возвращаемый список в переменной author_list
    print(author_list)
    return author_list
if __name__ == '__main__':
    url = 'https://www.carlogos.org/car-brands/tesla-logo.html'
    main(url)