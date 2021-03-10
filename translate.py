thirukural = {}
import requests

for i in range(1,1331):
    url = 'https://api-thirukkural.vercel.app/api?num='+str(i)
    x = requests.get(url)
    res = x.json()

    temp = {}
    temp['tamil'] = res['tam_exp']
    thirukural[str(res['number'])] = temp

    thirukural[str(i)]['sect_tam'] = res['sect_tam']
    thirukural[str(i)]['sect_eng'] = res['sect_eng']
    thirukural[str(i)]['chap_tam'] = res['chap_tam']
    thirukural[str(i)]['chap_eng'] = res['chap_eng']
    thirukural[str(i)]['line1'] = res['line1']
    thirukural[str(i)]['line2'] = res['line2']
    
  
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'ta',
    'to': ['en', 'hi']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': '', #Key Removed
    'Ocp-Apim-Subscription-Region': '', #Key Removed
    'Content-type': 'application/json'
    
}
for i in range(1,1331):
    # You can pass more than one object in body.
    body = [{
        'text': thirukural[str(i)]['tamil']
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    thirukural[str(i)]['english'] = response[0]['translations'][0]['text']
    thirukural[str(i)]['hindi'] = response[0]['translations'][1]['text']

import json
with open('thirukural_exp.json', 'w') as fp:
    json.dump(thirukural, fp)

