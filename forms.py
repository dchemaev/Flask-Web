from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class BooksCreateForm(FlaskForm):
    title = StringField('Заголовок книги', validators=[DataRequired()])
    content = TextAreaField('Описание', validators=[DataRequired()])
    link = StringField('Ссылка на источник', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class UserCreateForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Создать')
