def search_by_ip(logs, ip):
    """Mencari log berdasarkan alamat IP."""
    return [
        log for log in logs
        if log["ip_address"] == ip
    ]


def filter_failed(logs):
    """Menampilkan aktivitas login yang gagal."""
    return [
        log for log in logs
        if log["event"] == "LOGIN"
        and log["status"] == "FAILED"
    ]


def detect_suspicious(logs, threshold=3):
    """Mendeteksi IP dengan login gagal berulang."""
    failed_counts = {}

    for log in filter_failed(logs):
        ip = log["ip_address"]
        failed_counts[ip] = failed_counts.get(ip, 0) + 1

    return {
        ip: count
        for ip, count in failed_counts.items()
        if count >= threshold
    }


def get_statistics(logs):
    """Menghitung statistik aktivitas keamanan."""

    unique_ips = {
        log["ip_address"] for log in logs
    }

    unique_users = {
        log["username"] for log in logs
    }

    return {
        "total_logs": len(logs),
        "unique_ips": len(unique_ips),
        "unique_users": len(unique_users),
        "successful_logins": sum(
            1 for log in logs
            if log["event"] == "LOGIN"
            and log["status"] == "SUCCESS"
        ),
        "failed_logins": len(filter_failed(logs)),
        "suspicious_ips": detect_suspicious(logs)
    }