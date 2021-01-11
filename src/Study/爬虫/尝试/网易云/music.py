# encoding:utf-8

import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
}
n = 1

while n == 1:
    try:
        url = "http://music.163.com/song/media/outer/url?id=" + input('请输入歌曲id:')
        res = requests.get(url, headers=headers)
        filename = input('输入歌曲名:') + '.mp3'
        with open(filename, "wb") as f:
            f.write(res.content)
        print("successful...")
    except Exception:
        print("无法下载...")

    c = input("是否退出 (y退出):")
    if c == 'y' or c == 'Y':
        break
