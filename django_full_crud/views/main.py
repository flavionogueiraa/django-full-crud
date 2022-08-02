import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir


def create_views_files(app_name, snake_model_name, model_name):
    view_path = f"{get_project_dir(app_name)}/views/"
    model_path = view_path + f"{snake_model_name}/"

    create_view_script = scripts.create_view_script(
        app_name, model_name, snake_model_name
    )
    with open(f"{model_path}{snake_model_name}_create_view.py", "w", encoding="utf-8") as create_view:
        create_view.write(create_view_script)

    delete_view_script = scripts.delete_view_script(
        app_name, model_name, snake_model_name
    )
    with open(f"{model_path}{snake_model_name}_delete_view.py", "w", encoding="utf-8") as delete_view:
        delete_view.write(delete_view_script)

    detail_view_script = scripts.detail_view_script(
        app_name, model_name, snake_model_name
    )
    with open(f"{model_path}{snake_model_name}_detail_view.py", "w", encoding="utf-8") as detail_view:
        detail_view.write(detail_view_script)

    list_view_script = scripts.list_view_script(app_name, model_name, snake_model_name)
    with open(f"{model_path}{snake_model_name}_list_view.py", "w", encoding="utf-8") as list_view:
        list_view.write(list_view_script)

    update_view_script = scripts.update_view_script(
        app_name, model_name, snake_model_name
    )
    with open(f"{model_path}{snake_model_name}_update_view.py", "w", encoding="utf-8") as update_view:
        update_view.write(update_view_script)

    deep_init = scripts.init_script(app_name, f"views\\{snake_model_name}")
    with open(f"{model_path}__init__.py", "w", encoding="utf-8") as init:
        init.write(deep_init)

    normal_init = scripts.init_script(app_name, "views")
    with open(f"{view_path}/__init__.py", "w", encoding="utf-8") as init:
        init.write(normal_init)
