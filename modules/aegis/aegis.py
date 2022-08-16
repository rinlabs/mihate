import os
import json
import requests
from .url_processing import extract_url, get_v4_list, extract_domain
from .classes.urlhaus import URLHaus
from .classes.hyperphish import Hyperphish
from .classes.abuse_ipdb import AbuseIPDB


class Aegis:
    """Scans text for malicious links and IP"""
    def __init__(self, url):
        self.url = extract_url(url)
        self.urlhaus = self.query_urlhaus(url)
        self.hyperphish = self.query_hyperphish(url)
        self.abuseipdb = self.query_abuseipdb(url)
        self.threat_value = self.get_threat_value()

    def query_hyperphish(self, url):
        """Scans message with hyperphish"""
        hyperphish_array = []
        # fetch hyperphish domain list
        url_list = json.loads(requests.get(
            "https://api.hyperphish.com/gimme-domains").text)
        # checks if the message contains URLs
        extracted_url = extract_url(url)
        for i in extracted_url:
            fld = extract_domain(i)
            if fld in url_list:
                hyperphish_array.append(Hyperphish(i, 1))
        return hyperphish_array

    def query_urlhaus(self, url):
        """Scans message with URLHaus"""
        urlhaus_array = []
        for i in extract_url(url):
            # Construct the HTTP request
            data = {'url': extract_url(i)}
            response = requests.post(
                'https://urlhaus-api.abuse.ch/v1/url/', data)
            # Parse the response from the API
            json_response = response.json()
            if json_response['query_status'] == 'ok':
                # print(json.dumps(json_response, indent=4, sort_keys=False))
                url_json = json_response['url']
                threat = json_response['threat']
                detection = 1
                urlhaus_array.append(URLHaus(url_json, threat, detection))
        return urlhaus_array

    def query_abuseipdb(self, url):
        """Scans message with AbuseIPDB"""
        abuseipdb_array = []
        # defining AbuseIPDB endpoint
        endpoint = 'https://api.abuseipdb.com/api/v2/check'
        ##print(get_v4_list(url))
        for i in get_v4_list(url):
            # constructs query parameters
            query_string = {
                'ipAddress': i,
                'maxAgeInDays': '90'
            }
            headers = {
                'Accept': 'application/json',
                'Key': os.getenv('ABUSEIPDB_KEY')
            }
            response = requests.request(
                method='GET', url=endpoint, headers=headers, params=query_string).json()
            ##print(response)
            if int(response['data']['totalReports']) > 0:
                domain = response['data']['domain']
                ip = response['data']['ipAddress']
                abuse_confidence = response['data']['abuseConfidenceScore']
                country = response['data']['countryCode']
                total_reports = response['data']['totalReports']
                ip_type = response['data']['usageType']
                detection = 1
                abuseipdb_array.append(AbuseIPDB(
                    domain, ip, abuse_confidence, country, total_reports, ip_type, detection))
        return abuseipdb_array

    def get_threat_value(self):
        """Returns the threat value of the message"""
        urlhaus_threat_val = 0
        hyperphish_threat_val = 0
        abuseipdb_threat_val = 0

        print(self.abuseipdb[0].detection)

        # sums all detected value in array hyperphishArray
        for index,i in enumerate(self.hyperphish):
            hyperphish_threat_val += self.hyperphish[index].detection

        # sums all detected value in array URLHausArray
        for index,i in enumerate(self.urlhaus):
            urlhaus_threat_val += self.urlhaus[index].detection

        for index,i in enumerate(self.abuseipdb):
            abuseipdb_threat_val += self.abuseipdb[index].detection

        return urlhaus_threat_val + hyperphish_threat_val + abuseipdb_threat_val
