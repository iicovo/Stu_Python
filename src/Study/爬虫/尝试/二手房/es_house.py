# encoding:utf-8

import requests
from bs4 import BeautifulSoup


def parse_page(url):
    headers = {
        "Cookie": "select_city=410100; lianjia_ssid=c1b79a92-5a0f-4466-8294-0453b8641e36; lianjia_uuid=a8a1ced0-c70a-4f2a-a348-8a38350b3473; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176ad7cdfe0b37-0154ef2d20252d-c791039-1327104-176ad7cdfe1b8c%22%2C%22%24device_id%22%3A%22176ad7cdfe0b37-0154ef2d20252d-c791039-1327104-176ad7cdfe1b8c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(req.text, "html5lib")
    s = soup.find('div', attrs={"class": "content"})
    house_list = s.find_all('li')[5:]


    for house in house_list:
        title = house.find('div', class_='info clear')
        try:
            house_title = title.find('a').text
            house_position = title.find('div', class_='positionInfo').text
            house_house_contents = title.find('div', class_='houseInfo').text
            house_follow = title.find('div', class_='followInfo').text
            house_price = title.find('div', class_='priceInfo').text


            with open('result.txt', 'a', encoding='utf-8') as f:
                f.write(
                    house_title + '\t' + house_position + '\t' + house_house_contents + '\t' + house_follow + '\t' + house_price + '\n')

        except Exception:
            pass


def main():

    url = 'http://zz.lianjia.com/ershoufang/pg32/'
    parse_page(url)


if __name__ == '__main__':
    main()
