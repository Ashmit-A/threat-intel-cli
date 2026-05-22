def classify_threat(features):

    if features["num_cves"] > 0 and features["num_malware"] > 0:
        return "Critical"

    elif features["num_cves"] > 0:
        return "High"

    elif features["num_malware"] > 0:
        return "Medium"

    return "Low"