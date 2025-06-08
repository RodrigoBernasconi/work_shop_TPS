"""
Algoritmo para percorrer o arquivo .csv designado e calcular a rota mais curta
Puxar e apresentar os resultados de Held-Karp e Vizinho Mais Próximo
"""
from Held_Karp import *
from vizinho_proximo import *

if __name__ == "__main__":
    main_held_karp()
    print()
    main_near_neighbor()