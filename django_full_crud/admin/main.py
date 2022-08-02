import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir


def create_admin_files(app_name, snake_model_name, model_name):
    admin_script = scripts.admin_script(app_name, snake_model_name, model_name)
    with open(f"{get_project_dir(app_name)}/admin/{snake_model_name}_admin.py", "w", encoding="utf-8") as admin:
        admin.write(admin_script)

    init_script = scripts.init_script(app_name, "admin")
    with open(f"{get_project_dir(app_name)}/admin/__init__.py", "w", encoding="utf-8") as init:
        init.write(init_script)
