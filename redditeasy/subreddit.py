from .base import get_post, get_async_post, SubredditBase


class Subreddit(SubredditBase):
    """
    This class is for getting posts from a subreddit
    """

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        return get_post(self, rtype="hot", rfor=self.subreddit, slash="r")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return get_post(self, rtype="top", rfor=self.subreddit, slash="r")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return get_post(self, rtype="new", rfor=self.subreddit, slash="r")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return get_post(self, rtype="controversial", rfor=self.subreddit, slash="r")


class AsyncSubreddit(SubredditBase):
    """
    This class is for getting posts from a subreddit in an async way
    """

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        return await get_async_post(self, rtype="hot", rfor=self.subreddit, slash="r")

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await get_async_post(self, rtype="top", rfor=self.subreddit, slash="r")

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await get_async_post(self, rtype="new", rfor=self.subreddit, slash="r")

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await get_async_post(self, rtype="controversial", rfor=self.subreddit, slash="r")
