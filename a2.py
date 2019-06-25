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

    # print(plant_WH_distance[('Ottawa', 'Barrie')])

    WH_cust_distance = {}
    with open('WH_cust_distance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            cust = line[0]
            WH = line[1]
            dist = line[2]
            WH_cust_distance[(cust, WH)] = dist

    # print(WH_cust_distance[('Greater Sudbury', 'London')])
    return plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance


def optimize(plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance):
    m = Model()

    # creating variables
    P = len(plants)
    W = len(WHs)
    C = len(custs)
    tij = m.addVars(P, W, vtype=GRB.INTEGER)  # number of goods from plant i to WH j
    Wj = m.addVars(W, vtype=GRB.BINARY)  # 1 if warehouse j operates
    Cjk = m.addVars(W, C, vtype=GRB.INTEGER)  # number of goods from WH j to cust k

    # constants
    dij = plant_WH_distance
    djk = WH_cust_distance
    Cj = WH_cost
    Ci = plant_cost
    Wpj = WH_cap

    # objective function
    m.setObjective(quicksum(quicksum(tij[i, j] * dij[i, j] for i in range(P)) for j in range(W)) * COST_KM +
                   quicksum(Wj[j] * Cj[j] for j in range(W)) +
                   quicksum(quicsum(Cjk * djk for j in range(W)) for k in range(C)) +
                   quicksum(Ci for i in range(P)), GRB.MINIMIZE)

    # constraints
    for j in range(W):
        m.addConstr(quicksum(tij for i in range(P)) <= Wpj[j])
        m.addContr()


if __name__ == "__main__":
    # cost per kilometer
    COST_KM = 187

    plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance = info()
    optimize(plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance)
