from .base import get_post, get_async_post, UserBase


class User(UserBase):
    """
    This class is for getting posts from a user
    """

    def get_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return get_post(self, rtype="hot", rfor=user, slash="u")

    def get_top_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (This will return the TOP POST OF TODAY,
         not the top post of all time)
        """

        return get_post(self, rtype="top", rfor=user, slash="u")

    def get_new_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (new)
        """

        return get_post(self, rtype="new", rfor=user, slash="u")

    def get_controversial_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (new)
        """

        return get_post(self, rtype="controversial", rfor=user, slash="u")


class AsyncUser(UserBase):
    """
    This class is for getting posts from a user in an async way
    """

    async def get_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return await get_async_post(self, rtype="hot", rfor=user, slash="u")

    async def get_top_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (This will return the TOP POST OF TODAY,
         not the top post of all time)
        """

        return await get_async_post(self, rtype="top", rfor=user, slash="u")

    async def get_new_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (new)
        """

        return await get_async_post(self, rtype="new", rfor=user, slash="u")

    async def get_controversial_post(self, user):
        """
        :return: (str) Info about the randomly selected post from the user (new)
        """

        return await get_async_post(self, rtype="controversial", rfor=user, slash="u")
