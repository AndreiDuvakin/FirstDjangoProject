# Запуск проекта (Linux)

Перед запуском проекта откройте терминал в папке рядом
с папкой проекта (так, чтобы при вводе команды `ls` у вас
отображалась папка [lyceum](lyceum), файл [requirements.txt](requirements/prod.txt) и др.)

Командой `python -m venv venv` создадим виртуальное окружение и
командой `source venv/bin/activate` запустим его, после выполнения
данной команды в самой левой части строки терминала должна появится
надпись (venv).

Для запуска приложения понадобиться файл .env, который должен содержать
следующие переменные:

* SECRET_KEY
* TIME_ZONE
* LANGUAGE_CODE
* DEBUG

По умолчанию можете установить следующие значения:

* SECRET_KEY=придумайте_ключ
* TIME_ZONE=UTC
* LANGUAGE_CODE=en-us
* DEBUG=True

Теперь установим зависимости, запуск проекта для проверки работоспособности
потребует ввода команды `pip install -r requirements/prod.txt`. Зависимости
необходимые для разработки проекта можно установить командой `pip install -r requirements/dev.txt`.  
А для запуска проекта в режиме теста команда: `pip install -r requirements/test.txt`.

Перейдем в папку с проектом, командой `cd lyceum`, в таком
случае при вводе команды `ls` вы должны увидеть файлы [manage.py](lyceum%2Fmanage.py),
[db.sqlite3](lyceum%2Fdb.sqlite3), папку [lyceum](lyceum%2Flyceum) и другие. Запустим
наш проект командой `python manage.py runserver`, после этого при
переходе на адрес http://127.0.0.1:8000/ у вас должна открыться
страница приветствия, это означает, что проект успешно запущен.

## Статус проверки:
[![Pipeline status](https://gitlab.crja72.ru/django/2024/spring/course/students/43836-Mr.BoyMan-yandex.ru-course-1112/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/spring/course/students/43836-Mr.BoyMan-yandex.ru-course-1112/pipelines)