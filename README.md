# Проект "Электронные товары"

## Описание

Этот проект представляет собой систему для управления продуктами и узлами сети. Включает функциональность для создания, обновления, удаления и получения информации о продуктах и узлах сети. В проект также интегрированы функции аутентификации и авторизации, управление пользователями и работа с JWT токенами.

## Установка

### Предварительные требования

- Python 3.8 или новее
- pip
- Docker (по желанию)
- Docker Compose (по желанию)

### Клонирование репозитория

git clone https://github.com/EvgeniyKhan/electronics
cd electronics
Создание виртуального окружения
python3 -m venv env
source env/bin/activate  # На Windows используйте `env\Scripts\activate`
Установка зависимостей
pip3 install -r requirements.txt
Настройка базы данных
Создайте и настройте базу данных, указав параметры подключения в файле config/settings.py.

Миграции базы данных
python3 manage.py makemigrations
python3 manage.py migrate
Создание суперпользователя
python3 manage.py createsuperuser
Запуск сервера
python3 manage.py runserver
Документация API

API доступно по следующим эндпоинтам:

Продукты

GET /api/products/ — Получить список всех продуктов
POST /api/products/ — Создать новый продукт
GET /api/products/{id}/ — Получить информацию о продукте
PUT /api/products/{id}/ — Обновить информацию о продукте
DELETE /api/products/{id}/ — Удалить продукт
Узлы сети

GET /api/networknodes/ — Получить список всех узлов сети
POST /api/networknodes/ — Создать новый узел сети
GET /api/networknodes/{id}/ — Получить информацию о узле сети
PUT /api/networknodes/{id}/ — Обновить информацию о узле сети
DELETE /api/networknodes/{id}/ — Удалить узел сети
Пользователи

POST /api/users/create/ — Создать нового пользователя
PUT /api/users/update/{id}/ — Обновить информацию о пользователе
DELETE /api/users/delete/{id}/ — Удалить пользователя
GET /api/users/{id}/ — Получить информацию о пользователе
