import urllib
import simplejson as json

serviceurl="http://python-data.dr-chuck.net/geojson?"

address = input("Enter location:")
url=serviceurl+urllib.urlencode({'sensor':'false','address': address})
print 'Retrieving',url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
try:
    js=json.loads(str(data))
except:
    js=None
if 'status' not in js or js['status']!='OK':
    print('===Failed to retrieve==')
    print(data)
    #continue
#print(json.dumps(js,indent=4))
else:
    place_id = js['results'][0]['place_id']
    print "Place-id",place_id
          
    
