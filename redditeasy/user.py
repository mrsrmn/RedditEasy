from .base import get_post, get_async_post, UserBase


class User(UserBase):
    """
    This class is for getting posts from a user
    """

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return get_post(self, rtype="hot", rfor=self.user, slash="u")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return get_post(self, rtype="top", rfor=self.user, slash="u")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return get_post(self, rtype="new", rfor=self.user, slash="u")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return get_post(self, rtype="controversial", rfor=self.user, slash="u")


class AsyncUser(UserBase):
    """
    This class is for getting posts from a user in an async way
    """

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return await get_async_post(self, rtype="hot", rfor=self.user, slash="u")

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await get_async_post(self, rtype="top", rfor=self.user, slash="u")

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await get_async_post(self, rtype="new", rfor=self.user, slash="u")

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await get_async_post(self, rtype="controversial", rfor=self.user, slash="u")
