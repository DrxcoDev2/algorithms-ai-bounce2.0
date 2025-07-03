import matplotlib.pyplot as plt
import seaborn as sns 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from basic import *
from model import * 

plt.figure(figsize=(12, 10))
sns.heatmap(bigram_probabilities, xticklabels=vocab, yticklabels=vocab, cmap="viridis")
plt.title("Matriz de Probabilidades de Bigramas")
plt.xlabel("Siguiente palabra")
plt.ylabel("Palabra actual")
plt.savefig("bigram_matrix.png")
print("Imagen guardada como 'bigram_matrix.png'")
