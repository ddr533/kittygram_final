[![Main Kittygramm workflow](https://github.com/ddr533/kittygram_final/actions/workflows/main.yaml/badge.svg)](https://github.com/ddr533/kittygram_final/actions/workflows/main.yaml)

# KittyGram  
##### Описание проекта 
Kittygram — социальная сеть для обмена фотографиями любимых питомцев.
##### Основные возможности:
* Публикация фотографий и достижений питомцев.
* Получение данных по API.

##### Технологии 
  
 - Python 3.9   
 - Django 4.0
 - Django rest_framework
 - Docker
 - Sqlite3
 - React
  
### Как запустить проект на localhost (разработка):

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ddr533/kittygram_final.git
```

```
cd infra_sprint1
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
```
source env/scripts/activate
```
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Как запустить проект в контейнере Docker Linux:
* Установить Докер
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
sudo systemctl status docker
```
* Установить и настроить nginx на порт 9000:
```
sudo apt install nginx -y
sudo systemctl start nginx
sudo nano /etc/nginx/sites-enabled/default
........
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
........

```

* Скопируйте на сервер в директорию kittygram/ файл docker-compose.production.yml
* Запустите docker compose
```
sudo docker compose -f docker-compose.production.yml up -d
```
* Выполните миграции, соберите статические файлы бэкенда и скопируйте их в /backend_static/static/:
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```


### Примеры запросов API:
* Создание нового пользователя:
  
  - api/users/
```
    {
        "email": "string",
        "username": "string",
        "password": "string"
    }

``` 
* Получение токена для аутентификации (Token): 

  - api/token/
```
    {
        "username": "string",
        "password": "string"
    }

``` 
* Получить список всех котов (GET): 

  - api/сats/

```
{
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 24,
            "name": "Мурка",
            "color": "black",
            "birth_year": 1999,
            "achievements": [
                {
                    "id": 3,
                    "achievement_name": "Спит весь день"
                },
                {
                    "id": 1,
                    "achievement_name": "Считай голубей"
                }
            ],
            "owner": "Иван",
            "age": 24,
            "image": "http://127.0.0.1:8080/media/cats/images/temp.png",
            "image_url": "/media/cats/images/temp.png"
        },
  ....

```
* Разместить фото кота (POST): 

  - api/cats/
  - В поле image передавать строку с картинкой в формате base64 

```
        {
            "name": "Василий",
            "color": "#DCDCDC",
            "birth_year": 2020,
            "image": base64
            "achievements": [
                {"achievement_name": "разбил вазу"}
            ]
        }   

```

### Автор:
Андрей Дрогаль & Yandex_Practicum
