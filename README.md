Для Развертывания на сервере потребуется

** клонироват репозиторий с GitHub:**

git@github.com:aleksospishev/drf_sky.git
Установить на сервере Docker, Docker Compose:

sudo apt install curl                                   - установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      - скачать скрипт для установки
sh get-docker.sh                                        - запуск скрипта
sudo apt-get install docker-compose-plugin              - последняя версия docker compose

**_Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):_**
```
scp docker-compose.yml nginx.conf username@IP:~/foodgram/infra

# username - имя пользователя на сервере
# IP - публичный IP сервера
```

Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:

SECRET_KEY              - секретный ключ Django проекта
DOCKER_PASSWORD         - пароль от Docker Hub
DOCKER_USERNAME         - логин Docker Hub
HOST                    - публичный IP сервера
USER                    - имя пользователя на сервере
PASSPHRASE              - *если ssh-ключ защищен паролем
SSH_KEY                 - приватный ssh-ключ
TELEGRAM_TO             - ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          - токен бота, посылающего сообщение

DB_ENGINE               - django.db.backends.postgresql
DB_NAME                 - postgres
POSTGRES_USER           - postgres
POSTGRES_PASSWORD       - postgres
DB_HOST                 - db
DB_PORT                 - 5432 (порт по умолчанию)
_Создать и запустить контейнеры Docker, выполнить команду на сервере из директории foodgram/infra:_

sudo docker-compose up -d
Выполнить миграции:

sudo docker-compose exec web python manage.py migrate
Собрать статику:

sudo docker-compose exec web python manage.py collectstatic --noinput
Наполнить базу данных содержимым из файла ingredients.json:

sudo docker-compose exec web python manage.py loaddata data/ingredients.json
Создать суперпользователя:

sudo docker-compose exec web python manage.py createsuperuser
Для остановки контейнеров Docker:

sudo docker-compose down -v      - с их удалением
sudo docker-compose stop         - без удаления
данные для входа в админ:

exam@admin.ru    -email
1234             -password
# drf_sky