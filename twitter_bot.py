import os
import sys
import time
import feedparser
import requests

RSS_URL = "https://rsshub.rssforever.com/twitter/user/nototan_"
WEBHOOK_URL = "https://discord.com/api/webhooks/1487849417963999244/vTMSJxVxroYNc_VWWneRcuROvFfE-cyQyhfK6oqHMKYnmkKnoAkFwXnWzXyKDk90mcGM"

print("BOOT OK", flush=True)
print("Python:", sys.version, flush=True)
print("RSS_URL:", RSS_URL, flush=True)
print("WEBHOOK set:", bool(WEBHOOK_URL), flush=True)

sent = set()

while True:
    try:
        print("loop start", flush=True)

        feed = feedparser.parse(RSS_URL)
        print("feed parsed", flush=True)
        print("entries:", len(feed.entries), flush=True)

        for entry in feed.entries:
            link = getattr(entry, "link", "")
            title = getattr(entry, "title", "")

            if link and link not in sent:
                print("sending:", link, flush=True)
                r = requests.post(
                    WEBHOOK_URL,
                    json={"content": f"📢 新しい投稿！\n{title}\n{link}"},
                    timeout=20
                )
                print("discord status:", r.status_code, flush=True)
                sent.add(link)

        time.sleep(60)

    except Exception as e:
        print("ERROR:", repr(e), flush=True)
        time.sleep(60)
