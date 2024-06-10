# Django Tutorial 01

- Reference: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

## Check django version

```bash
python3 -m django --version
```

## Install django

```bash
pip3 install django==5.0.6
```

## Start project

```bash
django-admin startproject django_tutorial_01
```

## Install requirementx.txt

```bash
pip3 install -r requirements.txt
```

## Run migrate

- Create postgre schema before run migrate

```bash
python3 manage.py migrate
```

## Run server

```bash
python3 manage.py runserver
```

- Open

```bash
localhost:8000
```
