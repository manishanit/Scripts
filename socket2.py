import urllib
from BeautifulSoup import *
url = input('Enter-')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
no = soup('span')
sum1 = 0
for nos in no:
    sum1 = sum1+int(nos.text)
print(sum1)
