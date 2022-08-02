from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="django_full_crud",
    version="0.2.6",
    url="https://github.com/flaviotech/django-full-crud/",
    license="MIT License",
    author="Flávio Silva",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="flavio.nogueira.profissional@gmail.com",
    keywords="Django, CRUD",
    description="Django Full CRUD",
    packages=find_packages(),
    install_requires=["django"],
    project_urls={
        "GitHub": "https://github.com/flaviotech/django-full-crud/",
    }
)
