class AbuseIPDB:
    """Stores AbuseIPDB Detection information"""
    def __init__(self,domain,ip,abuse_confidence,country,total_reports,ip_type,detection):
        self.domain = domain
        self.ip = ip
        self.abuse_confidence = abuse_confidence
        self.country = country
        self.total_reports = total_reports
        self.ip_type = ip_type
        self.detection = detection
