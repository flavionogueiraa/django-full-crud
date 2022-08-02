import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir
from django_full_crud.utils import get_init_list


def create_urls_files(app_name):
    init_list = get_init_list(app_name, "views")
    urls_script = scripts.urls_script(app_name, init_list)
    with open(f"{get_project_dir(app_name)}/urls.py", "w", encoding="utf-8") as urls:
        urls.write(urls_script)
