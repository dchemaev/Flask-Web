from flask_restful import abort

from flask import Flask, redirect, session, request
from flask import render_template as flask_render_template
import extra.auth as auth
from api.v1 import init as init_api_v1
from forms import *

from models import User, Books


def init_route(app, db):
    # Переопределение стандартного рендера, добавляет параметр auth_user
    def render_template(*args, **kwargs):
        kwargs['auth_user'] = auth.get_user()
        return flask_render_template(*args, **kwargs)

    init_api_v1(app, auth)  # Инициализация маршрутов для API

    @app.route('/')
    @app.route('/index')
    def index():
        if not auth.is_authorized():
            return render_template(
                'index.html',
                title='Главная',
            )
        all_book_list = Books.query.filter_by(user_id=auth.get_user().id)
        return render_template(
            'books-list.html',
            title="Мои книги",
            books_list=all_book_list
        )

    @app.route('/install')
    def install():
        db.create_all()
        return render_template(
            'install-success.html',
            title="Главная"
        )

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        has_error = False
        login = ''
        if request.method == 'POST':
            username = request.form['username']
            if auth.login(username, request.form['password']):
                return redirect('/')
            else:
                has_error = True
        return render_template(
            'login.html',
            title='Вход',
            login=login,
            has_error=has_error
        )

    @app.route('/logout', methods=['GET'])
    def logout():
        auth.logout()
        return redirect('/')

    @app.route('/user/create', methods=['GET', 'POST'])
    def registration():
        has_error = False
        form = UserCreateForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                has_error = True
            else:
                User.add(username=username, password=password)
                auth.login(username, password)
                return redirect('/')
        return render_template(
            'registration.html',
            title='Зарегистрироваться',
            form=form,
            has_error=has_error
        )

    @app.route('/books', methods=['GET'])
    def Books_list():
        if not auth.is_authorized():
            return redirect('/login')
        Books_list = Books.query.filter_by(user_id=auth.get_user().id)
        return render_template(
            'books-list.html',
            title="Книги",
            books_list=Books_list
        )

    @app.route('/book/create', methods=['GET', 'POST'])
    def Books_create_form():
        if not auth.is_authorized():
            return redirect('/login')
        form = BooksCreateForm()
        if form.validate_on_submit():
            title = form.title.data
            author = form.author.data
            content = form.content.data
            link = form.link.data
            Books.add(title=title, author=author, content=content, link=link, user=auth.get_user())
            return redirect('/')
        return render_template(
            'books-create.html',
            title='Создать книгу',
            form=form
        )

    @app.route('/book/<int:id>')
    def Books_view(id: int):
        if not auth.is_authorized():
            return redirect('/login')
        Book = Books.query.filter_by(id=id).first()
        if not Book:
            abort(404)
        if Books.user_id != auth.get_user().id:
            abort(403)
        user = Book.user
        return render_template(
            'books-view.html',
            title='Книга - ' + Book.title,
            book=Book,
            author=Book.author,
            content=Book.content,
            user=user,
            link=Book.link
        )

    @app.route('/book/delete/<int:id>')
    def Book_delete(id: int):
        if not auth.is_authorized():
            return redirect('/login')
        book = Books.query.filter_by(id=id).first()
        if Books.user_id != auth.get_user().id:
            abort(403)
        book.delete(book)
        return redirect('/book')


