## Вступление
Task manager - это JSON API, который дает возможность пользователю ставить себе задачи, отражать в системе изменение их статуса и просматривать историю задач.

## Стек
Python, Django, Django REST fremawork, django-filter, docker, PostgreSQL, gunicorn

## Authorization
API предназначет только для использования авторизованным пользователям.
Для получения доступа к API вам нужно зарегистрировать пользователя в task_manager POST запросом на http://127.0.0.1:8000/api/v1/register/ с параметрами *user* и *password*, после чего по POST запрос на http://127.0.0.1:8000/api/v1/token/ с теми же параметрами и вы получите JWT токен. 
При отправке любого запроса передавайте токен в заголовке **Authorization: Bearer <токен>**

## Функциональность
Главные кейсы использования Task manager API:
1. Пользователь может зарегистрироваться в сервисе задав пару логин-пароль
2. В системе может существовать много пользователей
3. Пользователь может авторизоваться в сервисе предоставив пару логин-пароль и получив в ответе токен
4. Пользователь видит только свои задачи
5. Пользователь может создать себе задачу. Задача должна как минимум содержать следующие данные:
    (*) - обязательные поля. Остальные значения полей можно оставить пустыми
    - *Название
    - *Описание
    - *Время создания
    - *Статус
    - Планируемое дата завершения
6. ПОлльзователь может менять планируемое время завершения, название и описание задачи
7. Пользователь может менять статусзадачи н любой из данного набора
8. Пользователь может получить список задач своих задач, с возможностью фильтрации по статусу и планируемому времени завершения
9. Пользователь может просмотреть историю изменений задачи (названия, описания, статуса, времени завершения)

Статус можно задать только из перечня:
* NEW - Новая (по умолчанию)
* PLANNED - Запланированная 
* IN_PROGRESS - В работе
* COMPLETED - Завершенная

Дату завершения нужно задавать в формате %Y-%m-%d %H:%M

## Доступные методы
| endpoint | Тип запроса | Описание |
| :--- | :--- | :--- | 
| api/v1/register/ | POST | Регистрация пользователя|
| api/v1/token/ | POST | Получение JWT токена (access и refresh)|
| api/v1/tasks/ | GET, POST  | Получение списка всех задач пользователя, фильтрайия списка по статусу и времени завершения или создание новой задачи|
| api/v1/tasks/{task_id}/ | GET, PUT, PATCH, DELETE  | Получение, удаление, частичное/пoлное редактирование задачи по ее id|
| api/v1/tasks/{task_id}/history | GET | Получние истории изменений задачи по ее id|

## Примеры
Все API ендпоинты возвращают JSON представление получаемых, созданных или отредактированных объектов.

Пример запроса POST на api/v1/tasks/

    {
        "title":"Найти Йеннифер",
        "description": "Жди меня в Вербицах у Вызимы"
        "status": "IN_PROGRESS"
        "complete_date": 2021-11-01 12:22
    }

Пример ответа: 

    {
        "id": 5,
        "title": "grobubar",
        "description": "дескриптион389",
        "author": "lirikbk",
        "create_date": "2020-10-05T20:24:33.780781Z",
        "status": "IN_PROGRESS",
        "complete_date": "2021-11-01T12:22:00Z"
    }

Пример GET запроса на api/v1/tasks/

    {
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 5,
            "title": "grobubar",
            "description": "дескриптион",
            "author": "lirikbk",
            "create_date": "2020-10-05T20:24:33.780781Z",
            "status": "IN_PROGRESS",
            "complete_date": "2021-11-01T12:22:00Z"
        },
        {
            "id": 4,
            "title": "grobubar",
            "description": "дескриптион",
            "author": "lirikbk",
            "create_date": "2020-10-05T19:20:05.252352Z",
            "status": "IN_PROGRESS",
            "complete_date": null
        },
       ......
    }

## Инструкция к запуску
На вашей локальной машине должен быть установлен Docker
1. Склонировать репозиторий к себе на локальную машину
2. В корневой директории проекта файл .env и прописать, в нем следующее:
    ```
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    ```
3. Далее в теоминале выполнить команду `docker-compose up`.
4. Когда контейнер запустится, выполнить команду `docker stats` и узнать id контейнера, название которого заканчивается на web
5. Подключиться к контейнеру командой docker exec -it <id контейнера> bash
6. в контейнере выполнить команду python manage.py migrate

