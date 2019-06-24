from gurobipy import *
import csv

# porting in the static data

# plants
plants = ['Cambridge', 'Barrie']
plant_cap = [1500, 1500]
plant_cost = [288.00, 476.00]

# warehouses
WHs = []
WH_cap = []
WH_cost = []
with open('WH.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        WHs.append(row[0])
        WH_cap.append(row[1])
        WH_cost.append(row[2])
print(WH_cost)
