class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, 
    # and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
# Best-first search
def best_first_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': Heuristic ('+ str(heuristics.get(current_node.name)) + ") Actual(" + str(current_node.g)+")")
                current_node = current_node.parent
            path.append(start_node.name + ': Heuristic ('+ str(heuristics.get(current_node.name)) + ") Actual(" + str(start_node.g)+")")
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate cost to goal
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('GT Pasteur', 'Kawah Putih', 56)
    graph.connect('GT Pasteur', 'Kampung Gajah', 11)
    graph.connect('Kawah Putih', 'Alun-alun Bandung', 47)
    graph.connect('Kampung Gajah', 'Kawah Putih', 60)
    graph.connect('Kampung Gajah', 'Alun-alun Bandung', 12)
    graph.connect('Kampung Gajah', 'Gedung Sate', 11)
    graph.connect('Alun-alun Bandung', 'Gedung Sate', 3)
    graph.connect('Alun-alun Bandung', 'Kampung Tulip', 9)
    graph.connect('Alun-alun Bandung', 'Saung Udjo', 7)
    graph.connect('Gedung Sate', 'Tebing Keraton', 11)
    graph.connect('Kampung Tulip', 'Trans Studio Mall', 7)
    graph.connect('Saung Udjo', 'Trans Studio Mall', 6)
    graph.connect('Tebing Keraton', 'Trans Studio Mall', 18)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['GT Pasteur'] = 274
    heuristics['Kawah Putih'] = 288
    heuristics['Kampung Gajah'] = 261
    heuristics['Alun-alun Bandung'] = 169
    heuristics['Gedung Sate'] = 143
    heuristics['Kampung Tulip'] = 170
    heuristics['Saung Udjo'] = 82
    heuristics['Tebing Keraton'] = 81
    heuristics['Trans Studio Mall'] = 0

    # Menu
    print("=============Program Greedy Best-First Search Algorithm============")
    print("Masukan Asal dan Tujuan: ")
    kota_awal = int(input())
    
    if kota_awal == 1:
      awal = "GT Pasteur"
    elif kota_awal == 2:
      awal = "Kawah Putih"
    elif kota_awal == 3:
      awal = "Kampung Gajah"
    elif kota_awal == 4:
      awal = "Gedung Sate"
    elif kota_awal == 5:
      awal = "Alun-Alun Bandung"
    elif kota_awal == 6:
      awal = "Kampung Tulip"
    elif kota_awal == 7:
      awal = "Saung Udjo"
    elif kota_awal == 8:
      awal = "Tebing Keraton"
    elif kota_awal == 9:
      awal = "Trans Studio Mall"
      
    kota_tujuan = int(input())
    if kota_tujuan == 1:
      tujuan = "GT Pasteur"
    elif kota_tujuan == 2:
      tujuan = "Kawah Putih"
    elif kota_tujuan == 3:
      tujuan = "Kampung Gajah"
    elif kota_tujuan == 4:
      tujuan = "Gedung Sate"
    elif kota_tujuan == 5:
      tujuan = "Alun-alun Bandung"
    elif kota_tujuan == 6:
      tujuan = "Kampung Tulip"
    elif kota_tujuan == 7:
      tujuan = "Saung Udjo"
    elif kota_tujuan == 8:
      tujuan = "Tebing Keraton"
    elif kota_tujuan == 9:
      tujuan = "Trans Studio Mall"

    

    # Run search algorithm 
    print("\nMenampilkan Jalur, Nilai Heuristic dan Actual Cost")
    path = best_first_search(graph, heuristics, awal, tujuan)
    print(path)

# Tell python to run main method
if __name__ == "__main__": main()
print('\n')