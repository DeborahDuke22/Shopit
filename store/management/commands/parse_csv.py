import csv
import os
import decimal
from decimal import Decimal
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from store.models import Store, Category

#We use the command tools so that we gain access to our models and database connections
#https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ 


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Store.objects.all().delete()
        Category.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/store/womens_clothing.csv', newline='', encoding='mac_roman') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            category_list = []
            for row in reader:
                print(row[6])
                if row[1] not in category_list:
                    category_list.append(row[1])
                    category_object = Category.objects.create(
                        title = row[1]
                    )
                else:
                    category_object = Category.objects.get(title=row[1])
                category_object.save()

                store = Store.objects.create(
                name = row[4],
                price = Decimal(row[5]),
                category = category_object,
                image_1 = row[16],
                image_alt = row[17]
                
                )
                store.save()

          fake = Faker()

        # create some customers
        # we convert some values from tuples to strings
        for i in range(10):
            first_name = fake.first_name(),
            first_name = str(first_name[0])
            last_name = fake.last_name(),
            last_name = str(last_name[0])
            username = first_name + last_name,
            username = username[0]
            user = User.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = fake.ascii_free_email(), 
            password = 'p@ssw0rd')
            customer = Customer.objects.get(user = user)
            customer.address = fake.address(),
            customer.address = str(customer.address[0])
            customer.save()


        print("data parsed successfully")

        