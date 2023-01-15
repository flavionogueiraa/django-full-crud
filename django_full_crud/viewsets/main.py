import django_full_crud.scripts as scripts
from django_full_crud.globals import get_django_full_crud_json, get_project_dir


def create_viewsets_files(app_name, snake_model_name, model_name):
    if get_django_full_crud_json("make_viewsets"):
        print("Creating viewset files...")

        viewset_script = scripts.viewset_script(app_name, model_name)
        with open(f"{get_project_dir(app_name)}/viewsets/{snake_model_name}_viewset.py", "w", encoding="utf-8") as viewset:
            viewset.write(viewset_script)

        if get_django_full_crud_json("make_viewsets_init"):
            init_script = scripts.init_script(app_name, "viewsets")
            with open(f"{get_project_dir(app_name)}/viewsets/__init__.py", "w", encoding="utf-8") as init:
                init.write(init_script)
        print("Viewset files created successfully!")
    else:
        print("Skipping viewset files...")
        print("Successfully skipped viewset files!")
