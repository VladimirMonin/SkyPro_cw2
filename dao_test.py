import pytest
from posts_dao import PostsDAO

dao = PostsDAO()


class TestPostDAO:

    def test_create_postsDAO_object(self):
        """Проверяем создание объекта DAO"""
        assert isinstance(dao, PostsDAO) == True

    def test_list_get_posts(self):
        """Проверяем что в поле постов попал именно список словарей с нужными полями"""
        dao.get_posts()
        assert isinstance(dao.posts_list, list) == True
        assert isinstance(dao.posts_list[0], dict) == True
        assert dao.posts_list[0]["poster_nam"]
        assert dao.posts_list[0]["poster_avatar"]
        assert dao.posts_list[0]["pic"]
        assert dao.posts_list[0]["content"]
        assert dao.posts_list[0]["views_count"]
        assert dao.posts_list[0]["likes_count"]
        assert dao.posts_list[0]["pk"]

    def test_list_get_comments(self):
        dao.get_comments()
        assert isinstance(dao.comments_list, list) == True
        assert isinstance(dao.comments_list[0], dict) == True
        assert dao.comments_list[0]['post_id']
        assert dao.comments_list[0]['commenter_name']
        assert dao.comments_list[0]['comment']
        assert dao.comments_list[0]['pk']

    def test_get_posts_by_user(self, data='leo'):
        assert isinstance(dao.get_posts_by_user(data), list) == True
        assert len(dao.get_posts_by_user(data)) > 0, 'Ожидается 1 и более'
        assert dao.get_posts_by_user(data)[0]['comments_count'], 'Ожидается наличие ключа comments_count'

    def test_get_post_by_keyword(self, data='ЕДА'):
        assert isinstance(dao.get_post_by_keyword(data), list) == True

    def test_get_post_by_pk(self, data=1):
        assert isinstance(dao.get_post_by_pk(data), dict) == True

    def test_get_posts_for_json(self):
        assert isinstance(dao.get_posts_for_json(), list) == True

    def test_get_main_page(self):
        assert isinstance(dao.get_main_page(), list) == True
