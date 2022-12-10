import json
import os
import platform
from pathlib import Path

so = platform.system()


def update_current_app(app_name):
    global CURRENT_APP
    CURRENT_APP = app_name


def base_dir(name=None):
    return os.path.join(BASE_DIR, name or "")


def get_project_name():
    windows_path = os.path.join(
        PROJECT_BASE_DIR, ".vscode", "django_full_crud.json"
    )
    linux_path = os.path.join(
        PROJECT_BASE_DIR.parent, ".vscode", "django_full_crud.json"
    )

    if os.path.exists(windows_path):
        path = windows_path
    else:
        path = linux_path

    try:
        return get_django_full_crud_json(path)
    except:
        raise (
            Exception(
                "Arquivo django_full_crud.json não encontrado, por favor, verifique a seção 'Modo de uso' da documentação"
            )
        )


def get_django_full_crud_json(path):
    with open(path, encoding="utf-8") as settings:
        dict_json = json.load(settings)
        return dict_json.get("project_name", None)


def get_project_dir(string=""):
    if so == "Windows":
        return os.path.join(PROJECT_BASE_DIR, PROJECT_NAME, string)
    elif so == "Linux":
        return os.path.join(PROJECT_BASE_DIR.parent, PROJECT_NAME, string)
    else:
        raise (Exception("SO não disponível"))


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_BASE_DIR = (
    Path(__file__).resolve().parent.parent.parent.parent.parent.parent
)

PROJECT_NAME = get_project_name()

BAR = "\\" if so == "Windows" else "/"

get_project_dir()
