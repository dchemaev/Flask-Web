"""
Точка входа

Здесь инициализируются все настройки, подключения к БД, приложение flask и маршрутизатор (router)

После инициализации запускается вебсервер
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controller import init_route
from dbase import db
from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()

app = Flask(__name__)
app.config['SECRET_KEY'] = cipher_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_route(app, db)

app.run(port=8000, host='127.0.0.1')
