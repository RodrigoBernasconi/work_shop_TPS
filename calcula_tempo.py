import math
import pandas as pd

# Função para formatar tempo em uma unidade legível
def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.6f} s"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} min"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} h"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} dias"
    years = days / 365
    return f"{years:.2f} anos"

# Lista de valores de n
valores_n = list(range(5, 61, 5))

# Lista para armazenar os dados
dados = []

# Para cada valor de n, calcule as operações e tempo estimado
for n in valores_n:
    operacoes = (n ** 2) * (2 ** n)
    tempo_segundos = operacoes / 1_000_000_000
    dados.append({
        "n": n,
        "operações": f"{operacoes:,}",
        "tempo estimado": format_time(tempo_segundos)
    })

# Criar um DataFrame e exibir a tabela
df = pd.DataFrame(dados)
print(df.to_string(index=False))
