# стек Django ORM (Admin, Models, PosgreSQL, кастомные команды по заполнению данных) ##
# Как пользоваться проектом:
  1) Клонировать проект в отдельную папку
  2) Провести настройку виртуального окружения
# Настройка виртуального окружения на windows, cmd:
    Создать виртуальное окружение
        python -m venv venv
        venv/scripts/activate
    В виртуальном окружении запустить команду:
        pip install -r ./requirements.txt

  3) Создать админку:
       python manage.py createsuperuser
  4) Создать БД в ручном режиме в pgAdmin, внести настройки подключения в корне_проекта/config/settings.py, переменная DATABASE
  5) Запустить сервер:
       Прописать скрипт параметр "runserver" в конфигурации к "manage.py"
       Или запустить команду в консоли:
         python manage.py runserver
  6) Заполнить БД через учетку админа по адресу_сервера/admin,
     Или заполнить файл main/data/main_data.json, далее использовать команду:
       python -Xutf8 manage.py dumpdata main --exclude contenttypes --output main/data/main_data.json
  7) Применить кастомную команду в cmd:
       python manage.py fill
     Модели и их поля посмотреть в main/models.py



