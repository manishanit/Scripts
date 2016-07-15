import urllib
import xml.etree.ElementTree as ET

url = input('Enter the url')
html = urllib.urlopen(url).read()
root = ET.fromstring(html)
counts = root.findall('.//count')
sum1 = 0
for count in counts:
    sum1=sum1+int(count.text)
print(sum1)
