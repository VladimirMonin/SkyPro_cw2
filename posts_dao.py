import json

from config import *


class PostsDAO:

    def __init__(self):
        self.posts_list = None
        self.comments_list = None

    def load_posts(self):
        with open(POSTS_JSON, 'r', encoding='utf-8') as file:
            self.posts_list = json.load(file)

    def load_comments(self):
        with open(COMMENTS_JSON, 'r', encoding='utf-8') as file:
            self.comments_list = json.load(file)

    def get_posts(self):
        self.load_posts()
        return self.posts_list

    def get_comments(self):
        self.load_comments()
        return self.comments_list

    def load_all(self):
        self.get_posts()
        self.get_comments()

    def get_posts_by_user(self, user_name):
        user_posts_list = []
        self.load_all()
        for post in self.posts_list:
            if post['poster_name'] == user_name:
                user_posts_list.append(post)
        return user_posts_list

    def get_comments_by_post_id(self, post_id):
        comments_list = []
        self.load_all()
        for comment in self.comments_list:
            if comment['post_id'] == post_id:
                comments_list.append(comment)
        return comments_list


dao = PostsDAO()
print(dao.get_comments_by_post_id(1))
