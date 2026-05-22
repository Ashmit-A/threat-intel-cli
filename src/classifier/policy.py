def decide_action(severity, confidence):

    if confidence >= 0.65 and (severity == "Critical" or severity == "High"):
        return "ALERT_IMMEDIATE"

    elif confidence >= 0.50:
        return "ALERT_REVIEW"

    else:
        return "IGNORE"