# encoding:utf-8
import re

text = '<span class="txt"><a href="/song?id=409031374"><b title="Z imt">Zi<div class="soil">E</div>mt</b></a></span>'

# s = re.search('href="/song\?id=(.+?)"', text).group(1)
# s = re.findall('\d+', text)
# print(s[0])

s = re.search('title="(.*?)"', text).group(1)
print(s)