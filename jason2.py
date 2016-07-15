import urllib
import simplejson as json

url = input('Enter a url')
html = urllib.urlopen(url).read()

info = json.loads(html)
sum1 = 0
for x in info["comments"]:
    sum1 = sum1+ int(x["count"])

print(sum1)
