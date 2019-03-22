from requests import get, post, delete

cookies = dict(session='session cookies here')
print(post('http://localhost:8000/api/v1/books',
           json={'title': 'Заголовок', 'content': 'Текст ниги', 'link': 'Ссылка', 'user_id': 1},
           cookies=cookies).json())
print(get('http://localhost:8000/api/v1/books').json())
print(delete('http://localhost:8000/api/v1/books/5', cookies=cookies).json())
print(get('http://localhost:8000/api/v1/books').json())
