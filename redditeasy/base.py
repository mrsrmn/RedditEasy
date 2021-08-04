import re

import requests
import json
import requests.auth
import aiohttp

from random import SystemRandom

from .reddit import Reddit
from .exceptions import RequestError, EmptyResult
from .client import Client

cryptogen = SystemRandom()


async def async_request(headers, client_auth, rtype, rfor, slash):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://reddit.com/{slash}/{rfor}/{rtype}.json", headers=headers,
                          auth=client_auth) as r:
            content = await r.json()
            return content


def get_request(client_auth, headers, rtype, slash, rfor):
    request = requests.get(f"https://www.reddit.com/{slash}/{rfor}/{rtype}.json", headers=headers, auth=client_auth)
    return json.loads(request.content)


def check_for_api_error(response: dict):
    if "message" in list(response.keys()):
        raise RequestError(f"{response['error']} {response['message']}")



def get_post(self, rtype, slash, rfor):
    if self.client_id is None or self.client_secret is None or self.user_agent is None:
        headers = {"User-Agent": Client.USER_AGENT.name}
        client_auth = requests.auth.HTTPBasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)

    else:
        headers = {"User-Agent": self.user_agent}
        client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)

    meme = get_request(client_auth, headers, rtype=rtype, rfor=rfor, slash=slash)
    check_for_api_error(meme)

    try:
        try:
            post = meme["data"]["children"]
            random_meme = meme["data"]["dist"]
        except TypeError:
            post = meme[0]["data"]["children"]
            random_meme = meme[0]["data"]["dist"]

        try:
            randompost = cryptogen.randint(0, random_meme - 1)
            if post[randompost]["data"]["stickied"]:
                randompost += 1
            nsfw = post[randompost]["data"]["over_18"]
        except IndexError:
            randompost = 0
            if post[randompost]["data"]["stickied"]:
                randompost += 1
            nsfw = post[randompost]["data"]["over_18"]
        except ValueError:
            raise EmptyResult("The given user / subreddit is empty")

        stickied = post[randompost]["data"]["stickied"]
        spoiler = post[randompost]["data"]["spoiler"]
        s = post[randompost]["data"]["created"]
        media = post[randompost]["data"]["media"]

        try:
            flair_author = post[randompost]["data"]["author_flair_text"]
        except IndexError:
            flair_author = None

        try:
            flair_post = post[randompost]["data"]["link_flair_text"]
        except IndexError:
            flair_post = None

        try:
            media_metadata = post[randompost]["data"]["media_metadata"]
        except KeyError:
            media_metadata = None

        if media_metadata:
            media_list = []

            for i in range(len(media_metadata)):
                media_list.append(media_metadata[list(media_metadata.keys())[i]]["s"]["u"])

            contenttext = {
                "mediaCount": len(media_metadata),
                "media": media_list,
                "fullData": media_metadata
            }
        elif not media:
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

        is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

        regex_url = re.compile(r'^(?:http|ftp)s?://')

        regex_url_image = re.compile(
            r'(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?')

        if type(contenttext) != str:
            content_type = "Gallery"
        elif re.match(regex_url_image, contenttext):
            content_type = "Image"
        elif post[randompost]["data"]["is_video"]:
            content_type = "Video"
        elif re.match(regex_url, contenttext):
            content_type = "URL"
        else:
            content_type = "Text"

        return Reddit(
            content=contenttext,
            title=post[randompost]["data"]["title"],
            upvote_ratio=post[randompost]["data"]["upvote_ratio"],
            total_awards=post[randompost]["data"]["total_awards_received"],
            score=post[randompost]["data"]["score"],
            downvotes=post[randompost]["data"]["downs"],
            nsfw=nsfw,
            created_at=int(s),
            author=post[randompost]["data"]["author"],
            post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
            stickied=stickied,
            spoiler=spoiler,
            author_flair=flair_author,
            post_flair=flair_post,
            subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"],
            comment_count=post[randompost]["data"]["num_comments"],
            is_media=is_media,
            subreddit_name=post[randompost]["data"]["subreddit"],
            content_type=content_type
        )
    except KeyError:
        try:
            post = meme["data"]["children"]
            random_meme = meme["data"]["dist"]
        except TypeError:
            post = meme[0]["data"]["children"]
            random_meme = meme[0]["data"]["dist"]

        try:
            randompost = cryptogen.randint(0, random_meme - 1)
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
        except IndexError:
            flair_author = None

        try:
            flair_post = post[randompost]["data"]["link_flair_text"]
        except IndexError:
            flair_post = None

        try:
            media_metadata = post[randompost]["data"]["media_metadata"]
        except KeyError:
            media_metadata = None

        if media_metadata:
            media_list = []

            for i in range(len(media_metadata)):
                media_list.append(media_metadata[list(media_metadata.keys())[i]]["s"]["u"])

            contenttext = {
                "mediaCount": len(media_metadata),
                "media": media_list,
                "fullData": media_metadata
            }
        elif not media:
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
                contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
        else:
            contenttext = post[randompost]["data"]["url"]

        is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

        regex_url = re.compile(r'^(?:http|ftp)s?://')
        regex_url_image = re.compile(
            r'(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?')

        if type(contenttext) != str:
            content_type = "Gallery"
        elif re.match(regex_url_image, contenttext):
            content_type = "Image"
        elif post[randompost]["data"]["is_video"]:
            content_type = "Video"
        elif re.match(regex_url, contenttext):
            content_type = "URL"
        else:
            content_type = "Text"


        return Reddit(
            content=contenttext,
            title=post[randompost]["data"]["title"],
            upvote_ratio=post[randompost]["data"]["upvote_ratio"],
            total_awards=post[randompost]["data"]["total_awards_received"],
            score=post[randompost]["data"]["score"],
            downvotes=post[randompost]["data"]["downs"],
            nsfw=nsfw,
            created_at=int(s),
            author=post[randompost]["data"]["author"],
            post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
            stickied=stickied,
            spoiler=spoiler,
            author_flair=flair_author,
            post_flair=flair_post,
            subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"],
            comment_count=post[randompost]["data"]["num_comments"],
            is_media=is_media,
            subreddit_name=post[randompost]["data"]["subreddit"],
            content_type=content_type
        )


