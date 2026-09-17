import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


ACCESS_TOKEN = os.environ["THREADS_ACCESS_TOKEN"]


# 게시할 글
text = "Squawk!"

response = requests.post(
    "https://graph.threads.net/v1.0/me/threads",
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    },
    data={
        "media_type": "TEXT",
        "text": text,
        "auto_publish_text": "true",
    },
    timeout=30,
)

response.raise_for_status()

print("게시 성공")
print(response.json())
