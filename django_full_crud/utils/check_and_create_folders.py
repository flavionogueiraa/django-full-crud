import os
from functools import partial

from django_full_crud.globals.main import get_project_dir


def check_and_create_folder(app_name, snake_model_name, directory):
    path_exists = os.path.exists(
        f"{get_project_dir(app_name)}/{directory}/{snake_model_name}"
    )
    if not path_exists:
        os.makedirs(f"{get_project_dir(app_name)}/{directory}/{snake_model_name}")


def check_and_create_folders(app_name, snake_model_name):
    directories = [f"templates/{app_name}", "views"]
    partial_check_and_create_folder = partial(check_and_create_folder, app_name, snake_model_name)
    list(map(partial_check_and_create_folder, directories))
