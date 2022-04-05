import json
from config import *

def get_posts_all(filename=POSTS_JSON):

    try:
        file = open(filename, encoding='UTF-8')
        candidates = json.load(file)
        file.close()
        return candidates
    except ValueError:
        return 'Ошибка чтения файла'  # includes simplejson.decoder.JSONDecodeError (согласно стаковерфлоу)
    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'
    pass


def get_post_by_user(username):
    """Возвращает посты конкретного юзера"""
    pass


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    pass


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    pass


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    pass
