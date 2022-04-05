import json

from config import *


class PostsDAO:

    def __init__(self):
        self.posts_list = None
        self.comments_list = None

    def load_posts(self):
        """Метод загружает файл с постами и сохраняет их в поле объекта"""
        with open(POSTS_JSON, 'r', encoding='utf-8') as file:
            self.posts_list = json.load(file)

    def load_comments(self):
        """Метод загружает файл с комментами и сохраняет их в поле объекта"""
        with open(COMMENTS_JSON, 'r', encoding='utf-8') as file:
            self.comments_list = json.load(file)

    def get_posts(self):
        """Метод загружает данные по постам в поле объекта и возвращает список словарей с постами """
        self.load_posts()
        return self.posts_list

    def get_comments(self):
        """ Метод загружает данные по комментам в поле объекта и возвращает список словарей с комментами"""
        self.load_comments()
        return self.comments_list

    def get_all(self):
        """Метод обновляет поля объекта данными с Json посты и комменты"""
        self.get_posts()
        self.get_comments()

    def get_posts_by_user(self, user_name):
        """ Метод обновляет поле с постами, а потом возвращает список словарей постов конкретного пользователя """
        user_posts_list = []
        self.get_posts()
        for post in self.posts_list:
            if post['poster_name'] == user_name:
                user_posts_list.append(post)
        return user_posts_list

    def get_comments_by_post_id(self, post_id):
        """ Метод обновляет поле с комментами, а потом возвращает комменты принадлежащие конкретному посту"""
        comments_list = []
        self.get_comments()
        for comment in self.comments_list:
            if comment['post_id'] == post_id:
                comments_list.append(comment)
        return comments_list

    def get_post_by_keyword(self, keyword):
        """Метод обновляет поле с постами, а потом возвращает пост с искомыми словами в тексте поста"""
        post_list = []
        self.get_posts()
        for post in self.posts_list:
            if keyword.lower() in post['content'].lower():
                post_list.append(post)
        return post_list

    def get_post_by_pk(self, pk):
        """Метод обновляет поле с постами, а потом возвращает пост по его ID в виде списка"""
        post_list = []
        self.get_posts()
        for post in self.posts_list:
            if post['pk'] == pk:
                post_list.append(post)
        return post_list
