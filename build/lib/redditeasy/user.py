import requests
import json
import requests.auth
import aiohttp

import random
import datetime

from .reddit import Reddit
from .exceptions import RequestError
from .client import Client


class User:
    def __init__(self, user_agent, user, client_id, client_secret):
        self.user = user
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """
        
        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = requests.auth.HTTPBasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)

        else:
            client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            media = post[randompost]["data"]["media"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None


            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None


                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = requests.auth.HTTPBasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)

        else:
            client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            media = post[randompost]["data"]["media"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None


            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None


                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = requests.auth.HTTPBasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)

        else:
            client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            media = post[randompost]["data"]["media"]
            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None


            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None


                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = requests.auth.HTTPBasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)

        else:
            client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            request = requests.get(f"https://www.reddit.com/u/{self.user}/hot.json", headers=headers,
                                   auth=client_auth)
            meme = json.loads(request.content)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            s = post[randompost]["data"]["created"]
            media = post[randompost]["data"]["media"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None


            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None


                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])


class AsyncUser:
    def __init__(self, user_agent, user, client_id, client_secret):
        self.user = user
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret

    async def async_meme(self, headers, client_auth):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://reddit.com/u/{self.user}/hot.json", headers=headers, auth=client_auth) as r:
                content = await r.json()
                return content

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)

        else:
            client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            media = post[randompost]["data"]["media"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None

                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)

        else:
            client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            media = post[randompost]["data"]["media"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None

                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)

        else:
            client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            media = post[randompost]["data"]["media"]
            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            s = post[randompost]["data"]["created"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None

                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        if self.client_id is None or self.client_secret is None or self.user_agent is None:
            client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
            headers = {"User-Agent": Client.USER_AGENT.name}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)

        else:
            client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
            headers = {"User-Agent": self.user_agent}

            meme = await AsyncUser.async_meme(self, headers=headers, client_auth=client_auth)
        try:
            post = meme["data"]["children"]

            try:
                randompost = random.randint(0, meme["data"]["dist"] - 1)
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]
            except IndexError:
                randompost = 0
                if post[randompost]["data"]["stickied"]:
                    randompost += 1
                nsfw = post[randompost]["data"]["over_18"]

            stickied = post[randompost]["data"]["stickied"]
            spoiler = post[randompost]["data"]["spoiler"]
            s = post[randompost]["data"]["created"]
            media = post[randompost]["data"]["media"]
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            if not media:
                contenttext = post[randompost]["data"]["selftext"]
                if contenttext == "":
                    try:
                        contenttext = contenttext = post[randompost]["data"][
                            "url_overridden_by_dest"]
                    except KeyError:
                        contenttext = None
            elif media:
                try:
                    contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                except KeyError:
                    contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
            else:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]

            return Reddit(
                content=contenttext,
                title=post[randompost]["data"]["title"],
                upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                total_awards=post[randompost]["data"]["total_awards_received"],
                score=post[randompost]["data"]["score"],
                downvotes=post[randompost]["data"]["downs"],
                nsfw=nsfw,
                created_at=updated,
                author=post[randompost]["data"]["author"],
                post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                    .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                stickied=stickied,
                spoiler=spoiler,
                author_flair=flair_author,
                post_flair=flair_post,
                subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
            )
        except KeyError:
            try:
                post = meme["data"]["children"]

                try:
                    randompost = random.randint(0, meme["data"]["dist"] - 1)
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]
                except IndexError:
                    randompost = 0
                    if post[randompost]["data"]["stickied"]:
                        randompost += 1
                    nsfw = post[randompost]["data"]["over_18"]

                stickied = post[randompost]["data"]["stickied"]
                spoiler = post[randompost]["data"]["spoiler"]
                media = post[randompost]["data"]["media"]
                s = post[randompost]["data"]["created"]
                updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

                try:
                    flair_author = post[randompost]["data"]["author_flair_text"]
                    flair_post = post[randompost]["data"]["link_flair_text"]
                except IndexError:
                    flair_author = None
                    flair_post = None

                if not media:
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                    if contenttext == "":
                        try:
                            contenttext = contenttext = post[randompost]["data"]["url"]
                        except KeyError:
                            contenttext = None
                elif media:
                    try:
                        contenttext = post[randompost]["data"]["media"]["oembed"]["thumbnail_url"]
                    except KeyError:
                        contenttext = post[randompost]["data"]["secure_media_embed"][
                            "media_domain_url"]
                else:
                    contenttext = post[randompost]["data"]["url"]

                return Reddit(
                    content=contenttext,
                    title=post[randompost]["data"]["title"],
                    upvote_ratio=post[randompost]["data"]["upvote_ratio"],
                    total_awards=post[randompost]["data"]["total_awards_received"],
                    score=post[randompost]["data"]["score"],
                    downvotes=post[randompost]["data"]["downs"],
                    nsfw=nsfw,
                    created_at=updated,
                    author=post[randompost]["data"]["author"],
                    post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                        .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
                    stickied=stickied,
                    spoiler=spoiler,
                    author_flair=flair_author,
                    post_flair=flair_post,
                    subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"]
                )
            except KeyError:
                raise RequestError(meme["message"])
