import requests,lxml,save2,test
from bs4 import BeautifulSoup
def geting_imp(url):
    req=requests.get(url=url)
    src=req.content
    soup=BeautifulSoup(src,'lxml')
    all_li=soup.find('ul').find_all('li')
    name_all=[]
    tipe_all=[]
    tag=[]
    for item in all_li:
        a=item.find('a')['href']
        name_all.append(item.find('img').next_element.text)
        a='https://www.carlogos.org/'+a
        print(a)

        tipe_all.append(item.find('label').text)
        x=test.main(a)
        print(x)
        tag.append(x)
    save2.save(name_all,tipe_all,tag)
def main(url):
    geting_imp(url)
if __name__=='__main__':
    url='https://www.carlogos.org/car-brands/page-8.html'
    main(url)