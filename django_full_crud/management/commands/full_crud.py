from django.core.management import BaseCommand
from django_full_crud.main import full_crud


class Command(BaseCommand):
    help = "Rode o full_crud em uma model, em uma app ou no projeto todo"

    def add_arguments(self, parser):
        parser.add_argument(
            "app",
            nargs="?",
            help="Escolha uma app para rodar o full_crud.",
        )
        parser.add_argument(
            "model",
            nargs="?",
            help="Escolha uma model para rodar o full_crud.",
        )

    def handle(self, *args, **options):
        try:
            app = options["app"]
        except:
            app = None

        try:
            model = options["model"]
        except:
            model = None

        full_crud(app, model)
