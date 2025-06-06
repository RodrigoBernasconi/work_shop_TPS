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