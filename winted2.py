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
        company=row[17]
        title = row[18]
        contens= row[20]
        image=row[22]
        deadline=row[23]
        
        district = row[25]
        compensetion = row[26]
        subcategory = row[27]
        carrer = row [28]
        tag = row [31]

        if row[17] and row[18]:
           asd2 =District.objects.get(id=row[25])
           asd3=Money.objects.get(id=row[26])
           asd4=Subcategory.objects.get(id=row[27])
           asd5= Carrer.objects.get(id=row[28])
           asd6= Sub_tag.objects.get(id=row[31])
           Company.objects.create(name=company,title=title,contens=contens,image_url=image,dead_line=deadline,district=asd2,money=asd3,subcategories=asd4,carrer=asd5,sub_tag=asd6)
            
            
                    