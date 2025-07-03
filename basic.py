import numpy as np
from collections import Counter

# Ingreso del corpus
corpus = input("Introduce el corpus: ")

# Preprocesado
words = corpus.lower().split()

# Vocabulario limitado a las 500 palabras más comunes + <UNK>
word_counts = Counter(words)
most_common_500 = [word for word, _ in word_counts.most_common(500)]

if '<UNK>' not in most_common_500:
    vocab = most_common_500 + ['<UNK>']
else:
    vocab = most_common_500

vocab_size = len(vocab)

print(f"Vocabulary: {vocab}")
print(f"Vocabulary size: {vocab_size}")

# Mapas palabra-índice e índice-palabra
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

# Función segura
def word_to_index(word):
    return word_to_idx[word] if word in word_to_idx else word_to_idx['<UNK>']

# Convertir corpus a índices
corpus_indices = [word_to_index(w) for w in words]
