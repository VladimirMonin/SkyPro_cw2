import pytest
from posts_dao import PostsDAO

dao = PostsDAO()


class TestPostDAO:

    def test_create_postsDAO_object(self):
        assert isinstance(dao, PostsDAO) == True

    def test_get_posts(self):
        assert isinstance(dao.get_posts(), list) == True

    def test_get_comments(self):
        assert isinstance(dao.get_comments(), list) == True

    def test_get_posts_by_user(self, data=1):
        assert isinstance(dao.get_posts_by_user(data), list) == True

    def test_get_post_by_keyword(self, data='ЕДА'):
        assert isinstance(dao.get_post_by_keyword(data), list) == True

    def test_get_post_by_pk(self, data=1):
        assert isinstance(dao.get_post_by_pk(data), list) == True
