from flask import Flask, request, render_template
from posts_dao import PostsDAO

dao = PostsDAO()
app = Flask(__name__)


@app.route('/')
def get_main_page():
    posts_list = dao.get_main_page()
    return render_template('index.html', posts_list=posts_list)


@app.route('/posts/<post_id>')
def get_post_by_id(post_id):
    single_post_dict = dao.get_post_by_pk(post_id)  # Словарь с данными по ОДНОМУ посту
#    post_comments_list = single_post_dict['comments']  # Список словарей с комментами
    return render_template('post.html', post=single_post_dict)


app.run(debug=True)

"""
Главная
Надо дать на главную
1. Аватарка автора 31 строка
2. Ник автора 33 строка
КАРТИНКА ПОСТА  38 строка?
3. Укороченный(!) текст поста (до скольки знаков?) 39 строка
4. Количество просмотров 43 строка
5. Колличество комментов 47 строка

Пост
1. Ава 32 строка
НИК автора 34 строка
2. Картинка поста 41 строка
3. Комменты около 60 строки
4. Количество просмотров 55
5. Количество комментариев 52
6. Текст поста 45 (ПОЧЕМУ ДВАЖДЫ ИДЕТ???)
"""
