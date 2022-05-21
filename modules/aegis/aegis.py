import sys
import requests
import json
from dotenv import load_dotenv
from modules.urlProcessing import *
from modules.aegis.URLHaus import *
from modules.aegis.hyperphish import *

class aegis:
    def __init__(self,url):
        self.url = extractUrl(url)
        self.URLHaus = self.queryURLHaus(url)
        self.hyperphish = self.queryHyperphish(url)
        self.threatValue = self.getThreatValue()

    def queryURLHaus(self,url):
        URLHausArray = []
        for i in extractUrl(url):
            # Construct the HTTP request
            data = {'url' : extractUrl(i)}
            response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data)
            # Parse the response from the API
            json_response = response.json()
            if json_response['query_status'] == 'ok':
                # returns query result
                print(json.dumps(json_response, indent=4, sort_keys=False))
                urlJSON = json_response['url']
                threat = json_response['threat']
                detection = 1
                URLHausArray.append(URLHaus(urlJSON,threat,detection))
        return URLHausArray

    def queryHyperphish(self,url):
        hyperphishArray = []
        urlList = json.loads(requests.get("https://api.hyperphish.com/gimme-domains").text)
        # checks if the message contains URLs
        for i in extractUrl(url):
            if (i in urlList):
                print(1)
                hyperphishArray.append(Hyperphish(i,1))
        return hyperphishArray

    def getThreatValue(self):
        URLHausThreatVal = 0
        HyperphishThreatVal = 0

        for index,i in enumerate(self.URLHaus):
            URLHausThreatVal += self.URLHaus[index].detection

        for index,i in enumerate(self.hyperphish):
            HyperphishThreatVal += self.hyperphish[index].detection

        return URLHausThreatVal + HyperphishThreatVal
