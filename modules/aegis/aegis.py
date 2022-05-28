import os
import requests
import json
from modules.aegis.urlProcessing import extractUrl, getv4List
from modules.aegis.classes.URLHaus import URLHaus
from modules.aegis.classes.hyperphish import Hyperphish
from modules.aegis.classes.abuseIPDB import AbuseIPDB


class aegis:
    def __init__(self, url):
        self.url = extractUrl(url)
        self.URLHaus = self.queryURLHaus(url)
        self.hyperphish = self.queryHyperphish(url)
        self.abuseipdb = self.queryAbuseIPDB(url)
        self.threatValue = self.getThreatValue()

    def queryURLHaus(self, url):
        URLHausArray = []
        for i in extractUrl(url):
            # Construct the HTTP request
            data = {'url': extractUrl(i)}
            response = requests.post(
                'https://urlhaus-api.abuse.ch/v1/url/', data)
            # Parse the response from the API
            json_response = response.json()
            if json_response['query_status'] == 'ok':
                # print(json.dumps(json_response, indent=4, sort_keys=False))
                urlJSON = json_response['url']
                threat = json_response['threat']
                detection = 1
                URLHausArray.append(URLHaus(urlJSON, threat, detection))
        return URLHausArray

    def queryHyperphish(self, url):
        hyperphishArray = []
        # fetch hyperphish domain list
        urlList = json.loads(requests.get(
            "https://api.hyperphish.com/gimme-domains").text)
        # checks if the message contains URLs
        for i in extractUrl(url):
            if (i in urlList):
                hyperphishArray.append(Hyperphish(i, 1))
        return hyperphishArray

    def queryAbuseIPDB(self, url):
        abuseIPDBArray = []
        # defining AbuseIPDB endpoint
        endpoint = 'https://api.abuseipdb.com/api/v2/check'
        print(getv4List(url))
        for i in getv4List(url):
            # constructs query parameters
            queryString = {
                'ipAddress': i,
                'maxAgeInDays': '90'
            }
            headers = {
                'Accept': 'application/json',
                'Key': os.getenv('ABUSEIPDB_KEY')
            }
            response = requests.request(
                method='GET', url=endpoint, headers=headers, params=queryString).json()
            print(response)
            if (int(response['data']['totalReports']) > 0):
                domain = response['data']['domain']
                ip = response['data']['ipAddress']
                abuseConfidence = response['data']['abuseConfidenceScore']
                country = response['data']['countryCode']
                totalReports = response['data']['totalReports']
                ipType = response['data']['usageType']
                detection = 1
                abuseIPDBArray.append(AbuseIPDB(
                    domain, ip, abuseConfidence, country, totalReports, ipType, detection))
        return abuseIPDBArray

    def getThreatValue(self):
        URLHausThreatVal = 0
        HyperphishThreatVal = 0
        AbuseIPDBThreatVal = 0

        # sums all detected value in array URLHausArray
        for index, i in enumerate(self.URLHaus):
            URLHausThreatVal += self.URLHaus[index].detection

        # sums all detected value in array hyperphishArray
        for index, i in enumerate(self.hyperphish):
            HyperphishThreatVal += self.hyperphish[index].detection

        for index, i in enumerate(self.abuseipdb):
            AbuseIPDBThreatVal += self.abuseipdb[index].detection

        return URLHausThreatVal + HyperphishThreatVal + AbuseIPDBThreatVal
