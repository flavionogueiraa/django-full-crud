import django_full_crud.scripts as scripts
from django_full_crud.globals import get_django_full_crud_json
from django_full_crud.globals.main import get_project_dir
from django_full_crud.utils import get_init_list


def create_urls_files(app_name):
    if get_django_full_crud_json("make_urls"):
        print("Creating urls file...")

        view_init_list = get_init_list(app_name, "views")
        viewset_init_list = get_init_list(app_name, "viewsets")
        urls_script = scripts.urls_script(app_name, view_init_list, viewset_init_list)
        with open(
            f"{get_project_dir(app_name)}/urls.py", "w", encoding="utf-8"
        ) as urls:
            urls.write(urls_script)

        print("Urls file created successfully!")
    else:
        print("Skipping urls file...")
        print("Successfully skipped urls file!")
