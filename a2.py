from gurobipy import *
import csv

def info():
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

    # customers
    custs = []
    cust_demand = []
    with open('cust.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            custs.append(row[0])
            cust_demand.append(row[1])
    # print(custs)
    # print(cust_demand)

    # distances
    plant_WH_distance = {}
    with open('plant_WH_distance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            WH = line[0]
            plant = line[1]
            dist = line[2]
            plant_WH_distance[(WH, plant)] = dist

    print(plant_WH_distance[('Ottawa', 'Barrie')])

    WH_cust_distance = {}
    with open('WH_cust_distance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            cust = line[0]
            WH = line[1]
            dist = line[2]
            WH_cust_distance[(cust, WH)] = dist

    print(WH_cust_distance[('Greater Sudbury', 'London')])

def optimize():
    m = Model()

    # creating variables
    # x = m.addVars(n,n, vtype=GRB.BINARY)


if __name__ == "__main__":
    # cost per kilometer
    COST_KM = 187

    info()
