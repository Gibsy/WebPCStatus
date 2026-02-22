import time
import json
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")                        
SITE = os.getenv("SITE")                              
STATUS_FILE = "status.json"
INTERVAL = 30               # you can change to 60 (1 minute)

start_time = datetime.now(timezone.utc)

def upload_status(online=True):
    now = datetime.now(timezone.utc)
    data = {
        "online": online,
        "last_update": now.isoformat(),
        "online_since": start_time.isoformat()
    }

    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

    with open(STATUS_FILE, "rb") as f:
        files = {"status.json": f}
        headers = {"Authorization": f"Bearer {API_KEY}"}
        r = requests.post("https://neocities.org/api/upload", headers=headers, files=files)
        print(f"[{now}] Uploaded status.json, response code: {r.status_code}")

if __name__ == "__main__":
    while True:
        try:
            upload_status(True)
        except Exception as e:
            print("Error uploading:", e)
        time.sleep(INTERVAL)
