### Проект YaMDb.
Описание:
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Возможности:
Просматривать, создавать новые, удалять и изменять отзывы.
Комментировать отзывы, смотреть, удалять и обновлять комментарии к отзывам.

### Как запустить проект:

Установка Python 3.7 и подготовка окружения
Установите программное обеспечение: скачайте установочные файлы и запустите их.
Python: www.python.org/downloads/ устанавливаем Python 3.7
Visual Studio Code: code.visualstudio.com/download
Git: git-scm.com/download/win
```
Запустить Git Bash
Клонировать репозиторий и перейти в него в командной строке Git Bash:
```
git clone git@github.com:haddaway11/api_yamdb.git
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
на Mac или Linux:
python3 -m venv env
source env/bin/activate
для Windows:
python -m venv venv
source venv/Scripts/activate
```

Обновляем pip
на Mac или Linux:
python3 -m pip install --upgrade pip
для Windows:
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
```

Выполнить миграции:

на Mac или Linux:
python3 manage.py migrate
для Windows:
python manage.py migrate
```

Запустить проект:
на Mac или Linux:
python3 manage.py runserver
для Windows:
python manage.py runserver
```

### Документация к API проекта Yatube:
по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube

Алгоритм регистрации пользователей
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).

Пользовательские роли
Аноним — может просматривать описания произведений, читать отзывы и комментарии.
Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
Суперюзер Django — обладет правами администратора (admin)


#Регистрация нового пользователя
/auth/signup/ (POST)
{
  "email": "string",
  "username": "string"
}
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.
использовать имя 'me' в качестве username запрещено.
Поля email и username должны быть уникальными.

Получение JWT-токена
/auth/token/ (POST)
{
  "username": "string",
  "confirmation_code": "string"
}

/categories/ (GET)
Получить список всех категорий
Права доступа: Доступно без токена
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]

/categories/ (POST)
Создать категорию.
Права доступа: Администратор.
Поле slug каждой категории должно быть уникальным.
{
  "name": "string",
  "slug": "string"
}

/categories/{slug}/ (DEL)
Удалить категорию.
Права доступа: Администратор.

/genres/ (GET)
Получить список всех жанров.
Права доступа: Доступно без токена.
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]

/genres/ (POST)
Добавить жанр.
Права доступа: Администратор.
Поле slug каждого жанра должно быть уникальным.
{
  "name": "string",
  "slug": "string"
}

/genres/{slug}/ (DEL)
Удалить жанр.
Права доступа: Администратор.

/titles/ (GET)
Получение списка всех произведений.
Права доступа: Доступно без токена.
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]

/titles/ (POST)
Добавить новое произведение.
Права доступа: Администратор.
Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего).
При добавлении нового произведения требуется указать уже существующие категорию и жанр.
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}

/titles/{titles_id}/ (GET)
информация о произведении
Права доступа: Доступно без токена
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}

/titles/{titles_id}/ (PATCH)
Обновить информацию о произведении
Права доступа: Администратор
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}

/titles/{titles_id}/ (DEL)
Удалить произведение.
Права доступа: Администратор.

/titles/{title_id}/reviews/ (GET)
Получить список всех отзывов.
Права доступа: Доступно без токена.
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]

/titles/{title_id}/reviews/ (POST)
Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение.
Права доступа: Аутентифицированные пользователи.
{
  "text": "string",
  "score": 1
}

/titles/{title_id}/reviews/{review_id}/ (GET)
Получить отзыв по id для указанного произведения.
Права доступа: Доступно без токена.
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}

/titles/{title_id}/reviews/{review_id}/ (PATCH)
Частично обновить отзыв по id.
Права доступа: Автор отзыва, модератор или администратор.
{
  "text": "string",
  "score": 1
}

/titles/{title_id}/reviews/{review_id}/ (DEL)
Удалить отзыв по id
Права доступа: Автор отзыва, модератор или администратор.

/titles/{title_id}/reviews/{review_id}/comments/ (GET)
Получить список всех комментариев к отзыву по id
Права доступа: Доступно без токена.
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]

/titles/{title_id}/reviews/{review_id}/comments/ (POST)
Добавить новый комментарий для отзыва.
Права доступа: Аутентифицированные пользователи.
{
  "text": "string"
}

/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ (GET)
Получить комментарий для отзыва по id.
Права доступа: Доступно без токена.
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}

/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ (PATCH)
Частично обновить комментарий к отзыву по id.
Права доступа: Автор комментария, модератор или администратор.
{
  "text": "string"
}

/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ (DEL)
Удалить комментарий к отзыву по id.
Права доступа: Автор комментария, модератор или администратор.

/users/ (GET)
Получить список всех пользователей.
Права доступа: Администратор
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]

/users/ (POST)
Добавить нового пользователя.
Права доступа: Администратор
Поля email и username должны быть уникальными.
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}

/users/{username}/ (GET)
Получить пользователя по username.
Права доступа: Администратор
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}

/users/{username}/ (PATCH)
изменить данные пользователя по username.
Права доступа: Администратор.
Поля email и username должны быть уникальными.
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}

/users/{username}/ (DEL)
Удалить пользователя по username.
Права доступа: Администратор.

/users/me/ (GET)
Получить данные своей учетной записи
Права доступа: Любой авторизованный пользователь
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}

/users/me/ (PATCH)
изменить данные своей учетной записи
Права доступа: Любой авторизованный пользователь
Поля email и username должны быть уникальными.
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}