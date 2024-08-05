import os
import sys
from importlib import import_module

import django
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

from django_full_crud.admin.main import create_admin_files
from django_full_crud.forms.main import create_forms_files
from django_full_crud.globals import PROJECT_NAME, base_dir, get_project_dir
from django_full_crud.serializers.main import create_serializers_files
from django_full_crud.templates.main import create_templates_files
from django_full_crud.urls.main import create_urls_files
from django_full_crud.utils import (
    camel_to_snake_case,
    check_and_create_folders,
    get_modules,
)
from django_full_crud.views.main import create_views_files
from django_full_crud.viewsets.main import create_viewsets_files


def make_initial_configs():
    sys.path.insert(1, os.path.join(base_dir()))
    sys.path.insert(1, os.path.join(get_project_dir()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings")
    Cling(get_wsgi_application())

    django.setup()


def get_app_models(app_name):
    models = []
    package = import_module(f"{app_name}.models")
    all_models = getattr(package, "__all__")
    for model in all_models:
        models.append(model.__name__)

    return models


def get_project_models():
    models = []
    modules = get_modules(get_project_dir())
    only_folders = get_only_folders(modules)
    only_apps = get_only_apps(only_folders)
    for module in only_apps:
        models_folder = import_module(f"{module['module_name']}.models")
        models_from_this_app = getattr(models_folder, "__all__")
        for model in models_from_this_app:
            models.append(model.__name__)

    return models


def get_only_folders(init_list):
    return list(filter(lambda init: init["folder"], init_list))


def get_only_files(init_list):
    return list(filter(lambda init: not init["folder"], init_list))


def get_only_apps(modules):
    return list(filter(lambda module: search_models_folder(module), modules))


def search_models_folder(module):
    for children in module["childrens"]:
        if children["module_name"] == "models":
            return True
    return False


def execute(app_name, models):
    for model in models:
        print("\n========================================")
        print(f"CRUD of {app_name}.{model}:")
        snake_model_name = camel_to_snake_case(model)
        model_exists = os.path.exists(
            f"{get_project_dir(app_name)}/models/{snake_model_name}.py"
        )

        if model_exists:
            check_and_create_folders(app_name, snake_model_name)

            create_admin_files(app_name, snake_model_name, model)
            create_forms_files(app_name, snake_model_name, model)
            create_serializers_files(app_name, snake_model_name, model)
            create_templates_files(app_name, snake_model_name, model)
            create_views_files(app_name, snake_model_name, model)
            create_viewsets_files(app_name, snake_model_name, model)
            create_urls_files(app_name)
        else:
            print(
                Exception(
                    f"A model {model} não foi encontrada, verifique a ortografia da mesma, além do diretório de pastas"  # noqa E501
                )
            )


def full_crud(app_name=None, model_name=None):
    print("Starting django-full-crud...")
    make_initial_configs()

    if model_name:
        print("Executing only one model...")
        models = [model_name]
        execute(app_name, models)
    elif app_name:
        print("Executing only one app...")
        models = get_app_models(app_name)

        execute(app_name, models)
    else:
        print("Executing all project...")
        modules = get_modules(get_project_dir())
        only_folders = get_only_folders(modules)
        only_apps = get_only_apps(only_folders)

        for module in only_apps:
            models_folder = import_module(f"{module['module_name']}.models")
            models_from_this_app = getattr(models_folder, "__all__")
            models_name = list(
                map(lambda model: model.__name__, models_from_this_app)
            )

            this_app = module["module_name"]
            execute(this_app, models_name)

    print("\nFinished django-full-crud!")
