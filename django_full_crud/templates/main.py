import django_full_crud.scripts as scripts
from django_full_crud.globals.main import get_project_dir
from django_full_crud.utils import get_class_info


def create_templates_files(app_name, snake_model_name, model_name):
    base_path = f"{get_project_dir(app_name)}/templates/{app_name}/{snake_model_name}/{snake_model_name}"
    class_info = get_class_info(app_name, model_name)

    with open(f"{base_path}_form.html", "w", encoding="utf-8") as form_template:
        form_template.write(scripts.form_template_script(class_info))

    with open(f"{base_path}_list.html", "w", encoding="utf-8") as list_template:
        list_template.write(scripts.list_template_script(class_info))

    with open(f"{base_path}_delete.html", "w", encoding="utf-8") as delete_template:
        delete_template.write(scripts.delete_template_script())

    with open(f"{base_path}_detail.html", "w", encoding="utf-8") as detail_template:
        detail_template.write(scripts.detail_template_script(class_info))
