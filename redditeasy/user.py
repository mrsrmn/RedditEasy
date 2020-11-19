import requests
import json
import random
from .reddit import Reddit
import datetime
import requests.auth

client_auth = requests.auth.HTTPBasicAuth('isLVlpKPAs1cBQ', 'S5HrQV1oLjXDvs7YPdJ8hkFCN8f0oQ')
headers = {"Authorization": "bearer fhTdafZI-0ClEzzYORfBSCR7x3M", "User-Agent": "Meon/0.1 by emirsurmen"}


class User:
    def __init__(self, user):
        self.user = user

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = random.randint(0, meme["data"]["dist"])
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = random.randint(0, meme["data"]["dist"])
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["selftext"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected top post from the user
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/top.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = 1
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/top.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = 1
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["selftext"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/new.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = random.randint(0, meme["data"]["dist"])
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/new.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = random.randint(0, meme["data"]["dist"])
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["selftext"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/controversial.json",
                                   headers=headers, auth=client_auth)
            meme = json.loads(request.content)
            randompost = 1
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/controversial.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)
            randompost = 1
            nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            return Reddit(
                content=meme["data"]["children"][randompost]["data"]["selftext"],
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated
            )
