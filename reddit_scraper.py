# reddit_scraper.py
import os
import praw
from dotenv import load_dotenv

load_dotenv()

def get_user_data(username):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    user = reddit.redditor(username)
    data = {"comments": [], "posts": []}

    try:
        for comment in user.comments.new(limit=100):
            data["comments"].append({
                "body": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}"
            })

        for post in user.submissions.new(limit=100):
            data["posts"].append({
                "title": post.title,
                "body": post.selftext,
                "permalink": f"https://www.reddit.com{post.permalink}"
            })

    except Exception as e:
        print(f"Error fetching data: {e}")

    return data
