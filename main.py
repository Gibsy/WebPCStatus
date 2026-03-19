import time
import json
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

STATUS_FILE = "status.json"
INTERVAL = 180  # You can change this, but 180 seconds is optimal to avoid using the API too frequently
                # In status.js, it marks you as offline if status.json hasn't been updated for 240 seconds
                # You can change that value as well if you want to

start_time = datetime.now(timezone.utc)


def upload_to_neocities(path):
    try:
        with open(path, "rb") as f:
            r = requests.post(
                "https://neocities.org/api/upload",
                headers={"Authorization": f"Bearer {API_KEY}"},
                files={os.path.basename(path): f},
                timeout=10
            )
        return r.status_code == 200
    except Exception as e:
        print("Neocities upload error:", e)
        return False


def update_all():
    now = datetime.now(timezone.utc)

    status = {
        "online": True,
        "last_update": now.isoformat(),
        "online_since": start_time.isoformat()
    }

    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

    upload_to_neocities(STATUS_FILE)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] STATUS uploaded")


if __name__ == "__main__":
    while True:
        update_all()
        time.sleep(INTERVAL)
