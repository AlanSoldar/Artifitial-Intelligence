import gradiente
import csv

with open('house_prices_train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)