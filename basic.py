import numpy as np  

corpus = """Artificial Intelligence is the new electricity.
Machine learning is the future of AI.
AI is transforming industries and shaping the future."""

words = corpus.lower().split()

vocab = list(set(words))
vocab_size = len(vocab)


print(f"Vocabulary: {vocab}")
print(f"Vocabulary size: {vocab_size}")

word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

corpus_indices = [word_to_idx[word] for word in words]
