import praw
import json
from datetime import datetime
import time

# Reddit API bilgilerini gir
reddit = praw.Reddit(
    client_id="JfAGFScl6ll0ujW3gp3HWQ",
    client_secret="4gpDvRbe57rYQsxo1HFXVOZ2m-AXlg",
    user_agent="mycarapp by /u/Sensitive_Ad9047"
)


subreddits = [
    "MechanicAdvice", 
    "Cartalk", 
    "AskMechanics", 
    "AutoRepair", 
    "Automotive", 
    "CarHelp", 
    "Justrolledintotheshop", 
    "CarProblems",
    "Autos", 
    "CarMaintenance", 
    "DIYauto", 
    "CarRepair",
    "CarTalk",
    "Mechanic", 
    "FixIt", 
    "AutoMechanics"
]


json_data = []
count = 0  

for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"▶ Subreddit: {subreddit_name} üzerinden veri çekiliyor...")

    for post in subreddit.hot(limit=100000):
        if not post.stickied and not post.is_self:
            continue

        data = {
            "title": post.title,
            "content": post.selftext,
            "date": datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d'),
            "comments": []
        }

        try:
            post.comments.replace_more(limit=0)
            for comment in post.comments:
                data["comments"].append(comment.body)
        except:
            pass  

        json_data.append(data)
        count += 1

        if count % 100 == 0:
            print(f"✔ {count} veri toplandı...")

        time.sleep(1)

    for post in subreddit.new(limit=100000):
        if not post.stickied and not post.is_self:
            continue

        data = {
            "title": post.title,
            "content": post.selftext,
            "date": datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d'),
            "comments": []
        }

        try:
            post.comments.replace_more(limit=0)
            for comment in post.comments:
                data["comments"].append(comment.body)
        except:
            pass

        json_data.append(data)
        count += 1

        if count % 100 == 0:
            print(f"✔ {count} veri toplandı...")

        time.sleep(1)

with open("reddit_ariza_verisi_100000.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f"🎉 Tamamlandı! Toplam {count} veri JSON formatında kaydedildi.")
