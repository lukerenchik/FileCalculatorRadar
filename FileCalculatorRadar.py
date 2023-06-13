import os, os.path
import datetime
from time import *


#Function Used to Count Number of Each Date
def countX(list, unique):
    return list.count(unique)


#Formatting Dates for Printing to Console
def dateformat(date):
    dt = datetime.datetime.strptime(date, '%Y%m%d').strftime('%m/%d/%y')
    return dt

#Initializing Variables
path = "D:/"
date_list = []
print_dates = []

#Pulling Date data from HDD
for f in os.listdir(path=path):
    name, ext = os.path.splitext(f)
    if ext == '.mf4':
        date_list.append(str(f[8:16]))


#Isolating Unique File Dates
unique_dates = set(date_list)
unique_dates = sorted(unique_dates)

for i in unique_dates:
    print('{} has {} files, {} Hours'.format(dateformat(i), countX(list=date_list, unique = i), countX(list=date_list, unique = i)/12 ))
    

input('Press ENTER to exit')