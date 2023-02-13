import django_full_crud.scripts as scripts
from django_full_crud.globals import get_django_full_crud_json, get_project_dir


def create_serializers_files(app_name, snake_model_name, model_name):
    if get_django_full_crud_json("make_serializers"):
        print("Creating serializer files...")

        serializer_script = scripts.serializer_script(model_name)
        with open(f"{get_project_dir(app_name)}/serializers/{snake_model_name}_serializer.py", "w", encoding="utf-8") as serializer:
            serializer.write(serializer_script)

        if get_django_full_crud_json("make_serializers_init"):
            init_script = scripts.init_script(app_name, "serializers")
            with open(f"{get_project_dir(app_name)}/serializers/__init__.py", "w", encoding="utf-8") as init:
                init.write(init_script)
        print("Serializer files created successfully!\n")
    else:
        print("Skipping serializer files...")
        print("Successfully skipped serializer files!\n")
