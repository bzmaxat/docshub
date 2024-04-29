
# Руководство по установке проекта





#### Clone a GitHub Repository 

```link
git clone https://github.com/bzmaxat/docshub.git
```

#### Create a virtual environment.

Unix/Linux/macOS

```link
  python3 -m venv venv
```

Windows 

```link
  python -m venv venv
```
#### Activate the virtual environment

Unix/Linux/macOS

```link
  source env/bin/activate
```

Windows 

```link
  .\env\Scripts\activate
```

#### Install the requirements

```link
  pip install -r requirements.txt
```

#### Make your migrations

```link
  python manage.py makemigrations
  python manage.py migrate
```

#### Create a new superuser

```link
  python manage.py createsuperuser
```

#### And finally

```link
  python manage.py runserver
```



## API

URL для HTTP запросов: `http://127.0.0.1:8000/api/docs/`

`GET` запрос - Аутентификация не требуется

`POST, PUT, PATCH, DELETE` запросы - Требуется аутентификация

Для получения токена:

`POST` запрос на `http://127.0.0.1:8000/api-token-auth/` с параметрами 
```json
{
    "username": "example@mail.com",
    "password": "password"
}
```
