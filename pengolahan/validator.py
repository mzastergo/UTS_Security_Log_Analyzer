from datetime import datetime
from ipaddress import ip_address


def validate_log(log):
    """Memeriksa apakah data log valid."""

    required_fields = {
        "timestamp",
        "ip_address",
        "username",
        "event",
        "status"
    }

    if not required_fields.issubset(log.keys()):
        return False

    if any(not log[field] for field in required_fields):
        return False

    try:
        datetime.strptime(
            log["timestamp"], "%Y-%m-%d %H:%M:%S"
        )
        ip_address(log["ip_address"])
    except (ValueError, TypeError):
        return False

    if log["event"] not in {"LOGIN", "LOGOUT"}:
        return False

    if log["status"] not in {"SUCCESS", "FAILED"}:
        return False

    return True