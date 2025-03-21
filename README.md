Для Развертывания на сервере потребуется

** клонироват репозиторий с GitHub:**

git@github.com:aleksospishev/drf_sky.git
Установить на сервере Docker, Docker Compose:


```

Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:

SECRET_KEY              - секретный ключ Django проекта
DOCKER_PASSWORD         - пароль от Docker Hub
DOCKER_USERNAME         - логин Docker Hub
HOST                    - публичный IP сервера
USER                    - имя пользователя на сервере
PASSPHRASE              - *если ssh-ключ защищен паролем
SSH_KEY                 - приватный ssh-ключ
DB_NAME                 - имя базы данных
POSTGRES_USER           - пользователь базы данных
POSTGRES_PASSWORD       - пароль от базы данных
DB_HOST                 - db
DB_PORT                 - 5432 (порт по умолчанию)

ntcn