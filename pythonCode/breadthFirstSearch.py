# Breadth-First Search Application
from collections import deque
#First Creat the Directed Graph
graph = dict()
graph["you"] = ["Alice", "Bob", "Claire", "Jim"]
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Claire"] = ["Thom","Jonny"]
graph["Peggy"] = []
graph["Anuj"] = []
graph["Thom"] = []
graph["Jonny"] = []
graph["Jim"] = []

def mango_seller(name):
    if name[-1] == "x":
        return True

# BFS Application Realization
def BFSApp(name):
    search_queue = deque()
    search_queue += graph[name]
    searched_list = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched_list:
            if mango_seller(person):
                print person + " is a mango seller!"
                return True
            else:
                search_queue += graph[person]
            searched_list.append(person)
    print "No one is a mango seller!"
    return False

#Main Function
BFSApp("you")
