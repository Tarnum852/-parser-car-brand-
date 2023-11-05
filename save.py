import requests,time
def save(url,x):
    headers = {"Accept": "*/*",
               "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    req = requests.get(url=url, headers=headers)

    scr = req.content
    with open(f'all_cards\{x}.png', 'wb') as file:
        file.write(scr)
if __name__=='__main__':
    url='https://z.mil.ru/images/gorbachuk-02.06.2022-932.jpg'
    save(url,'карточка','1')