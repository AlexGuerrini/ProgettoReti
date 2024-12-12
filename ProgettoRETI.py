import sys
from prettytable import PrettyTable

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors= set()
        self.routing_table = dict()
        
    def add_neighbor(self, neighbor, distance):
        self.neighbors.add(neighbor)
        self.routing_table[neighbor] = [distance,neighbor]

    def update_routing_table(self):
        updated = False
        for neighbor in self.neighbors:
            for dest, via in neighbor.routing_table.items():
                if dest != self:
                    new_distance = self.routing_table[neighbor][0] + via[0]
                    if dest not in self.routing_table or new_distance < self.routing_table[dest][0]:
                        self.routing_table[dest] = (new_distance, self.routing_table[neighbor][1])
                        updated = True
        return updated
    
    def __repr__(self):
        return self.name

def print_routing_tables(nodes):
    for node in nodes:
        table = PrettyTable()
        table.field_names = ["Destinazione", "Distanza", "Gateway"]
        for dest, (distance, gateway) in node.routing_table.items():
            table.add_row([dest, distance, gateway])
        print(f"Tabella di routing del nodo {node.name}:")
        print(table)
        print("\n")

def distance_vector_routing():

    print_routing_tables(nodes)
    iteration = 0
    while True:
        print(f"Iterazione {iteration + 1}:")
        updated = False
        for node in nodes:
            if node.update_routing_table():
                updated = True
        print_routing_tables(nodes)
        if not updated:
            break
        iteration += 1


#GENERAZIONE DEI NODI

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.add_neighbor(B, 1)
A.add_neighbor(D, 4)

B.add_neighbor(A, 1)
B.add_neighbor(C, 2)

C.add_neighbor(B, 2)
C.add_neighbor(D, 3)

D.add_neighbor(A, 4)
D.add_neighbor(C, 3)

nodes = []
nodes.append(A)
nodes.append(B)
nodes.append(C)
nodes.append(D)

distance_vector_routing()
