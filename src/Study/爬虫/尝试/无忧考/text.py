# encoding:utf-8
import requests
from bs4 import BeautifulSoup


def par(url, headers):
    res = requests.get(url, headers).content
    soup = BeautifulSoup(res, 'lxml')
    soup1 = soup.find('div', class_='content-txt')
    res = soup1.find_all('p')
    for resu in res:
        a = resu.text
        with open('result1.txt', 'a', encoding='utf-8') as f:
            f.write(a + '\n')


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'cookie': '__cfduid=d29b0a8f1dd4be75a547ac499a36368a41590048749; Hm_lvt_f4ae163e87a012d4ab5106f993decb4c=1590048755,1590049857',
        'referer': 'https://www.51test.net/show/9752780.html'
    }
    url = 'https://www.51test.net/show/9752780.html'
    par(url, headers)


if __name__ == '__main__':
    main()
