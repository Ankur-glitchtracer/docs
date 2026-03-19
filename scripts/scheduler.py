from datetime import datetime, timedelta
from config import REVIEW_INTERVAL

def extract_confidence(conf_str):
    try:
        return int(conf_str.split("/")[0])
    except:
        return 0

def get_interval(conf, impact):
    base = REVIEW_INTERVAL.get(conf, 7)

    if impact.lower() == "high":
        return int(base * 0.8)
    elif impact.lower() == "low":
        return int(base * 1.5)

    return base

def next_review(conf, impact):
    return datetime.now() + timedelta(days=get_interval(conf, impact))

def decay(conf):
    return max(1, conf - 1)
