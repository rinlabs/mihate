from urlextract import URLExtract
from urllib.parse import urlparse

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
