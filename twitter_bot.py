import feedparser
import requests
import time

RSS_URL = "https://rsshub.rssforever.com/twitter/user/nototan_"
WEBHOOK_URL = "https://discord.com/api/webhooks/1487849417963999244/vTMSJxVxroYNc_VWWneRcuROvFfE-cyQyhfK6oqHMKYnmkKnoAkFwXnWzXyKDk90mcGM"

sent = set()

print("BOT STARTED")

while True:
    print("checking...")

    feed = feedparser.parse(RSS_URL)
    print("entries:", len(feed.entries))

    for entry in feed.entries:
        if entry.link not in sent:
            print("sending:", entry.link)

            data = {
                "content": f"📢 新しい投稿！\n{entry.link}"
            }
            r = requests.post(WEBHOOK_URL, json=data)
            print("discord:", r.status_code)

            sent.add(entry.link)

    time.sleep(60)
