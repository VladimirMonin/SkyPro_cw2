from flask import Flask, request, render_template
from posts_dao import PostsDAO
# Импортируем логирование
import logging

# Включаем логирование
logging.basicConfig(encoding='utf-8', level=logging.INFO)

dao = PostsDAO()
app = Flask(__name__)


#  ВЬЮШКА ГЛАВНОЙ СТРАНИЦЫ
@app.route('/')
def get_main_page():
    posts_list = dao.get_main_page()
    return render_template('index.html', posts_list=posts_list)


#  ВЬЮШКА СТРАНИЦЫ 1 ПОСТА (по ID)
@app.route('/posts/<int:post_id>')
def get_post_by_id(post_id):
    single_post_dict = dao.get_post_by_pk(post_id)  # Словарь с данными по ОДНОМУ посту
    return render_template('post.html', post=single_post_dict)


#  ВЬЮШКА СТРАНИЦЫ ПОИСКА
@app.route('/search/')  # http://127.0.0.1:5000/search/?s=%D0%B5%D0%B4%D0%B0
def get_search():
    search_str = request.args.get('s')
    logging.info(f'Поисковая фраза: {search_str}')

    post_list = dao.get_post_by_keyword(search_str)[:10]
    logging.info(f'Поисковый список: {post_list}')
    search_count = len(post_list)

    return render_template('search.html', post_list=post_list, scount=search_count)


app.run(debug=True)
