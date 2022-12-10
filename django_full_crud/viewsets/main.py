import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir


def create_viewsets_files(app_name, snake_model_name, model_name):
    viewset_script = scripts.viewset_script(app_name, model_name)
    with open(f"{get_project_dir(app_name)}/viewsets/{snake_model_name}_viewset.py", "w", encoding="utf-8") as viewset:
        viewset.write(viewset_script)

    init_script = scripts.init_script(app_name, "viewsets")
    with open(f"{get_project_dir(app_name)}/viewsets/__init__.py", "w", encoding="utf-8") as init:
        init.write(init_script)
