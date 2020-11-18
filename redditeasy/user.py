import requests
import json
import random
from .reddit import Reddit


class User:
    def __init__(self, user):
        self.user = user

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json")
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
        :return: (str) Info about the randomly selected top post from the user
        """

        randompost = random.randint(1, 25)
        request = requests.get(f"https://www.reddit.com/u/{self.user}/top.json")
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
        request = requests.get(f"https://www.reddit.com/u/{self.user}/new.json")
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
        request = requests.get(f"https://www.reddit.com/u/{self.user}/controversial.json")
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
