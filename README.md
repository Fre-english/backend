# Django Project Setup


## Установка

1. Создайте виртуальное окружение и активируйте его:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

2. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Настройка проекта

1. Переименуйте файл `.env.example` в `.env` и настройте переменные окружения. Пример файла:

    ```bash
    SECRET_KEY=django-insecure-jsp7vi%&d33*g^po98m^y6_w54_dczhbpy
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=Get from Google Console
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=Get from Google Console
    ```

2. Примените миграции для базы данных:

    ```bash
    python manage.py migrate
    ```


## Запуск проекта

Чтобы запустить проект на локальном сервере, выполните команду:

1.

```bash
python manage.py runserver
```

2.

```bash
celery -A freenglish.celery_app worker --loglevel=info --pool=solo
```

3.

```bash
daphne -b 0.0.0.0 -p 8001 freenglish.asgi:application
```

