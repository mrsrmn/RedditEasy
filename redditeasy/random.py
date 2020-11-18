import requests
import json
import random
import datetime
from .reddit import Reddit


class Random:
    def __init__(self, sub):
        self.subreddit = sub

    def get_title(self):
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        return meme["data"]["children"][random.randint(1, 25)]["data"]["title"]

    def get_image(self):
        """
        :return: (str) The image URL of a random post
        """

        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        return meme["data"]["children"][random.randint(1, 25)]["data"]["url_overridden_by_dest"]

    def get_post(self):
        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)
        time = meme["data"]["children"][randompost]["data"]["created"] / 1000.0

        return Reddit(
            time=meme["data"]["children"][randompost]["data"]["created"] / 1000.0,
            image_link=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
            title=meme["data"]["children"][randompost]["data"]["title"],
            upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
            total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
            score=meme["data"]["children"][randompost]["data"]["score"],
            downvotes=meme["data"]["children"][randompost]["data"]["downs"],
            updated=datetime.datetime.fromtimestamp(time).strftime("%d-%m-%Y %I:%M:%S UTC"),
            nsfw=meme["data"]["children"][randompost]["data"]["over_18"],
            pinned=meme["data"]["children"][randompost]["data"]["pinned"]
        )
