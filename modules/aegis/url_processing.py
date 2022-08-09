from urlextract import URLExtract
import dns
import dns.resolver
import iocextract
import tld
from tld import get_tld


def extract_url(url):
    """Extracts URL from text"""
    if URLExtract().has_urls(url_check(url)) is True:
        return URLExtract().find_urls(url_check(url))
    elif URLExtract().has_urls(url_check(url)) is False:
        return


def extract_domain(url):
    """Extracts Domain from text"""
    domain_name = []
    try:
        domain_name = get_tld(url, as_object=True, fix_protocol=True).fld
    except tld.exceptions.TldDomainNotFound:
        print("FLD Not Found/Is IP")
    except tld.exceptions.TldBadUrl:
        print("Bad URL")
    return domain_name


def url_check(url):
    """Validates and fix invalid URL"""
    # checks first 8 character of the URL string
    if url[0:7] == "https://":
        # appends https if not found
        url = url[7:]
        return url
    elif url[0:6] == "http://":
        url = url[6:]
        return url
    else:
        # returns untouched url if contains http(s)
        return url


def v4_dns(url):
    """Validates URL DNS"""
    v4 = []
    try:
        v4 = dns.resolver.resolve(url, 'A')
    except dns.exception.Timeout:
        print("DNS Query Timed Out")
    except dns.resolver.NoAnswer:
        print("DNS Record No Answer")
    except dns.resolver.NXDOMAIN:
        print("NXDOMAIN")
    return v4


def v4_regex(url):
    "Extract IPv4 Addresses from text"
    v4 = []
    for i in iocextract.extract_ipv4s(url):
        v4.append(i)
    return v4


def get_v4_list(url):
    """Returns all IPv4 from text"""
    v4 = []
    for index, i in enumerate(extract_url(url)):
        for i in (v4_dns(extract_url(url)[index])):
            v4.append(i)
    v4.extend(v4_regex(url))
    return v4
