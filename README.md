# api_final
api final

## Описание
Данный проект - упрощенная блог-платформа. Можно заводить пользователей с логинами и паролями, заводить группы будущих постов, затем пользователи постят посты, а также оставляют комментарии к чужим постам. Пользователи могут быть подписаны на других пользователей. Пользователи могут менять (модифицировать, удалять) свой контент, но не могут чужой. бОльшая часть операций на чтение доступна даже незалогированным пользователям.
Пользы особо от проекта нет, разве что закрепить полученные на учебном курсе знания об API.

## Установка
- убедиться, что репозитарий имеет статус public, а не private, либо попросить владельца сменить его на такой
- клонировать репозитарий
```
git clone https://github.com/D77S/api_final_yatube
```
- перейти в папку склонированного проекта
```
cd api_final_yatube
```
- создать окружение
```
python -m venv venv
```
(Данная и некоторые последующие команды - только для windows, у кого не он - те пусть сами найдут свои варианты команд.)
- активировать его
```
source venv/Scripts/activate
```
- установить требуемые для проекта пакеты
```
pip install -r requirements.txt
```
- перейти в папку с менеджером
```
cd yatube_api
```
- сделать миграции
```
python manage.py migrate
```
- запустить сервер
```
python manage.py runserver
```

## Примеры
Некоторые примеры запросов к API

- Получение публикаций
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
```
http://127.0.0.1:8000/api/v1/posts/
```
```
http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100
```
- Создание публикации
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
http://127.0.0.1:8000/api/v1/posts/
```
Получение одной публикации
Обновление/частичное обновление/удаление публикации
По id публикации
Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```
```
http://127.0.0.1:8000/api/v1/posts/1/
```
Получение/добавление комментариев (понятное дело, к одной публикации, не к нескольким сразу)
По id публикации
Получение всех комментариев/добавление одного нового комментария к публикации.
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```
Получение/обновление/частичное обновление/удаление одного конкретного комментария
По id публикации и id комментария
Обновить/удалить комментарий может только автор комментария. Анонимные запросы запрещены.
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
```
http://127.0.0.1:8000/api/v1/posts/1/comments/1/
```
Список групп
Получение списка доступных групп.
```
http://127.0.0.1:8000/api/v1/groups/
```
Информация о группе
По id группы
```
http://127.0.0.1:8000/api/v1/groups/{id}/
```
```
http://127.0.0.1:8000/api/v1/groups/1/
```
Подписки (фолловеры)
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
Подписание пользователя, от имени которого сделан запрос, на пользователя, переданного в теле запроса. Анонимные запросы запрещены.
```
http://127.0.0.1:8000/api/v1/follow/
```
Управление пользователями
Создание первого пользователя
```
python manage.py createsuperuser
```

Создание следующего пользователя
```
http://127.0.0.1:8000/api/v1/users
```
Получение токена пользователя
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Обновление токена пользователя
```
http://127.0.0.1:8000/api/v1/jwt/refresh/
```
