import networkx as nx
import matplotlib.pyplot as plt

n = 22
p = 0.23

# Генерация графа
G = nx.erdos_renyi_graph(n, p)

# Средняя степень вершины (по определению)
avg_degree_empirical = sum(dict(G.degree()).values()) / n
# Теоретическая средняя степень
avg_degree_theoretical = (n - 1) * p

print(f"Эмпирическая средняя степень: {avg_degree_empirical:.2f}")
print(f"Теоретическая средняя степень: {avg_degree_theoretical:.2f}")

# Визуализация графа
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Граф Эрдёша–Реньи")
plt.show()