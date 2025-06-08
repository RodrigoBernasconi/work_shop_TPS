import networkx as nx
import matplotlib.pyplot as plt
import sys
import random

def matrix_to_graph(dists):
    n = len(dists)
    G = nx.complete_graph(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                G[i][j]['weight'] = dists[i][j]
    return G

def plot_graph_step(G, tour, current_node, pos): 
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)

    edges_labels = nx.get_edge_attributes(G, name='weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels)

    plt.pause(0.5)

def calculate_tour_cost(G, tour):
    return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

def nearest_neighbor_tsp(G, start_node=0):
    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited = set(G.nodes)
    unvisited.remove(start_node)
    tour = [start_node]
    current_node = start_node

    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        current_node = next_node
        plot_graph_step(G, tour, current_node, pos)
    
    tour.append(start_node)
    plot_graph_step(G, tour, current_node, pos)

    tour_cost = calculate_tour_cost(G, tour)

    print(f"{' Vizinho + proximo ':-^40}")
    print(f"Custo: {tour_cost} | Caminho: {' -> '.join(map(str, tour))}")

    plt.ioff()
    plt.show()

def read_distances(filename):
    dists = []
    with open(filename, 'r') as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            dists.append(list(map(int, map(str.strip, line.split(',')))))
    return dists

def generate_distances(n):
    dists = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = random.randint(1, 99)

    return dists

def main_near_neighbor():
    arg = sys.argv[1]
    if arg.endswith('.csv'):
        dists = read_distances(arg)
    else:
        dists = generate_distances(int(arg))

    G = matrix_to_graph(dists)
    nearest_neighbor_tsp(G, start_node=0)

# Exemplo de uso com a mesma matriz do Held-Karp
if __name__ == "__main__":
    # Exemplo: mesma matriz usada no Held-Karp
    dists = [
        [0, 31, 46, 22, 34, 77, 61],
        [31, 0, 68, 16, 42, 94, 58],
        [46, 68, 0, 52, 83, 62, 60],
        [22, 16, 52, 0, 30, 92, 92],
        [34, 42, 83, 30, 0, 12, 21],
        [77, 94, 62, 92, 12, 0, 77],
        [61, 58, 60, 92, 21, 77, 0]
    ]

    G = matrix_to_graph(dists)
    nearest_neighbor_tsp(G, start_node=0)