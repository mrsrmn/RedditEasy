from .base import _get_post, _get_async_post, SubredditBase


class Subreddit(SubredditBase):
    """
    This class is for getting posts from a subreddit
    """

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        return _get_post(self, type="hot", rfor=self.subreddit, slash="r")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return _get_post(self, type="top", rfor=self.subreddit, slash="r")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="new", rfor=self.subreddit, slash="r")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="controversial", rfor=self.subreddit, slash="r")


class AsyncSubreddit(SubredditBase):
    """
    This class is for getting posts from a subreddit in an async way
    """

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        return await _get_async_post(self, type="hot", rfor=self.subreddit, slash="r")

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await _get_async_post(self, type="top", rfor=self.subreddit, slash="r")

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="new", rfor=self.subreddit, slash="r")

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="controversial", rfor=self.subreddit, slash="r")
