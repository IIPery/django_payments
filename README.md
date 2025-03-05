Django + stripe

тестовые данные карты

Номер карты: 4242 4242 4242 4242
11/26  CVC: 123 index: 000000

# Django + stripe API

## Описание:
stripe.com/docs - платёжная система с подробным API и бесплатным тестовым режимом для имитации
и тестирования платежей. 
С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов,
сохранять данные клиента, и реализовывать прочие платежные функции. 

## Стек технологий:
- Python 3.10
- Django 5.1
- Django rest framework
- HTML/CSS
- Sqlite3
- Stripe 11.6

## Установка:
1. Клонировать репозиторий
```commandline
git clone
```
2. Переименовать .env.example в .env
- добавить секретные ключи
- https://dashboard.stripe.com/test/dashboard

3. Запустить Docker
```commandline
docker-compose up --build
```
4. Создать суперпользователя
```commandline
docker-compose exec web python manage.py createsuperuser
```
5. Добавить в админке товары, скидки и налоги

