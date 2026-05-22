def build_features(entities):

    features = {
        "num_cves": len(entities["cves"]),
        "num_malware": len(entities["malware"]),
        "num_ips": len(entities["ips"]),
        "num_domains": len(entities["domains"])
    }

    return features