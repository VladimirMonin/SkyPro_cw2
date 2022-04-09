from flask import Flask, request, render_template
from posts_dao import PostsDAO
# Импортируем логирование
import logging
# Включаем логирование
logging.basicConfig(encoding='utf-8', level=logging.INFO)

dao = PostsDAO()
app = Flask(__name__)


@app.route('/')
def get_main_page():
    posts_list = dao.get_main_page()
    return render_template('index.html', posts_list=posts_list)


@app.route('/posts/<int:post_id>')
def get_post_by_id(post_id):
    single_post_dict = dao.get_post_by_pk(post_id)  # Словарь с данными по ОДНОМУ посту
    post_comments_list = single_post_dict['comments']  # Список словарей с комментами (пробовал уже и так вытащить)
    return render_template('post.html', post=single_post_dict, comments=post_comments_list)

@app.route('/search/')
def get_search():
    search_str = request.args.get('s')
    logging.info(f'Поисковая фраза: {search_str}')

    post_list = dao.get_post_by_keyword(search_str)[:10]
    logging.info(f'Поисковый список: {post_list}')
    search_count = len(post_list)

    return render_template('search.html', post_list=post_list, scount=search_count)

app.run(debug=True)

"""
Bookmarks.html - закладки
Index.html - главная
Post.html - страница просмотра 1 поста
Search.html - страница результатов поиска
Tag.html - страница поиска по тэгу
"""

"""
Index.html - главная
Надо дать на главную
1. Аватарка автора 31 строка
2. Ник автора 33 строка
КАРТИНКА ПОСТА  38 строка?
3. Укороченный(!) текст поста (до скольки знаков?) 39 строка
4. Количество просмотров 43 строка
5. Колличество комментов 47 строка

Post.html - страница просмотра 1 поста
1. Ава 32 строка
НИК автора 34 строка
2. Картинка поста 41 строка
3. Комменты около 60 строки
4. Количество просмотров 55
5. Количество комментариев 52
6. Текст поста 45 (ПОЧЕМУ ДВАЖДЫ ИДЕТ???)

1. Ава 38 строка
2. Ник 40 строка
3. Картинка поста 44
4. Тэги 46 строка
5. Текст описания короткий 46 строка
6. Комментариев 48 строка
7. Количество просмотров 51 строка


МЕТОДЫ
Метод получает ОДИН пост, ищет хештеги, делает стрип и откладывает их в список
Метод получает используя метод выше пробегается по тексту поста и меняет слова на урлы

"""

