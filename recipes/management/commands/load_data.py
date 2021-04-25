from django.core.management.base import BaseCommand, CommandError
from recipes.models import Ingredient, Tag
import csv

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                # do something with row data.
                name, dimension = row
                Ingredient.objects.get_or_create(name=name, dimension=dimension)
                # print(name + ', ' + unit)

Tag.objects.get_or_create(title='Завтрак', display_name='Завтрак', color='orange')
Tag.objects.get_or_create(title='Обед', display_name='Обед', color='green')
Tag.objects.get_or_create(title='Ужин', display_name='Ужин', color='purple')