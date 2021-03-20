from .base import _get_post, _get_async_post, SubredditBase


class Subreddit(SubredditBase):

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """

        return _get_post(self, type="hot")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """
        return _get_post(self, type="top")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="new")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="controversial")


class AsyncSubreddit(SubredditBase):

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the subreddit (hot)
        """
        return await _get_async_post(self, type="hot")


    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await _get_async_post(self, type="top")


    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="new")


    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="controversial")
