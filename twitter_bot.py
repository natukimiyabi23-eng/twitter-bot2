import feedparser
import requests
import time

RSS_URL = "https://rsshub.rssforever.com/twitter/user/nototan_"
WEBHOOK_URL = "https://discord.com/api/webhooks/1487849417963999244/vTMSJxVxroYNc_VWWneRcuROvFfE-cyQyhfK6oqHMKYnmkKnoAkFwXnWzXyKDk90mcGM"

sent = set()

while True:
    feed = feedparser.parse(RSS_URL)

    for entry in feed.entries:
        if entry.link not in sent:
            data = {
                "content": f"📢 新しい投稿！\n{entry.link}"
            }
            requests.post(WEBHOOK_URL, json=data)
            sent.add(entry.link)

    time.sleep(60)
