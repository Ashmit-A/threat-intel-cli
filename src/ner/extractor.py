import re

MALWARE_KEYWORDS = [
    "emotet",
    "trickbot",
    "wannacry",
    "ransomware",
    "spyware",
    "trojan",
    "keylogger",
    "botnet",
    "cryptominer",
]

def extract_entities(text):

    cve_pattern = r"CVE-\d{4}-\d+"
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    # domain_pattern = r"\b[a-zA-Z0-9.-]+\.(com|net|org|io)\b"
    domain_pattern = r"\b(?:[a-zA-Z0-9-]+\.)+(?:com|net|org|io)\b"

    cves = re.findall(cve_pattern, text)

    ips = re.findall(ip_pattern, text)

    domains = re.findall(domain_pattern, text)

    malware = [
        m for m in MALWARE_KEYWORDS
        if m in text.lower()
    ]

    return {
        "cves": cves,
        "malware": malware,
        "ips": ips,
        "domains": domains
    }