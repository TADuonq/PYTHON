import http.client, urllib.request
import urllib.parse, urllib.error
import base64, sys
import simplejson as json

subscription_key = '12f29133caf4406493e81b6a31c47c1a'
  
headers = {'Content-Type': 'application/json',
           'Ocp-Apim-Subscription-Key': subscription_key
           }
  
params = urllib.parse.urlencode({})

url1 = 'IMAGE URL TO BE ADDED HERE'
body = { 'url': url1 }
newbody =str(body)
  
try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, newbody, headers)
    response = conn.getresponse()
    data = response.read()
  
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))

    val = parsed[0]["scores"]
    res = max(val, key = val.get)
    print ("\nEmotion :: ",res)
  
    conn.close()
except Exception as e:
    print(e.args)