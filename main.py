import requests,lxml,save
from bs4 import BeautifulSoup
def geting_imp(url):
    req=requests.get(url=url)
    src=req.content
    soup=BeautifulSoup(src,'lxml')
    all_li=soup.find('ul').find_all('li')
    x=378
    for item in all_li:
        x+=1
        print(x)
        img_url=item.find("img")["src"]
        img_url=f'https://www.carlogos.org{img_url}'
        save.save(img_url,x)
def main(url):
    geting_imp(url)

if __name__=='__main__':
    url='https://www.carlogos.org/car-brands/page-8.html'
    main(url)