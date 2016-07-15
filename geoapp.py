import urllib
import simplejson as json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'


address = raw_input('Enter location: ')


url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
print json.dumps(js, indent=4)
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print 'lat',lat,'lng',lng
location = js['results'][0]['formatted_address']
print location
