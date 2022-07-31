# Django full crud!
Esse pacote serve para você criar um CRUD das suas models de forma que os arquvos sejam criados automaticamente.

## Instalação
```shell
pip install django-full-crud
```

## Dependências
Django

## Principais funcionalidades
- Criação do arquivo admin
- Criação do arquivo de forms
- Criação dos templates (delete, detail, form e list)
- Criação dos views (create, delete, detail, list e update)
- Criação dos paths presentes no urls.py
- Criação dos arquivos inits das pastas

## Recomendações
Criar suas apps com a estrutura fornecida por esse [modelo de app](https://github.com/TimeNovaData/django_app_modelo)


## Modo de uso
Crie um arquivo .vscode na raiz do seu projeto, depois adicione um arquivo chamado django_full_crud.json.

Adicione o seguinte conteudo no mesmo:
```json
{
    "project_name": "nome_do_seu_projeto"
}
```

Depois disso você precisa criar suas models dentro da pasta models e adiciona-las no init.py.
As seguintes variações de comandos podem ser executadas no terminal:

---
```shell
python manage.py full_crud nome_app NomeModel
```
O full crud é executado em cima da model especificada

---
```shell
python manage.py full_crud nome_app
```
O full crud é executado em cima da app especificada

---
```shell
python manage.py full_crud
```
O full crud é executado em cima do projeto inteiro
