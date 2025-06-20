import itertools
import random
import sys

class tps_path:
    def held_karp(self, dists):
        """
        Implementation of Held-Karp, an algorithm that solves the Traveling
        Salesman Problem using dynamic programming with memoization.

        Parameters:
            dists: distance matrix

        Returns:
            A tuple, (cost, path).
        """
        n = len(dists)

        # Maps each subset of the nodes to the cost to reach that subset, as well
        # as what node it passed before reaching this subset.
        # Node subsets are represented as set bits.
        C = {}

        # Set transition cost from initial state
        for k in range(1, n):
            C[(1 << k, k)] = (dists[0][k], 0)

        # Iterate subsets of increasing length and store intermediate results
        # in classic dynamic programming manner
        for subset_size in range(2, n):
            for subset in itertools.combinations(range(1, n), subset_size):
                # Set bits for all nodes in this subset
                bits = 0
                for bit in subset:
                    bits |= 1 << bit

                # Find the lowest cost to get to this subset
                for k in subset:
                    prev = bits & ~(1 << k)

                    res = []
                    for m in subset:
                        if m == 0 or m == k:
                            continue
                        res.append((C[(prev, m)][0] + dists[m][k], m))
                    C[(bits, k)] = min(res)

        # We're interested in all bits but the least significant (the start state)
        bits = (2**n - 1) - 1

        # Calculate optimal cost
        res = []
        for k in range(1, n):
            res.append((C[(bits, k)][0] + dists[k][0], k))
        opt, parent = min(res)

        # Backtrack to find full path
        path = [0]
        for i in range(n - 1):
            path.append(parent)
            new_bits = bits & ~(1 << parent)
            _, parent = C[(bits, parent)]
            bits = new_bits

        # Add implicit start state
        path.append(0)

        return opt, list(reversed(path))

def generate_distances(n):
    dists = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = random.randint(1, 99)

    return dists

def read_distances(filename):
    dists = []
    with open(filename, 'r') as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            dists.append(list(map(int, map(str.strip, line.split(',')))))
    return dists


def main_held_karp():
    path = tps_path()
    arg = sys.argv[1]
    if arg.endswith('.csv'):
        dists = read_distances(arg)
    else:
        dists = generate_distances(int(arg))

    for i,row in enumerate(dists):
        if i == 0:
            print(f"   {'|'.join([(str(i)+'v').rjust(3, ' ') for i in range(len(row))])}")
            print(f"{i}v|{'|'.join([str(n).rjust(3, ' ') for n in row])}")
        else:
            print(f"{i}v|{'|'.join([str(n).rjust(3, ' ') for n in row])}")

    print('')
    custo, caminho = path.held_karp(dists)
    #* Exibição dos resultados
    print(f"{' Held-Karp ':-^40}")
    print(f"Custo: {custo} | Caminho: {' -> '.join(map(str, caminho))}")
    # print(f"Caminho: {' -> '.join(map(str, caminho))}")

if __name__ == '__main__':
    path = tps_path()
    arg = sys.argv[1]
    if arg.endswith('.csv'):
        dists = read_distances(arg)
    else:
        dists = generate_distances(int(arg))

    for i,row in enumerate(dists):
        if i == 0:
            print(f"   {'|'.join([(str(i)+'v').rjust(3, ' ') for i in range(len(row))])}")
            print(f"{i}v|{'|'.join([str(n).rjust(3, ' ') for n in row])}")
        else:
            print(f"{i}v|{'|'.join([str(n).rjust(3, ' ') for n in row])}")

    print('')
    print(path.held_karp(dists))