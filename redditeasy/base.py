import aiohttp
from random import SystemRandom

from redditeasy.classes.client_data import ClientData
from redditeasy.classes.media import Media
from redditeasy.classes.post import Post
from redditeasy.exceptions.exceptions import EmptyResult
from redditeasy.types.content_type import ContentType
from redditeasy.utils.utils import get_meme, check_for_api_error, async_request

cryptogen = SystemRandom()


def get_post(self, rtype, slash, rfor):
    if self.client_id is None or self.client_secret is None or self.user_agent is None:
        meme = get_meme(
            rtype=rtype,
            rfor=rfor,
            slash=slash,
            is_auth_provided=False
        )

    else:
        meme = get_meme(
            rtype=rtype,
            rfor=rfor,
            slash=slash,
            is_auth_provided=True,
            client_data=ClientData(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent
            )
        )

    check_for_api_error(meme)

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
    flair_author = post[randompost]["data"].get("author_flair_text", None)
    flair_post = post[randompost]["data"].get("link_flair_text", None)
    media_metadata = post[randompost]["data"].get("media_metadata", None)

    if media_metadata:
        media_list = []
        gallery_data = post[randompost]["data"]["gallery_data"]["items"]

        for i in range(len(media_metadata)):
            media_list.append(Media(**{
                "id": list(media_metadata.keys())[i],
                "media": media_metadata[list(media_metadata.keys())[i]]["s"]["u"],
                "caption": gallery_data[i]["caption"] if "caption" in gallery_data[i] else None
            }))

        contenttext = media_list
        content_type = ContentType.GALLERY
    elif not media:
        contenttext = post[randompost]["data"]["selftext"]
        content_type = ContentType.TEXT

        if contenttext == "":
            contenttext = post[randompost]["data"].get("url_overridden_by_dest", None)
            content_type = ContentType.IMAGE
    elif media:
        contenttext = post[randompost]["data"]["media"]["reddit_video"]["scrubber_media_url"]
        content_type = ContentType.VIDEO
    else:
        contenttext = post[randompost]["data"]["url_overridden_by_dest"]
        content_type = ContentType.IMAGE

    is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

    return Post(
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
        meme = await async_request(
            rtype=rtype,
            rfor=rfor,
            slash=slash,
            is_auth_provided=False
        )
    else:
        client_auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
        headers = {"User-Agent": self.user_agent}

        meme = await async_request(
            headers=headers,
            client_auth=client_auth,
            rtype=rtype, rfor=rfor,
            slash=slash,
            is_auth_provided=True
        )

    check_for_api_error(meme)

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
    flair_author = post[randompost]["data"].get("author_flair_text", None)
    flair_post = post[randompost]["data"].get("link_flair_text", None)
    media_metadata = post[randompost]["data"].get("media_metadata", None)

    if media_metadata:
        media_list = []
        gallery_data = post[randompost]["data"]["gallery_data"]["items"]

        for i in range(len(media_metadata)):
            media_list.append(Media(**{
                "id": list(media_metadata.keys())[i],
                "media": media_metadata[list(media_metadata.keys())[i]]["s"]["u"],
                "caption": gallery_data[i]["caption"] if "caption" in gallery_data[i] else None
            }))

        contenttext = media_list
        content_type = ContentType.GALLERY
    elif not media:
        contenttext = post[randompost]["data"]["selftext"]
        content_type = ContentType.TEXT

        if contenttext == "":
            contenttext = post[randompost]["data"].get("url_overridden_by_dest", None)
            content_type = ContentType.IMAGE
    elif media:
        contenttext = post[randompost]["data"]["media"]["reddit_video"]["scrubber_media_url"]
        content_type = ContentType.VIDEO
    else:
        contenttext = post[randompost]["data"]["url_overridden_by_dest"]
        content_type = ContentType.IMAGE

    is_media = True if not post[randompost]["data"]["domain"].startswith("self") else False

    return Post(
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
    def __init__(self, client_id=None, client_secret=None, user_agent=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent


class UserBase:
    def __init__(self, client_id=None, client_secret=None, user_agent=None):
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret
