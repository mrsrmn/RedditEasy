from .base import _get_user_post, _get_user_async_post, UserBase


class User(UserBase):

    def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """
        return _get_user_post(self, type="hot")

    def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return _get_user_post(self, type="top")

    def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_user_post(self, type="new")

    def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return _get_user_post(self, type="controversial")


class AsyncUser(UserBase):

    async def get_post(self):
        """
        :return: (str) Info about the randomly selected post from the user
        """

        return await _get_user_async_post(self, type="hot")

    async def get_top_post(self):
        """
        :return: (str) Info about the randomly selected post (This will return the TOP POST OF TODAY, not the top post
         of all time)
        """

        return await _get_user_async_post(self, type="top")

    async def get_new_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_user_async_post(self, type="new")

    async def get_controversial_post(self):
        """
        :return: (str) Info about the randomly selected post (new)
        """

        return await _get_user_async_post(self, type="controversial")
