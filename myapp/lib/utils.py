from datetime import datetime


def isoformat_now() -> str:
    dt_utc = datetime.utcnow()
    return dt_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
