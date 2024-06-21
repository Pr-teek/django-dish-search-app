import csv
import ast
import re
from django.core.management.base import BaseCommand
from dishes.models import Dish
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Import dishes from CSV file"

    def handle(self, *args, **options):
        with open("restaurants_small.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    items = ast.literal_eval(row["items"])
                    for dish_name, price in items.items():
                        try:
                            price_value = float(
                                re.sub(r"\s*onwards\s*$", "", price)
                                .strip()
                                .replace("$", "")
                                .replace(" ", "")
                            )
                            try:
                                dish, created = Dish.objects.update_or_create(
                                    name=dish_name,
                                    restaurant=row["name"],
                                    defaults={"price": price_value},
                                )
                                if created:
                                    self.stdout.write(
                                        self.style.SUCCESS(f"Created: {dish}")
                                    )
                                else:
                                    self.stdout.write(
                                        self.style.WARNING(f"Updated: {dish}")
                                    )
                            except IntegrityError:
                                self.stdout.write(
                                    self.style.WARNING(
                                        f"Duplicate dish '{dish_name}' for restaurant '{row['name']}' - skipping"
                                    )
                                )
                        except ValueError:
                            self.stdout.write(
                                self.style.WARNING(
                                    f"Skipping dish '{dish_name}' due to invalid price: {price}"
                                )
                            )
                except (SyntaxError, ValueError):
                    self.stdout.write(
                        self.style.WARNING(
                            f"Skipping restaurant '{row['name']}' due to invalid items data"
                        )
                    )

        self.stdout.write(self.style.SUCCESS("Successfully imported dishes"))
