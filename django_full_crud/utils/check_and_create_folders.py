import os
from functools import partial

from django_full_crud.globals.main import get_project_dir
import django_full_crud.scripts as scripts


def check_and_create_directories(app_name, directory):
    path_exists = os.path.exists(f"{get_project_dir(app_name)}/{directory}")
    if not path_exists:
        os.makedirs(f"{get_project_dir(app_name)}/{directory}")

        if not "templates" in directory:
            blank_init_script = scripts.blank_init_script()
            with open(f"{get_project_dir(app_name)}/{directory}/__init__.py", "w", encoding="utf-8") as init:
                init.write(blank_init_script)


def check_and_create_folders(app_name, snake_model_name):
    directories = [
        "admin",
        "forms",
        f"templates/{app_name}/{snake_model_name}",
        "serializers",
        "views",
        f"views/{snake_model_name}",
        "viewsets",
    ]

    partial_check_and_create_directories = partial(
        check_and_create_directories, app_name
    )
    list(map(partial_check_and_create_directories, directories))
