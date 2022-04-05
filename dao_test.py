import pytest
from posts_dao import PostsDAO

dao = PostsDAO()


class TestPostDAO:

    def test_create_postsDAO_object2(self):
        assert isinstance(dao, PostsDAO) == True

    def test_get_posts(self):
        assert isinstance(dao.get_posts(), list) == True



# dao = PostsDAO()
# print(type(dao))
