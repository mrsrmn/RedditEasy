import requests
import json
import random
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
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/hot.json")
        meme = json.loads(request.content)
        nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
        pinned = meme["data"]["children"][randompost]["data"]["pinned"]

        if nsfw == "true":
            nsfw = True
        elif nsfw == "false":
            nsfw = False

        if pinned == "true":
            pinned = True
        elif pinned == "false":
            pinned = False

        return Reddit(
            image_link=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
            title=meme["data"]["children"][randompost]["data"]["title"],
            upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
            total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
            score=meme["data"]["children"][randompost]["data"]["score"],
            downvotes=meme["data"]["children"][randompost]["data"]["downs"],
            nsfw=nsfw,
            pinned=pinned
        )

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (top)
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/top.json")
        meme = json.loads(request.content)
        nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
        pinned = meme["data"]["children"][randompost]["data"]["pinned"]

        if nsfw == "true":
            nsfw = True
        elif nsfw == "false":
            nsfw = False

        if pinned == "true":
            pinned = True
        elif pinned == "false":
            pinned = False

        return Reddit(
            image_link=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
            title=meme["data"]["children"][randompost]["data"]["title"],
            upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
            total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
            score=meme["data"]["children"][randompost]["data"]["score"],
            downvotes=meme["data"]["children"][randompost]["data"]["downs"],
            nsfw=nsfw,
            pinned=pinned
        )

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/new.json")
        meme = json.loads(request.content)
        nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
        pinned = meme["data"]["children"][randompost]["data"]["pinned"]

        if nsfw == "true":
            nsfw = True
        elif nsfw == "false":
            nsfw = False

        if pinned == "true":
            pinned = True
        elif pinned == "false":
            pinned = False

        return Reddit(
            image_link=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
            title=meme["data"]["children"][randompost]["data"]["title"],
            upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
            total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
            score=meme["data"]["children"][randompost]["data"]["score"],
            downvotes=meme["data"]["children"][randompost]["data"]["downs"],
            nsfw=nsfw,
            pinned=pinned
        )

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/r/{self.subreddit}/controversial.json")
        meme = json.loads(request.content)
        nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
        pinned = meme["data"]["children"][randompost]["data"]["pinned"]

        if nsfw == "true":
            nsfw = True
        elif nsfw == "false":
            nsfw = False

        if pinned == "true":
            pinned = True
        elif pinned == "false":
            pinned = False

        return Reddit(
            image_link=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
            title=meme["data"]["children"][randompost]["data"]["title"],
            upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
            total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
            score=meme["data"]["children"][randompost]["data"]["score"],
            downvotes=meme["data"]["children"][randompost]["data"]["downs"],
            nsfw=nsfw,
            pinned=pinned
        )