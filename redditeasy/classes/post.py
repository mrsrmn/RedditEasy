from typing import Union

from redditeasy.types.content_type import ContentType


class Post:
    def __init__(self, content, title, upvote_ratio, total_awards, score, downvotes, created_at, nsfw, author, post_url,
                 stickied, spoiler, post_flair, author_flair, subreddit_subscribers, comment_count, is_media,
                 subreddit_name, content_type):
        self._content = content
        self._title = title
        self._upvote_ratio = upvote_ratio
        self._total_awards = total_awards
        self._score = score
        self._downvotes = downvotes
        self._created_at = created_at
        self._nsfw = nsfw
        self._author = author
        self._post_url = post_url
        self._stickied = stickied
        self._spoiler = spoiler
        self._post_flair = post_flair
        self._author_flair = author_flair
        self._subreddit_subscribers = subreddit_subscribers
        self._comment_count = comment_count
        self._is_media = is_media
        self._subreddit_name = subreddit_name
        self._content_type = content_type

    @property
    def content(self) -> str:
        """:return: The content of the post"""
        return self._content
    
    @property
    def title(self) -> str:
        """:return: The title of the post"""
        return self._title
    
    @property
    def upvote_ratio(self) -> int:
        """:return: The upvote ratio of the post"""
        return self._upvote_ratio

    @property
    def total_awards(self) -> int:
        """:return: The number of total awards of the post"""
        return self._total_awards
    
    @property
    def score(self) -> int:
        """:return: The upvote count of the post"""
        return self._score 
    
    @property
    def downvotes(self) -> int:
        """:return: The downvote count of the post"""
        return self._downvotes

    @property
    def created_at(self) -> int:
        """:return: The time when the post was created in epoch"""
        return self._created_at

    @property
    def nsfw(self) -> bool:
        """:return: If the post is marked as NSFW or not"""
        return self._nsfw

    @property
    def author(self) -> str:
        """:return: The author of the post"""
        return self._author

    @property
    def post_url(self) -> str:
        """:return: The URL of the post"""
        return self._post_url
    
    @property
    def stickied(self) -> bool:
        """:return: If the post is stickied or not"""
        return self._stickied
    
    @property
    def spoiler(self) -> bool:
        """:return: If the post is marked as spoiler or not"""
        return self._spoiler

    @property
    def post_flair(self) -> Union[str, None]:
        """:return: The flair of the post. If there isn't any, ``None``"""
        return self._post_flair

    @property
    def author_flair(self) -> Union[str, None]:
        """:return: The flair of the author. If there isn't any, ``None``"""
        return self._author_flair
    
    @property
    def subreddit_subscribers(self) -> int:
        """:return: The members in the subreddit the post is from"""
        return self._subreddit_subscribers
    
    @property
    def comment_count(self) -> int:
        """:return: The number of comments in the post"""
        return self._comment_count
    
    @property
    def is_media(self) -> bool:
        """:return: If the posts content is media (e.g. Image, Video)"""
        return self._is_media
    
    @property
    def subreddit_name(self) -> str:
        """:return: If the name of the subreddit the post is from"""
        return self._subreddit_name
    
    @property
    def content_type(self) -> ContentType:
        """:return: The type of the post"""
        return self._content_type
