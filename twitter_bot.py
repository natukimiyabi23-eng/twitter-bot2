import feedparser
import requests
import time

RSS_URL = "https://rsshub.rssforever.com/twitter/user/nototan_"
WEBHOOK_URL = "https://discord.com/api/webhooks/1487849417963999244/vTMSJxVxroYNc_VWWneRcuROvFfE-cyQyhfK6oqHMKYnmkKnoAkFwXnWzXyKDk90mcGM"

sent = set()

print("BOT STARTED", flush=True)

while True:
    try:
        print("checking...", flush=True)

        feed = feedparser.parse(RSS_URL)
        print("entries:", len(feed.entries), flush=True)

        for entry in feed.entries:
            link = getattr(entry, "link", "")
            title = getattr(entry, "title", "")

            if link and link not in sent:
                print("sending:", link, flush=True)

                data = {
                    "content": f"📢 新しい投稿！\n{title}\n{link}"
                }
                r = requests.post(WEBHOOK_URL, json=data)
                print("discord:", r.status_code, flush=True)

                sent.add(link)

        time.sleep(60)

    except Exception as e:
        print("ERROR:", e, flush=True)
        time.sleep(60)
