import urllib
from BeautifulSoup import *
url = "http://python-data.dr-chuck.net/known_by_Alieshah.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = 1
while count<=7:
    count1 = 1
    for tag in tags:
        if count1 == 18:
            new_url = tag.get('href')
            break
        count1=count1+1
    html1 = urllib.urlopen(new_url).read()
    soup1 = BeautifulSoup(html1)
    tags = soup1('a')
    count=count+1
print(tag.text)
        
