# Foodgram - Продуктовый помощник

Foodgram - это онлайн-сервис для публикации и обмена рецептами. Пользователи могут создавать свои рецепты, добавлять чужие рецепты в избранное, подписываться на других авторов и скачивать список покупок для выбранных блюд.

## Технологии

- Python 3.9
- Django 4.2
- Django REST Framework 3.15
- PostgreSQL 13
- Docker
- Nginx
- Gunicorn
- GitHub Actions

## Возможности

- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление рецептов
- Добавление рецептов в избранное
- Добавление рецептов в список покупок
- Скачивание списка ингредиентов для покупки
- Подписка на авторов
- Фильтрация рецептов по тегам
- Поиск ингредиентов
- Генерация коротких ссылок на рецепты

## Установка и запуск проекта локально

### 1. Клонируйте репозиторий:
```bash
git clone git@github.com:IlshatSharafukov/foodgram.git
cd foodgram
```

### 2. Создайте файл `.env` в папке `infra/`:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_HOST=db
DB_PORT=5432
```

### 3. Запустите проект через Docker Compose:
```bash
cd infra
docker-compose up -d --build
```

### 4. Выполните миграции:
```bash
docker-compose exec backend python manage.py migrate
```

### 5. Создайте суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```

### 6. Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

### 7. Импортируйте ингредиенты:
```bash
docker-compose exec backend python manage.py load_ingredients
```

### 8. Проект доступен по адресам:

- Фронтенд: https://diplomyandex123456.servepics.com/
- API: https://diplomyandex123456.servepics.com/api/
- Админка: https://diplomyandex123456.servepics.com/admin/
- Документация API: https://diplomyandex123456.servepics.com/api/docs/

## Примеры запросов к API

### Регистрация пользователя

**POST** `/api/users/`

Тело запроса:
```json
{
  "email": "user@example.com",
  "username": "username",
  "first_name": "Имя",
  "last_name": "Фамилия",
  "password": "password123"
}
```

Ответ:
```json
{
  "email": "user@example.com",
  "id": 1,
  "username": "username",
  "first_name": "Имя",
  "last_name": "Фамилия"
}
```

### Получение токена

**POST** `/api/auth/token/login/`

Тело запроса:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Ответ:
```json
{
  "auth_token": "your-auth-token-here"
}
```

### Создание рецепта

**POST** `/api/recipes/`

Заголовки:
```
Authorization: Token your-auth-token-here
```

Тело запроса:
```json
{
  "ingredients": [
    {
      "id": 1,
      "amount": 200
    }
  ],
  "tags": [1, 2],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "Название рецепта",
  "text": "Описание рецепта",
  "cooking_time": 30
}
```

Ответ:
```json
{
  "id": 1,
  "tags": [...],
  "author": {...},
  "ingredients": [...],
  "is_favorited": false,
  "is_in_shopping_cart": false,
  "name": "Название рецепта",
  "image": "http://localhost:8000/media/recipes/image.png",
  "text": "Описание рецепта",
  "cooking_time": 30
}
```

### Получение списка рецептов

**GET** `/api/recipes/`

Параметры запроса:
- `page` - номер страницы
- `limit` - количество результатов на странице
- `is_favorited` - фильтр по избранному (0/1)
- `is_in_shopping_cart` - фильтр по списку покупок (0/1)
- `author` - ID автора
- `tags` - slug тегов (можно передать несколько)

Пример: `/api/recipes/?tags=breakfast&tags=lunch`

Ответ:
```json
{
  "count": 123,
  "next": "http://localhost:8000/api/recipes/?page=2",
  "previous": null,
  "results": [...]
}
```

### Скачать список покупок

**GET** `/api/recipes/download_shopping_cart/`

Заголовки:
```
Authorization: Token your-auth-token-here
```

Ответ: файл `shopping_list.txt` с суммированными ингредиентами

## Деплой на сервер

### 1. Подготовьте сервер:
```bash
# Установите Docker и Docker Compose
sudo apt update
sudo apt install docker.io docker-compose-plugin -y

# Создайте папку проекта
mkdir -p ~/foodgram
cd ~/foodgram
```

### 2. Создайте `.env` файл на сервере:
```env
DEBUG=False
SECRET_KEY=super-secret-production-key
ALLOWED_HOSTS=yourdomain.com,ip-address
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=strong-password
DB_HOST=db
DB_PORT=5432
```

### 3. Получите SSL сертификат (для HTTPS):
```bash
sudo certbot certonly --standalone -d yourdomain.com --email your@email.com --agree-tos
```

### 4. Настройте GitHub Actions:

Добавьте секреты в Settings → Secrets and variables → Actions:

- `DOCKER_USERNAME` - ваш Docker Hub username
- `DOCKER_PASSWORD` - ваш Docker Hub password
- `HOST` - IP адрес сервера
- `USER` - пользователь на сервере
- `SSH_KEY` - приватный SSH ключ
- `SSH_PASSPHRASE` - пароль от SSH ключа (если есть)
- `TELEGRAM_TO` - ваш Telegram chat ID
- `TELEGRAM_TOKEN` - токен Telegram бота

### 5. Деплой происходит автоматически при пуше в ветку `main`

## Автор

Sharafukov Ilshat

GitHub: [@IlshatSharafukov](https://github.com/IlshatSharafukov)

## Развернутый проект

**URL:** https://diplomyandex123456.servepics.com

**Админка:** https://diplomyandex123456.servepics.com/admin/

Email админки: yc-admin-test@gmail.com
Имя пользователя: superpuperuser12349
Имя: superpuperuser12349
Password: superpuperuser12349@
