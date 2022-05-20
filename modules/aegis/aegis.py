import sys
import requests
import json
from dotenv import load_dotenv
from modules.urlProcessing import *
from modules.aegis.URLHaus import *

class aegis:
    def __init__(self,url):
        self.url = url
        self.URLHaus = self.queryURLHaus(url)
        self.hyperphish = self.queryHyperphish(url)
        self.threatValue = self.hyperphish + self.URLHaus.detection

    def queryURLHaus(self,url):
        # Construct the HTTP request
        data = {'url' : extractUrl(url)}
        response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data)
        # Parse the response from the API
        json_response = response.json()
        if json_response['query_status'] == 'ok':
            # returns query result
            # print(json.dumps(json_response, indent=4, sort_keys=False))
            urlJSON = json_response['url']
            threat = json_response['threat']
            signature = json_response['tags'][3]
            detection = 1
            return URLHaus(urlJSON,threat,signature,detection)
        elif json_response['query_status'] == 'no_results':
            # not found
            return URLHaus("","","",0)
        else:
            # something happened
            return URLHaus("","","",0)

    def queryHyperphish(self,url):
        urlList = json.loads(requests.get("https://api.hyperphish.com/gimme-domains").text)
        # checks if the message contains URLs
        if (extractUrl(urlCheck(url)) in urlList):
            return 1
        else:
            return 0
