# This is a DijkstraAlogrithm for Directed Map without loop

infinity = float("inf")
Map = {}

Map["start"] = {}
Map["start"]["A"] = 5
Map["start"]["B"] = 2

Map["A"] = {}
Map["A"]["C"] = 4
Map["A"]["D"] = 2

Map["B"] = {}
Map["B"]["A"] = 8
Map["B"]["D"] = 7

Map["C"] = {}
Map["C"]["D"] = 6
Map["C"]["final"] = 3

Map["D"] = {}
Map["D"]["final"] = 1

Map["final"] = {}

costs = {}
costs["A"] = 5
costs["B"] = 2
costs["C"] = infinity
costs["D"] = infinity
costs["final"] = infinity

parent = {}
parent["A"] = "start"
parent["B"] = "start"
parent["C"] = None
parent["D"] = None
parent["final"] = None

processedNodes = []
def NodeForMinCost(cost):
    bestNode = None
    costForBest = infinity
    for node in cost.keys():
        if cost[node] < costForBest and node not in processedNodes:
            bestNode = node
            costForBest = cost[node]
    return bestNode

chosenNode = NodeForMinCost(costs)
while chosenNode:
    neighbourNodes = Map[chosenNode]
    for n in neighbourNodes.keys():
        newCost = costs[chosenNode] + neighbourNodes[n]
        if newCost <= costs[n]:
            costs[n] = newCost
            parent[n] = chosenNode
    processedNodes.append(chosenNode)
    chosenNode = NodeForMinCost(costs)

print costs["final"]