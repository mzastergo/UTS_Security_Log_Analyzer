import csv
import json
from .validator import validate_log


def read_csv(filename):
    """Membaca dan memvalidasi data dari file CSV."""

    logs = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, strict=True)

            required_fields = {
                "timestamp", "ip_address",
                "username", "event", "status"
            }

            if not required_fields.issubset(
                reader.fieldnames or []
            ):
                raise ValueError("Kolom CSV tidak lengkap.")

            for row in reader:
                if validate_log(row):
                    logs.append(row)
                else:
                    print("Peringatan: Data tidak valid:", row)

    except FileNotFoundError:
        print("Error: File tidak ditemukan.")
        return []

    except (csv.Error, ValueError, OSError) as error:
        print("Error:", error)
        return []

    return logs


def save_json(filename, data):
    """Menyimpan hasil pengolahan ke file JSON."""

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except (OSError, TypeError, ValueError) as error:
        print("Error:", error)
        return False