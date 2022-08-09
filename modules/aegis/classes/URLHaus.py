class URLHaus:
    """Stores AbuseIPDB Detection information"""
    def __init__(self,url,threat,detection):
        self.url = url
        self.threat = threat
        self.detection = detection
