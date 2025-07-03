from basic import * 
import numpy as np  

bigram_counts = np.zeros((vocab_size, vocab_size))

for i in range(len(corpus_indices) - 1):
    current_word = corpus_indices[i]
    next_word = corpus_indices[i + 1]
    bigram_counts[current_word, next_word] += 1

bigram_counts += 0.01

bigram_probabilities = bigram_counts / bigram_counts.sum(axis=1, keepdims=True)

#print("Bigram probabilities matrix: ", bigram_probabilities)

def predict_next_word(current_word, bigram_probabilities):
    word_idx = word_to_idx[current_word]
    next_word_probs = bigram_probabilities[word_idx]
    next_word_idx = np.random.choice(range(vocab_size), p=next_word_probs)
    return idx_to_word[next_word_idx]

def generate_sentence(start_word, bigram_probabilities, length=5):
    sentence = [start_word]
    current_word = start_word

    for _ in range(length):
        next_word = predict_next_word(current_word, bigram_probabilities)
        sentence.append(next_word)
        current_word = next_word
    
    return ' '.join(sentence)

# TEST
current_word = "ai"
next_word = predict_next_word(current_word, bigram_probabilities)
print(f"Given '{current_word}', the model predicts '{next_word}'.")

generated_sentence = generate_sentence("artificial", bigram_probabilities, length=10)
print(f"Generated sentence: {generated_sentence}")