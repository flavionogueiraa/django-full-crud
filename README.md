# Django full crud!
This package is for you to create a fully automatic CRUD of your models.

## Dependencies
Django

## Installation
```shell
pip install django-full-crud
```

Add the following in settings.py:
```python
INSTALLED_APPS = [
    ...
    'django_full_crud',
    ...
]
```

## Features
- Creation the admin file
- Creation the form file
- Creation the templates (delete, detail, form and list)
- Creation the views (create, delete, detail, list and update)
- Creation of paths present in urls.py.
- Creation the init files.

## Recommendations
Build your apps using this [app template](https://github.com/TimeNovaData/django_app_modelo)


## Getting start
Create a .vscode file at the root of your project, then add a file called "django_full_crud.json". 

Add the following to it:
```json
{
    "project_name": "name_of_your_project"
}
```

After that in need to create your models and add them to init.py.
The following commands can be run in the terminal:

---
```shell
python manage.py full_crud nome_app NomeModel
```
The full_crud runs on the specified model.

---
```shell
python manage.py full_crud nome_app
```
The full_crud runs ont the specified app.

---
```shell
python manage.py full_crud
```
The full_crud runs on the project.
