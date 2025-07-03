import numpy as np  
from collections import Counter

corpus = """Artificial Intelligence is the new electricity.
Machine learning is the future of AI.
AI is transforming industries and shaping the future."""

words = corpus.lower().split()

word_counts = Counter(words)

most_common_500 = [word for word, count in word_counts.most_common(500)]

vocab = most_common_500 + ['<UNK>']
vocab_size = len(vocab)


print(f"Vocabulary: {vocab}")
print(f"Vocabulary size: {vocab_size}")

word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

def word_to_index(word):
    return word_to_idx[word] if word in word_to_idx else word_to_idx['<UNK>']


corpus_indices = [word_to_index(w) for w in words]