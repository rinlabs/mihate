from urlextract import URLExtract
from urllib.parse import urlparse
import dns
import dns.resolver
import re
import iocextract

def extractUrl(url):
    if (URLExtract().has_urls(urlCheck(url)) == True):
            return URLExtract().find_urls(urlCheck(url))
    elif (URLExtract().has_urls(urlCheck(url)) == False):
            return

def urlCheck(url):
    # checks first 8 character of the URL string
    if(url[0:7] == "https://"):
        # appends https if not found
        url=url[7:]
        return url
    elif(url[0:6] == "http://"):
        url=url[6:]
        return url
    else:
        # returns untouched url if contains http(s)
        return url

def v4DNS(url):
    v4 = []
    try:
        v4 = dns.resolver.resolve(url,'A')
    except (dns.exception.Timeout):
        print("DNS Query Timed Out")
    except (dns.resolver.NoAnswer):
        print("DNS Record No Answer")
    except (dns.resolver.NXDOMAIN):
        print("NXDOMAIN")
    return v4

def v4Regex(url):
    v4 = []

    for i in iocextract.extract_ipv4s(url):
        v4.append(i)
    return v4

def getv4List(url):
    v4 = []
    for index,i in enumerate(extractUrl(url)):
        for i in (v4DNS(extractUrl(url)[index])):
            v4.append(i)
    v4.extend(v4Regex(url))
    return v4
