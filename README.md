
# Руководство по установке проекта





#### Clone a GitHub Repository 

```http
  git clone https://github.com/bzmaxat/docshub.git
```

#### Create a virtual environment.

Unix/Linux/macOS

```http
  python3 -m venv venv
```

Windows 

```http
  python -m venv venv
```
#### Activate the virtual environment

Unix/Linux/macOS

```http
  source env/bin/activate
```

Windows 

```http
  .\env\Scripts\activate
```

#### Install the requirements

```http
  pip install -r requirements.txt
```

#### Make your migrations

```http
  python manage.py makemigrations
  python manage.py migrate
```

#### Create a new superuser

```http
  python manage.py createsuperuser
```

#### And finally

```http
  python manage.py runserver
```



## API

URL для HTTP запросов: `http://127.0.0.1:8000/api/docs/`

`GET` запрос - Аутентификация не требуется

`POST, PUT, PATCH, DELETE` запросы - Требуется аутентификация

Для получения токена:

`POST` запрос на `http://127.0.0.1:8000/api-token-auth/` с параметрами 
```http
{
    "username": "example@mail.com",
    "password": "password"
}
```
