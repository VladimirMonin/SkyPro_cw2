from flask import Flask, request, render_template
from posts_dao import PostsDAO

dao = PostsDAO()
app = Flask(__name__)

@app.route('/')
def get_main_page():
    return render_template('index.html')

app.run(debug=True)

"""
Надо дать на главную
1. Аватарка автора
2. Ник автора
3. Укороченный(!) текст поста (до скольки знаков?)
4. Количество просмотров
5. 
"""