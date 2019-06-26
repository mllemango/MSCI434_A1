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
    WH_Cost = []
    with open('WH.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            WHs.append(row[0])
            WH_cap.append(row[1])
            WH_Cost.append(row[2])
    # print(WHs)
    # print(WH_cap)
    # print(WH_Cost)
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
    tij = m.addVars(plants, WHs, vtype=GRB.INTEGER)  # number of goods from plant i to WH j
    Wj = m.addVars(WHs, vtype=GRB.BINARY)  # 1 if warehouse j operates
    Cjk = m.addVars(WHs, custs, vtype=GRB.INTEGER)  # number of goods from WH j to cust k

    # constants
    dij = plant_WH_distance
    djk = WH_cust_distance
    Cj = WH_Cost
    Ci = plant_cost
    Wpj = WH_cap
    Cdk = cust_demand
    Pci = plant_cap  # [1500, 1500]

    # objective function
    print((i for i in plant))
    '''
    m.setObjective(quicksum(quicksum(tij[(i, j)] * dij[(i, j)] for i in plants) for j in WHs) * COST_KM +
                   quicksum(Wj[j] * Cj[j] for j in range(W)) +
                   quicksum(quicksum(Cjk[j, k] * djk[j, k] for j in range(W)) for k in range(C)) +
                   quicksum(Ci[i] for i in range(P)), GRB.MINIMIZE)  # last summation is a constant

    # constraints
    # Plant constraints
    for i in range(P):
        m.addConstr(quicksum(tij[i, j] for j in range(W) <= Pci[i]))  # goods going out of plant i does not go over plant capacity
    # WH constraints --> 1 constraint for each WH
    for j in range(W):
        # m.addConstr(quicksum(tij[i, j] for i in range(P)) <= Wpj[j])  # WH goods do not exceed capcity
        m.addConstr(quicksum(tij[i, j] for i in range(P)) == quicksum(Cjk[j, k] for k in range(C)))  # goods going into WH = goods going out of WH
    # Customer demand
    for k in range(C):
        m.addConstr(quicksum(Cjk[j, k] for j in range(W)) == Cdk[k])  # demand is met for Cust K
    # Operations
    for j in range(W):
        m.addConstr(Wj[j] * Wpj[j] - quicksum(tij[i, j] for i in range(P)) >= 0)  # if WH j is not operating, nothing goes out of it

    m.update()
    #m.optimize()

    # printing output
    #print('Min Cost', m.objVal)

    '''


if __name__ == "__main__":
    # cost per kilometer
    COST_KM = 187

    plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance = info()
    optimize(plants, WHs, custs, plant_cap, plant_cost, WH_cap, WH_Cost, cust_demand, plant_WH_distance, WH_cust_distance)
