# yamdb_final

![workflow](https://github.com/LariosDeen/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?)

Учебный проект для изучения работы CI CD (Яндекс Практикум)  

Server IP:  
[84.252.142.175](http://84.252.142.175/admin)

### Описание работы проекта

Данный проект является проектом учебного курса Яндекс Практикум по
специальности Python-разработчик.
* Проект собирает отзывы (Review) пользователей на произведения (Titles). 
* Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
* Список категорий (Category) может быть расширен администратором (например, 
можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
* Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или 
послушать музыку.
* В каждой категории есть произведения: книги, фильмы или музыка. 
Например, в категории «Книги» могут быть произведения «Винни-Пух и 
все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» 
группы «Насекомые» и вторая сюита Баха.
* Произведению может быть присвоен жанр (Genre) из списка предустановленных 
(например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только 
администратор.
* Благодарные или возмущённые пользователи оставляют к произведениям текстовые 
отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти 
(целое число); из пользовательских оценок формируется усреднённая оценка 
произведения — рейтинг (целое число). На одно произведение пользователь может 
оставить только один отзыв.

### Примеры

##### Пользователь аутентифицируется посредвстом сервиса Simple JWT.  
Получите код подтверждения регистрации.  
Отправьте POST запрос с именем пользователя и e-mail на эндпойнт:  

[http://84.252.142.175/api/v1/auth/signup/](http://84.252.142.175/api/v1/auth/signup/)


POST request:
```
{
    "email": "terminator@skynet.com",
    "username": "terminator"
}
```

Response:
```
{
    "email": "terminator@skynet.com",
    "username": "terminator"
}
```

##### Получите токен для доступа к функциям сервиса проекта. 
Отправьте POST запрос с именем пользователя и полученным по e-mail 
кодом подтвреждения на эндпойнт:

[http://84.252.142.175/api/v1/auth/token/](http://84.252.142.175/api/v1/auth/token/)


POST request:
```
{
    "username": "terminator",
    "confirmation_code": "1234"
}
```

Response:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlb90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1OTc4OTAwOSwiaWF0IjoxNjU4MDYxMDA5LCJqdGkiOiJkNTUyNTJlODQ0OGI0MDExYjFjOGYwZDYxOGU2ZjAxZCIsInVzZXJfaWQiOjF9.IVjgYCbZiQ_kdraTYIz4VdYYpZoh7kTMxpmjjJ1tkIg",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlb90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4OTI1MDA5LCJpYXQiOjE2NTgwNjEwMDksImp0aSI6ImIzZDViMmY2YjExZjQxMTM4NTk1NWVmMzg5NmZmM2JkIiwidXNlcl9pZCI6MX0.dEfpwO3ZBA62R6lH6ybHx3KxCZU9PgQCoXvaEsl5UyI"
}
```

##### При желании можно заполнить пустые поля в своем профайле, отправив PATCH запрос на эндпойнт:

[http://84.252.142.175/api/v1/users/me/](http://84.252.142.175/api/v1/users/me/)

PATCH request:
```
{
    "username": "terminator",
    "email": "terminator@skynet.ru",
    "role": "user",
    "bio": "My biography.",
    "first_name": "Arnold",
    "last_name": "Schwarzenegger"
}
```

Response:
```
{
    "username": "terminator",
    "email": "terminator@skynet.ru",
    "role": "user",
    "bio": "My biography.",
    "first_name": "Arnold",
    "last_name": "Schwarzenegger"
}
```

##### Получение списка произведений GET запрос:

[http://84.252.142.175/api/v1/titles/](http://84.252.142.175/api/v1/titles/)


Response:
```
{
    "count": 32,
    "next": "http://web:8000/api/v1/titles/?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "rating": 7,
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "category": {
                "name": "Фильм",
                "slug": "movie"
            },
            "name": "12 разгневанных мужчин",
            "year": 1957,
            "description": null
        },
        {
            "id": 30,
            "rating": 10,
            "genre": [
                {
                    "name": "Рок",
                    "slug": "rock"
                }
            ],
            "category": {
                "name": "Музыка",
                "slug": "music"
            },
            "name": "Deep Purple — Smoke on the Water",
            "year": 1971,
            "description": null
        },
```


##### Получение информации о произведении GET запрос:
```
http://84.252.142.175/api/v1/titles/{titles_id}/
```

Response:
```
{
    "id": 5,
    "rating": 5,
    "genre": [
        {
            "name": "Комедия",
            "slug": "comedy"
        },
        {
            "name": "Детектив",
            "slug": "detective"
        },
        {
            "name": "Триллер",
            "slug": "thriller"
        }
    ],
    "category": {
        "name": "Фильм",
        "slug": "movie"
    },
    "name": "Криминальное чтиво",
    "year": 1994,
    "description": null
}
```

##### Создайте отзыв о произведении POST запрос:
```
http://84.252.142.175/api/v1/titles/{title_id}/reviews/
```
POST request:
```
{
    "genre": ["ballad"],
    "category": "book",
    "name": "Some name.",
    "year": 1999
}
```
Response:
```
{
    "id": 33,
    "genre": [
        "ballad"
    ],
    "category": "book",
    "name": "Some name.",
    "year": 1999,
    "description": null,
    "rating": null
}
```

##### Все доступные команды по использованию сервиса можно посмотреть на URL:

[http://84.252.142.175/redoc/](http://84.252.142.175/redoc/)

##### Теги для postman:  

Body
```
raw
```
```
JSON
```

Headers
```
Authorization
```
```
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZ
XhwIjoxNjU4OTMxNDA1LCJpYXQiOjE2NTgwNjc0MDUsImp0aSI6IjkzNDNlMzgzYmU1ZDRlMzg4ZD
A3OWI0ZTVlNTUzYzVhIiwidXNlcl9pZCI6MX0.sj5mOT2DrIX9TQ
```

### В проекте использованы технологии:

* Python
* Django
* Django REST Framework
* Simple JWT
* Docker
* Docker-compose
* Postgres
* Gunicorn
* Nginx
* Workflow

Проект выполнил студент 31 когорты Яндекс Практикума  
Лариос Димитри  
https://github.com/LariosDeen  
https://t.me/dimilari
