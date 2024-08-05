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
    try:
        return get_django_full_crud_json("project_name")
    except Exception:
        raise (
            Exception(
                "Arquivo django_full_crud.json não encontrado ou com algum erro de sintaxe, por favor, verifique a seção 'Modo de uso' da documentação."  # noqa E501
            )
        )


def get_django_full_crud_json(key, default=True):
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

    with open(path, encoding="utf-8") as settings:
        dict_json = json.load(settings)
        return dict_json.get(key, default)


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
