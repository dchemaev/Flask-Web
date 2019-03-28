from requests import get, post, delete

cookies = dict(session='session cookies here')
print()
print(post('http://localhost:8000/api/v1/books',
           json={'title': 'Название', 'author': 'Автор', 'content': 'Текст ниги', 'link': 'Ссылка', 'user_id': 1},
           cookies=cookies).json())
print()
print(get('http://localhost:8000/api/v1/books').json())
print()
print(delete('http://localhost:8000/api/v1/books/5', cookies=cookies).json())
print()
print(get('http://localhost:8000/api/v1/books').json())
