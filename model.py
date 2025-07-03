from basic import *
import numpy as np
import random

# Matriz de trigramas
trigram_counts = np.zeros((vocab_size, vocab_size, vocab_size))

for i in range(len(corpus_indices) - 2):
    w1, w2, w3 = corpus_indices[i], corpus_indices[i + 1], corpus_indices[i + 2]
    trigram_counts[w1, w2, w3] += 1

# Suavizado
trigram_counts += 0.01

# Probabilidades condicionales
trigram_probabilities = trigram_counts / trigram_counts.sum(axis=2, keepdims=True)

# Funciones
def safe_word_to_idx(word):
    return word_to_idx[word] if word in word_to_idx else word_to_idx['<UNK>']

def predict_next_word(w1, w2, trigram_probabilities):
    i1, i2 = safe_word_to_idx(w1), safe_word_to_idx(w2)
    probs = trigram_probabilities[i1, i2].copy()

    unk_idx = word_to_idx['<UNK>']
    probs[unk_idx] = 0
    total = probs.sum()
    if total == 0:
        probs = np.ones_like(probs) / len(probs)
    else:
        probs /= total

    next_idx = np.random.choice(range(vocab_size), p=probs)
    return idx_to_word[next_idx]

def generate_sentence(w1, w2, trigram_probabilities, length=10):
    sentence = [w1, w2]
    for _ in range(length):
        next_word = predict_next_word(w1, w2, trigram_probabilities)
        sentence.append(next_word)
        w1, w2 = w2, next_word
    return ' '.join(sentence)


bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
unique_bigrams = list(dict.fromkeys(bigrams))

# Tomar hasta 10 bigramas
if len(unique_bigrams) > 10:
    start_pairs = random.sample(unique_bigrams, 10)
else:
    start_pairs = unique_bigrams

# Generar texto para cada par
for i, (w1, w2) in enumerate(start_pairs, 1):
    print(f"\n[{i}] Generando texto iniciando con: ('{w1}', '{w2}')")
    sentence = generate_sentence(w1, w2, trigram_probabilities, length=10)
    print(sentence)



__all__ = ["trigram_probabilities", "vocab", "word_to_idx"]
