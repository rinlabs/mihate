class AbuseIPDB:
    def __init__(self,domain,ip,abuseConfidence,country,totalReports,ipType,detection):
        self.domain = domain
        self.ip = ip
        self.abuseConfidence = abuseConfidence
        self.country = country
        self.totalReports = totalReports
        self.ipType = ipType
        self.detection = detection
