from basic import * 
import numpy as np  

trigram_counts = np.zeros((vocab_size, vocab_size, vocab_size))

for i in range(len(corpus_indices) - 2):
    w1, w2, w3 = corpus_indices[i], corpus_indices[i+1], corpus_indices[i+2]
    trigram_counts[w1, w2, w3] += 1


trigram_counts += 0.01


trigram_probabilities = trigram_counts / trigram_counts.sum(axis=2, keepdims=True)

#print("Bigram probabilities matrix: ", bigram_probabilities)

def predict_next_word(w1, w2, trigram_probabilities):
    i1, i2 = word_to_idx[w1], word_to_idx[w2]
    probs = trigram_probabilities[i1, i2]
    next_idx = np.random.choice(range(vocab_size), p=probs)
    return idx_to_word[next_idx]

def generate_sentence(w1, w2, trigram_probabilities, length=10):
    sentence = [w1, w2]
    for _ in range(length):
        next_word = predict_next_word(w1, w2, trigram_probabilities)
        sentence.append(next_word)
        w1, w2 = w2, next_word  
    return ' '.join(sentence)


def top_predictions(w1, w2, trigram_probabilities, n=5):
    i1, i2 = word_to_idx[w1], word_to_idx[w2]
    probs = trigram_probabilities[i1, i2]
    top_indices = np.argsort(probs)[::-1][:n]
    return [(idx_to_word[i], probs[i]) for i in top_indices]

# TEST
start_w1, start_w2 = "artificial", "intelligence"

print("Top 5 predicciones para ('artificial', 'intelligence'):")
for word, prob in top_predictions(start_w1, start_w2, trigram_probabilities):
    print(f"{word}: {prob:.3f}")

print("\nOracion generada:")
print(generate_sentence(start_w1, start_w2, trigram_probabilities, length=10))
