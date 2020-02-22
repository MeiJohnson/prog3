import csv
import json

"""
Царулкова Анастасия Витальевна
2 группа 3 подгруппа

Copyright: 10.2019

Задание 3.3 ИСР
Cкрипт, который создает csv-файл с данными.

"""


with open('MOCKDATA.json') as f:
    data_dict = json.load(f)

with open('eggs.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    jsonwriter.writerow(data_dict[0].keys())
    keys = data_dict[0].keys()
    for el in data_dict:
        jsonwriter.writerow(el.values())
print("Файл записан")
