import requests
import json
import random
import datetime


class Random:
    def __init__(self, sub):
        self.subreddit = sub

    def get_title(self):
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        if meme["message"]:
            if meme["message"] == "Too Many Requests":
                raise KeyError("Too many requests. Please wait a little.")
        else:
            return meme["data"]["children"][random.randint(1, 25)]["data"]["title"]

    def get_author(self):
        """
        :return: (str) The name of the author
        """

        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        if meme["message"]:
            if meme["message"] == "Too Many Requests":
                raise KeyError("Too many requests. Please wait a little.")
            else:
                raise KeyError
        else:
            return meme["data"]["children"][random.randint(1, 25)]["data"]["title"]

    def get_image(self):
        """
        :return: (str) The URL of the image
        """

        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        if meme["message"]:
            if meme["message"] == "Too Many Requests":
                raise KeyError("Too many requests. Please wait a little.")
            else:
                raise KeyError
        else:
            return meme["data"]["children"][random.randint(1, 25)]["data"]["url_overridden_by_dest"]

    def get_post(self):
        """
        :return: (str) The URL of the image
        """

        randompost = random.randint(1, 25)

        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)

        time = meme["data"]["children"][randompost]["data"]["created"] / 1000.0

        if meme["message"]:
            if meme["message"] == "Too Many Requests":
                raise KeyError("Too many requests. Please wait a little.")
            else:
                raise KeyError
        else:
            image_link = meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"]
            title = meme["data"]["children"][randompost]["data"]["title"]
            upvote_ratio = meme["data"]["children"][randompost]["data"]["upvote_ratio"]
            total_awards = meme["data"]["children"][randompost]["data"]["total_awards_received"]
            score = meme["data"]["children"][randompost]["data"]["score"]
            downvotes = meme["data"]["children"][randompost]["data"]["downs"]
            updated = datetime.datetime.fromtimestamp(time).strftime("%d-%m-%Y %I:%M:%S UTC")
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]

            if nsfw == "false":
                nsfw = False
            elif nsfw == "true":
                nsfw = True

            if pinned == "false":
                pinned = False
            elif pinned == "true":
                pinned = True

            return f"['image_link': '{image_link}', 'title': '{title}', 'upvote_ratio': '{upvote_ratio}'," \
                   f"'total_awards': '{total_awards}', 'score': '{score}', 'downvotes': '{downvotes}'," \
                   f"'created_at': '{updated}', 'nsfw': '{nsfw}', 'pinned': '{pinned}']"
