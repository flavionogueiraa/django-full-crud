import django_full_crud.scripts as scripts
from django_full_crud.globals import get_django_full_crud_json, get_project_dir


def create_admin_files(app_name, snake_model_name, model_name):
    if get_django_full_crud_json("make_admins"):
        print("Creating admin files...")

        admin_script = scripts.admin_script(app_name, snake_model_name, model_name)
        with open(f"{get_project_dir(app_name)}/admin/{snake_model_name}_admin.py", "w", encoding="utf-8") as admin:
            admin.write(admin_script)

        if get_django_full_crud_json("make_admins_init"):
            init_script = scripts.init_script(app_name, "admin")
            with open(f"{get_project_dir(app_name)}/admin/__init__.py", "w", encoding="utf-8") as init:
                init.write(init_script)

        print("Admin files created successfully!\n")
    else:
        print("Skipping admin files...")
        print("Successfully skipped admin files!\n")
