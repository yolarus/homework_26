# Домашнее задание №32, урок 26

## Описание
1. Продолжена разработка приложения apple_shop, добавлены контроллеры ProductUpdateView, ProductDeleteView
2. Контроллеры ProductUpdateView, ProductCreateView в приложении apple_shop и ArticleCreateView, ArticleUpdateView собираются на основе кастомных форм ProductForm, ArticleForm
3. Формы ProductForm, ArticleForm стилизованы
4. В форме ProductForm с помощью метода clean_field настроена валидация полей name, description, price_per_unit, photo для предотвращения использования запрещенных слов, указания отрицательной цены и загрузки изображения неверного формата / более 5 Мб 
5. Скорректирован файл README.md

## Установка проекта
1. Клонирование проекта из [GitHub](https://github.com/yolarus/homework_26) по HTTPS-токену или SSH-ключу
2. Создание и заполнение файла .env своими данными

## Запуск
1. прописать в командной строке 'python manage.py runserver'
2. Нажать на ссылку на локальный сервер


## Установка зависимостей
1. Перейти в настройки Pycharm -> Setting -> Project -> Python Interpreter 
2. Добавить локальный интерпретатор с менеджером пакетов Poetry
3. Выполнить команду в терминале PyCharm 'poetry install'

## Тестирование
1. Тесты не выполнялись 