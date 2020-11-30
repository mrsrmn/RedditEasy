import requests
import json
import random
from .reddit import Reddit
import datetime
import requests.auth
from dotenv import load_dotenv
import os

load_dotenv(".env")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
auth = os.getenv("AUTH")
user_agent = os.getenv("USER_AGENT")

client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
headers = {"Authorization": auth, "User-Agent": user_agent}


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

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["selftext"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/top.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/top.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["selftext"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/new.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/new.json", headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["selftext"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        try:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/controversial.json",
                                   headers=headers, auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["url_overridden_by_dest"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            request = requests.get(f"https://www.reddit.com/u/{self.user}/controversial.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)

            try:
                randompost = random.randint(0, meme["data"]["dist"])
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                nsfw = meme["data"]["children"][randompost]["data"]["over_18"]

            pinned = meme["data"]["children"][randompost]["data"]["pinned"]
            stickied = meme["data"]["children"][randompost]["data"]["stickied"]
            spoiler = meme["data"]["children"][randompost]["data"]["spoiler"]
            s = meme["data"]["children"][randompost]["data"]["created"]
            media = meme["data"]["children"][randompost]["data"]["media"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = meme["data"]["children"][randompost]["data"]["author_flair_text"]
                flair_post = meme["data"]["children"][randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if nsfw == "true":
                nsfw = True
            elif nsfw == "false":
                nsfw = False

            if pinned == "true":
                pinned = True
            elif pinned == "false":
                pinned = False

            if stickied == "true":
                stickied = True
            elif stickied == "false":
                stickied = False

            if spoiler == "true":
                spoiler = True
            elif spoiler == "false":
                spoiler = False

            if media is None:
                contenttext = meme["data"]["children"][randompost]["data"]["selftext"]
            else:
                contenttext = meme["data"]["children"][randompost]["data"]["url"]

            return Reddit(
                content=contenttext,
                title=meme["data"]["children"][randompost]["data"]["title"],
                upvote_ratio=meme["data"]["children"][randompost]["data"]["upvote_ratio"],
                total_awards=meme["data"]["children"][randompost]["data"]["total_awards_received"],
                score=meme["data"]["children"][randompost]["data"]["score"],
                downvotes=meme["data"]["children"][randompost]["data"]["downs"],
                nsfw=nsfw,
                pinned=pinned,
                created_at=updated,
                author=meme["data"]["children"][randompost]["data"]["author"],
                post_url=f"https://reddit.com{meme['data']['children'][randompost]['data']['permalink']}",
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=meme["data"]["children"][randompost]["data"]["subreddit_subscribers"]
            )
