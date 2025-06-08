"""
Algoritmo exato, ou seja, vai conseguir buscar o menor valor do caminho possível
porém só é útil quando utilzado em n pequenos (recomendamos n <= 10)

Supondo que temos um computador muito potente que possa processar 1 bilhão de adições por segundo, com base nisso
observe na tabela a seguir o tempo médio que levaria para o algoritmo resolver o problema de TSP

n  | rotas por segundo | (n-1)!      | cálculo total
5  | 250 M             | 24          | insignificante
10 | 110 M             | 362 880     | 0.003 s
15 | 71 M              | 87 B        | 20 min
20 | 53 M              | 1.2 x 10^17 | 73 anos
"""

from itertools import combinations

def held_karp(dist):
    n = len(dist)
    C = {}

    # Estado base: apenas cidade 0 visitada
    for k in range(1, n):
        C[(frozenset([0, k]), k)] = (dist[0][k], [0, k])

    # Subconjuntos de tamanho 3 até n
    for s in range(3, n + 1):
        for subset in combinations(range(1, n), s - 1):
            subset = (0,) + subset
            set_frozen = frozenset(subset)

            for j in subset:
                if j == 0:
                    continue
                prev_set = set_frozen - frozenset([j])
                min_cost = float('inf')
                min_path = []
                for k in subset:
                    if k == 0 or k == j:
                        continue
                    cost, path = C[(prev_set, k)]
                    new_cost = cost + dist[k][j]
                    if new_cost < min_cost:
                        min_cost = new_cost
                        min_path = path + [j]
                C[(set_frozen, j)] = (min_cost, min_path)

    # Fechar o ciclo
    full_set = frozenset(range(n))
    min_cost = float('inf')
    min_path = []
    for j in range(1, n):
        cost, path = C[(full_set, j)]
        final_cost = cost + dist[j][0]
        if final_cost < min_cost:
            min_cost = final_cost
            min_path = path + [0]

    return min_cost, min_path

if __name__ == "__main__":
    # Matriz de distâncias entre 5 cidades (0 a 4)
    dist_matrix = [
        [0, 10, 15, 20, 10], # Vértice 0
        [10, 0, 35, 25, 30], # Vértice 1
        [15, 35, 0, 30, 20], # Vértice 2
        [20, 25, 30, 0, 15], # Vértice 3
        [10, 30, 20, 15, 0], # Vértice 4
    ]

    custo, caminho = held_karp(dist_matrix)

    print("Menor custo:", custo)
    print("Caminho ideal:", caminho)
