import urllib2, json, base64
accesstoken = "UM0P9S650YRJ9PD0G6QQ"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institutions.json"
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken + ":").replace('\n', '')
	)
response = urllib2.urlopen(request)
data = json.load(response)
for c in data:
	print c['UKPRN'],c['Name']
