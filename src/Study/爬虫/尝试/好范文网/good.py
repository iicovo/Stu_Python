# encoding:utf-8
import requests
from bs4 import BeautifulSoup


def webs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Referer': 'https://www.dogedoge.com/',
    }
    res = requests.get(url, headers).content
    soup = BeautifulSoup(res, 'html5lib')
    a = soup.find('div', class_="content")
    b = a.select('p')
    filename = input('请输入您要保存的文件名:') + '.txt'
    for i in b:
        c = list(i.stripped_strings)
        for d in c:
            fp = open(filename, 'a', encoding='utf-8')
            fp.write(d + '\n')
            fp.close()


def main():
    url = 'http://www.haoword.com/xindetihui/qitaxinde/511538.htm'
    webs(url)


if __name__ == '__main__':
    main()
