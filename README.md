# Held-Karp
Algoritmo exato, retorna o caminho ótimo(com menor custo) e retorna o caminho que foi feito.

O algoritmo de Held-Karp divide em subproblemas e vai percorrer, resolver e combinar esses subproblemas, apresentando assim a melhor opção de caminho, ele faz isso de forma dinâmica, sendo mais rápido do que um algoritmo de força bruta, que permuta todos os caminhos.

# Vizinho mais próximo
Algoritmo Heurístico(Guloso), retorna uma aproximação(não ótimo), também retorna o caminho que foi feito e o seu custo.

O algoritmo de vizinho mais próximo funciona de maneira gulosa, vai ir pelo menor valor que ele encontrar primeiro, sem se importar se isso será a melhor decisão a ser tomada no final das contas.

## percorrer_tps.py
Algoritmo auxiliar para rodar os dois casos citados anteriormente, para rodar a aplicação está sendo usado os arquivos .csv que o n escolhido, para rodar o programa, no terminal digite: **python percorrer_tps.py ex_n5.csv**

Dessa forma teremos ambos os algortimos rodando com os mesmo valores e pesos em cada vértice e aresta.


## Apresentação dos conceitos dos conteúdos abordados
- Apresentação de Slides: https://www.canva.com/design/DAGpiXCs8Kg/wY6c4RsrG0GCNRhWHuJxZA/edit?utm_content=DAGpiXCs8Kg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
