import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir


def create_forms_files(app_name, snake_model_name, model_name):
    form_script = scripts.form_script(model_name)
    with open(f"{get_project_dir(app_name)}/forms/{snake_model_name}_form.py", "w", encoding="utf-8") as form:
        form.write(form_script)

    init_script = scripts.init_script(app_name, "forms")
    with open(f"{get_project_dir(app_name)}/forms/__init__.py", "w", encoding="utf-8") as init:
        init.write(init_script)