async def get_async_post(self, rtype, rfor, slash):
    if self.client_id is None or self.client_secret is None or self.user_agent is None:
        client_auth = aiohttp.BasicAuth(Client.CLIENT_ID.name, Client.CLIENT_SECRET.name)
        headers = {"User-Agent": Client.USER_AGENT.name}

    else:
        client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
        headers = {"User-Agent": self.user_agent}

    meme = await async_request(headers=headers, client_auth=client_auth, rtype=rtype, rfor=rfor, slash=slash)
    check_for_api_error(meme)

    try:
        try:
            post = meme["data"]["children"]
            random_meme = meme["data"]["dist"]
        except TypeError:
            post = meme[0]["data"]["children"]
            random_meme = meme[0]["data"]["dist"]

        try:
            randompost = cryptogen.randint(0, random_meme - 1)
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

        try:
            flair_author = post[randompost]["data"]["author_flair_text"]
        except IndexError:
            flair_author = None

        try:
            flair_post = post[randompost]["data"]["link_flair_text"]
        except IndexError:
            flair_post = None

        try:
            media_metadata = post[randompost]["data"]["media_metadata"]
        except KeyError:
            media_metadata = None

        if media_metadata:
            media_list = []

            for i in range(len(media_metadata)):
                media_list.append(media_metadata[list(media_metadata.keys())[i]]["s"]["u"])

            contenttext = {
                "mediaCount": len(media_metadata),
                "media": media_list,
                "fullData": media_metadata
            }
        elif not media:
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

        is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

        regex_url = re.compile(r'^(?:http|ftp)s?://')
        regex_url_image = re.compile(
            r'(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?')

        if type(contenttext) != str:
            content_type = "Gallery"
        elif re.match(regex_url_image, contenttext):
            content_type = "Image"
        elif post[randompost]["data"]["is_video"]:
            content_type = "Video"
        elif re.match(regex_url, contenttext):
            content_type = "URL"
        else:
            content_type = "Text"


        return Reddit(
            content=contenttext,
            title=post[randompost]["data"]["title"],
            upvote_ratio=post[randompost]["data"]["upvote_ratio"],
            total_awards=post[randompost]["data"]["total_awards_received"],
            score=post[randompost]["data"]["score"],
            downvotes=post[randompost]["data"]["downs"],
            nsfw=nsfw,
            created_at=int(s),
            author=post[randompost]["data"]["author"],
            post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
            stickied=stickied,
            spoiler=spoiler,
            author_flair=flair_author,
            post_flair=flair_post,
            subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"],
            comment_count=post[randompost]["data"]["num_comments"],
            is_media=is_media,
            subreddit_name=post[randompost]["data"]["subreddit"],
            content_type=content_type
        )
    except KeyError:
        try:
            post = meme["data"]["children"]
            random_meme = meme["data"]["dist"]
        except TypeError:
            post = meme[0]["data"]["children"]
            random_meme = meme[0]["data"]["dist"]

        try:
            randompost = cryptogen.randint(0, random_meme - 1)
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
        except IndexError:
            flair_author = None

        try:
            flair_post = post[randompost]["data"]["link_flair_text"]
        except IndexError:
            flair_post = None

        try:
            media_metadata = post[randompost]["data"]["media_metadata"]
        except KeyError:
            media_metadata = None

        if media_metadata:
            media_list = []

            for i in range(len(media_metadata)):
                media_list.append(media_metadata[list(media_metadata.keys())[i]]["s"]["u"])

            contenttext = {
                "mediaCount": len(media_metadata),
                "media": media_list,
                "fullData": media_metadata
            }
        elif not media:
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
                contenttext = post[randompost]["data"]["secure_media_embed"]["media_domain_url"]
        else:
            contenttext = post[randompost]["data"]["url"]

        is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

        regex_url = re.compile(r'^(?:http|ftp)s?://')
        regex_url_image = re.compile(
            r'(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?')

        if type(contenttext) != str:
            content_type = "Gallery"
        elif re.match(regex_url_image, contenttext):
            content_type = "Image"
        elif post[randompost]["data"]["is_video"]:
            content_type = "Video"
        elif re.match(regex_url, contenttext):
            content_type = "URL"
        else:
            content_type = "Text"

        return Reddit(
            content=contenttext,
            title=post[randompost]["data"]["title"],
            upvote_ratio=post[randompost]["data"]["upvote_ratio"],
            total_awards=post[randompost]["data"]["total_awards_received"],
            score=post[randompost]["data"]["score"],
            downvotes=post[randompost]["data"]["downs"],
            nsfw=nsfw,
            created_at=int(s),
            author=post[randompost]["data"]["author"],
            post_url=f"https://reddit.com{post[randompost]['data']['permalink']}"
                .replace("https://reddit.com/r/u_", " https://reddit.com/u/"),
            stickied=stickied,
            spoiler=spoiler,
            author_flair=flair_author,
            post_flair=flair_post,
            subreddit_subscribers=post[randompost]["data"]["subreddit_subscribers"],
            comment_count=post[randompost]["data"]["num_comments"],
            is_media=is_media,
            subreddit_name=post[randompost]["data"]["subreddit"],
            content_type=content_type
        )


# Base classes


class SubredditBase:
    def __init__(self, subreddit, client_id=None, client_secret=None, user_agent=None):
        self.subreddit = subreddit
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent


class UserBase:
    def __init__(self, user, client_id=None, client_secret=None, user_agent=None):
        self.user = user
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret
