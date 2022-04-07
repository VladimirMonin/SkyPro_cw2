from flask import Flask, request, render_template
from posts_dao import PostsDAO

dao = PostsDAO()
app = Flask(__name__)


@app.route('/')
def get_main_page():
    return render_template('index.html', dao=dao)


app.run(debug=True)

"""
Надо дать на главную
1. Аватарка автора 31 строка
2. Ник автора 33 строка
3. Укороченный(!) текст поста (до скольки знаков?) 39 строка
4. Количество просмотров 43 строка
5. Колличество комментов 47 строка
"""
