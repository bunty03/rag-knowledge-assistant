import math
import re
from collections import Counter

# Chunks from Step 3 (you already have these conceptually)
chunks = [
    "Blockchain is an advanced database mechanism",
    "Cryptocurrency is a digital currency using encryption",
    "Bitcoin uses blockchain technology",
    "Ethereum supports smart contracts",
    "Solana focuses on scalability"
]

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

# Build vocabulary
vocab = {}
for chunk in chunks:
    for word in tokenize(chunk):
        if word not in vocab:
            vocab[word] = len(vocab)

# Create embeddings (Bag of Words)
embeddings = []
for chunk in chunks:
    counts = Counter(tokenize(chunk))
    vector = [0] * len(vocab)
    for word, idx in vocab.items():
        vector[idx] = counts.get(word, 0)
    embeddings.append(vector)

print("Total chunks:", len(embeddings))
print("Embedding vector size:", len(embeddings[0]))
print("Sample embedding (first 10 values):")
print(embeddings[0][:10])