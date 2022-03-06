from .base import get_post, get_async_post, UserBase
from .classes.post import Post


class User(UserBase):
    """
    This class is for getting posts from a user
    """

    def get_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (hot)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return get_post(self, rtype="hot", rfor=user, slash="u")

    def get_top_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (top)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return get_post(self, rtype="top", rfor=user, slash="u")

    def get_new_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (new)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return get_post(self, rtype="new", rfor=user, slash="u")

    def get_controversial_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (controversial)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return get_post(self, rtype="controversial", rfor=user, slash="u")


class AsyncUser(UserBase):
    """
    This class is for getting posts from a user in an async way
    """

    async def get_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (hot)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return await get_async_post(self, rtype="hot", rfor=user, slash="u")

    async def get_top_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (top)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return await get_async_post(self, rtype="top", rfor=user, slash="u")

    async def get_new_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (new)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return await get_async_post(self, rtype="new", rfor=user, slash="u")

    async def get_controversial_post(self, user: str) -> Post:
        """
        :return: Info about the randomly selected post from the user (controversial)
        :param: user (:obj:`builtins.str`) - The user to get the post from
        :rtype: Post
        """

        return await get_async_post(self, rtype="controversial", rfor=user, slash="u")
