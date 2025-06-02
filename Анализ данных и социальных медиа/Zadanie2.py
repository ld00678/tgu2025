import networkx as nx
import matplotlib.pyplot as plt

# Генерируем граф "горкой"
G = nx.path_graph(28)  # линейный путь даст горку центральностей

# Вычисляем меры центральности
centrality = nx.eigenvector_centrality_numpy(G)

# Отображение результатов
values = [centrality[n] for n in G.nodes()]
print("Eigenvector centrality:")
for node, val in centrality.items():
    print(f"{node}: {val:.4f}")

# Визуализация
plt.plot(list(G.nodes()), values, marker='o')
plt.title("Eigenvector centrality (горка)")
plt.xlabel("Node")
plt.ylabel("Centrality")
plt.grid(True)
plt.show()