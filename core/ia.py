import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from basic import *
from model import trigram_probabilities, vocab, word_to_idx, idx_to_word

def safe_word(word):
    return word if word in word_to_idx else '<UNK>'

def predict_next_word(w1, w2, trigram_probabilities):
    i1, i2 = word_to_idx[safe_word(w1)], word_to_idx[safe_word(w2)]
    probs = trigram_probabilities[i1, i2].copy()
    probs[word_to_idx['<UNK>']] = 0

    total = probs.sum()
    if total == 0:
        probs = np.ones_like(probs) / len(probs)
    else:
        probs /= total

    next_idx = np.random.choice(len(probs), p=probs)
    return idx_to_word[next_idx]

def generate_from_prompt(prompt, length=15):
    tokens = prompt.lower().split()
    if len(tokens) < 2:
        print("❌ Escribe al menos 2 palabras para el prompt.")
        return ""

    w1, w2 = tokens[0], tokens[1]
    sentence = [w1, w2]

    for _ in range(length):
        next_word = predict_next_word(w1, w2, trigram_probabilities)
        sentence.append(next_word)
        w1, w2 = w2, next_word

    return ' '.join(sentence)

if __name__ == "__main__":
    prompt = input("Escribe un prompt (al menos 2 palabras):\n> ")
    print("\nTexto generado:\n")
    print(generate_from_prompt(prompt))
