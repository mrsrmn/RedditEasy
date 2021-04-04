from .base import _get_post, _get_async_post, UserBase


class User(UserBase):
    """
    This class is for getting posts from a user
    """

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return _get_post(self, type="hot", rfor=self.user, slash="u")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return _get_post(self, type="top", rfor=self.user, slash="u")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="new", rfor=self.user, slash="u")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_post(self, type="controversial", rfor=self.user, slash="u")


class AsyncUser(UserBase):
    """
    This class is for getting posts from a user in an async way
    """

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return await _get_async_post(self, type="hot", rfor=self.user, slash="u")

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await _get_async_post(self, type="top", rfor=self.user, slash="u")

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="new", rfor=self.user, slash="u")

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_async_post(self, type="controversial", rfor=self.user, slash="u")
