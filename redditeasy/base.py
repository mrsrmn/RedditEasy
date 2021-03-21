import requests
import json
import requests.auth
import aiohttp

import random
import datetime

from .reddit import Reddit
from .exceptions import RequestError
from .client import Client


async def async_request(async_headers, async_client_auth, type, rfor, slash):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://reddit.com/{slash}/{rfor}/{type}.json", headers=async_headers,
                          auth=async_client_auth) as r:
            content = await r.json()
            return content


def get_request(client_id, client_secret, headers, type, slash, rfor):
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    request = requests.get(f"https://www.reddit.com/{slash}/{rfor}/{type}.json", headers=headers,
                           auth=client_auth)
    return json.loads(request.content)


#Subreddit Posts

def _get_post(self, type, slash, rfor):
    if self.client_id is None or self.client_secret is None or self.user_agent is None:
        headers = {"User-Agent": Client.USER_AGENT.name}
        meme = get_request(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name, headers, type=type, rfor=rfor,
                           slash=slash)

    else:
        headers = {"User-Agent": self.user_agent}
        meme = get_request(self.client_id, self.client_secret, headers, type=type, rfor=rfor,
                           slash=slash)

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
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
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

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if not media:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                if contenttext == "":
                    try:
                        contenttext = post[randompost]["data"]["url"]
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


async def _get_async_post(self, type, rfor, slash):
    if self.client_id is None or self.client_secret is None or self.user_agent is None:
        client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
        headers = {"User-Agent": Client.USER_AGENT.name}

        meme = await async_request(async_headers=headers, async_client_auth=client_auth, type=type, rfor=rfor,
                                   slash=slash)

    else:
        client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
        headers = {"User-Agent": self.user_agent}

        meme = await async_request(async_headers=headers, async_client_auth=client_auth, type=type, rfor=rfor,
                                   slash=slash)

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
                    contenttext = post[randompost]["data"]["url_overridden_by_dest"]
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

            try:
                flair_author = post[randompost]["data"]["author_flair_text"]
                flair_post = post[randompost]["data"]["link_flair_text"]
            except IndexError:
                flair_author = None
                flair_post = None

            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")

            if not media:
                contenttext = post[randompost]["data"]["url_overridden_by_dest"]
                if contenttext == "":
                    try:
                        contenttext = post[randompost]["data"]["url"]
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


# Base classes


class SubredditBase:
    def __init__(self, subreddit, client_id=None, client_secret=None, user_agent=None):
        self.subreddit = subreddit
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent


class UserBase:
    def __init__(self, user_agent, user, client_id, client_secret):
        self.user = user
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret
