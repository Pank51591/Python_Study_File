import requests
from bs4 import BeautifulSoup
#import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
r = requests.get('https://book.douban.com/subject/1084336/comments\\' , headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')

for item in pattern:
    print(item.string)
'''pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)

for star in p:
    s += int(star)
print(s)'''
