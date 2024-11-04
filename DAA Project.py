import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx

class TrafficGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = np.zeros((num_nodes, num_nodes))

    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight

    def warshall(self):
        closure = np.copy(self.adj_matrix)
        for k in range(self.num_nodes):
            for i in range(self.num_nodes):
                for j in range(self.num_nodes):
                    if closure[i][k] and closure[k][j]:
                        closure[i][j] = 1
        return closure

    def update_traffic(self):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.adj_matrix[i][j] > 0:
                    change = random.choice([-1, 0, 1])
                    self.adj_matrix[i][j] = max(1, self.adj_matrix[i][j] + change)

    def print_graph(self):
        print("Current Traffic Matrix:")
        print(self.adj_matrix)

    def visualize_graph(self):
        G = nx.DiGraph()
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.adj_matrix[i][j] > 0:
                    G.add_edge(i, j, weight=self.adj_matrix[i][j])
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Traffic Graph")
        plt.show()

def main():
    num_nodes = 5
    graph = TrafficGraph(num_nodes)

    edges = [(0, 1, 2), (1, 2, 3), (0, 2, 5), (2, 3, 1), (3, 4, 2), (4, 3, 1)]
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    graph.print_graph()
    graph.visualize_graph()
    closure = graph.warshall()
    print("\nTransitive Closure:")
    print(closure)

    print("\nUpdating traffic...")
    graph.update_traffic()
    graph.print_graph()
    graph.visualize_graph()
    new_closure = graph.warshall()
    print("\nNew Transitive Closure:")
    print(new_closure)

if __name__ == "__main__":
    main()
