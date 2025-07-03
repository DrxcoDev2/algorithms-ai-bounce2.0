import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from basic import *
from model import trigram_probabilities, vocab, word_to_idx

fixed_word = 'la'

if fixed_word not in word_to_idx:
    print(f"'{fixed_word}' no est� en el vocabulario.")
    exit()

fixed_idx = word_to_idx[fixed_word]
matrix = trigram_probabilities[fixed_idx]

print("Forma de la matriz 2D:", matrix.shape)

plt.figure(figsize=(12, 10))
sns.heatmap(matrix, xticklabels=vocab, yticklabels=vocab, cmap="viridis")
plt.title(f"Matriz de Probabilidades de Trigramas (fijo: '{fixed_word}')")
plt.xlabel("Siguiente palabra")
plt.ylabel("Palabra anterior")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
