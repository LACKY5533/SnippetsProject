# Snippets_28052025

## Инструкция по развертыванию проекта

1. Создать виртуальное окружение:  
```
python3 -m venv django_venv
```
2. Aктивировать виртуальное окружение:  
```
source django_venv/bin/activate
```
3. Установить нужные пакеты:  
```
python -m pip install -r requirements.txt
```
4. Применить миграции (и загрузить данные в БД)
```
python manage.py migrate
```
5. Запустить сервер
```
python manage.py runserver
```

## Выгрузка и загрузка данных при работе с БД
### Выгрузка данных из БД
```
python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/all_items.json
```
### Загрузка данных в БД
```
python manage.py loaddata MainApp/fixtures/all_items.json
```

## Дополнительно
1. Полезное расширение для шаблонов: `django`
```
ext install bastiteo.vscode-django
```
2. Добавить в `settings.json`
```
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "*.html": "django-html"
    }
```