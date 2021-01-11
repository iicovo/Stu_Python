import requests
import re


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }
    res = requests.get(url, headers)
    text = res.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynaties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    aothers = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    poems = re.findall(r'<div\sclass="contson".*?>(.*?)</div>', text, re.DOTALL)
    poems1 = []
    for poem in poems:
        x = re.sub(r'<.*?>|\n', '', poem)
        poems1.append(x.strip())

    contents = []
    for value in zip(titles, dynaties, aothers, poems1):
        titles, dynaties, aothers, poems = value
        cont = {
            '题目': titles,
            '作者': dynaties + '  ' + aothers,
            '正文': poems,
        }
        contents.append(cont)

    for content in contents:
        fp = open('今日古诗.txt', 'a', encoding='utf-8')
        fp.write(str(content)+'\n\n')
        fp.close()


def main():
    for x in range(1, 11):
        url = 'https://www.gushiwen.org/default_%s.aspx' % x
        parse_page(url)


if __name__ == '__main__':
    main()
