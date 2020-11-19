import os
import csv 
import sys 
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'winted4.settings')
django.setup()

from company.models import *
from user.models import *

CSV_PATH_PRODUCTS= 'win.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        main=Maincategory.objects.get(id=row[33])
        sub= Subcategory.objects.get(id=row[34])
        carrer =Carrer.objects.get(id=row[35])
        salary = row[36]

        if row[33] and row[34]:
            Salary.objects.create(maincategories=main , subcategories=sub , carrer=carrer , salary=salary)           
  
                            
            
                    