import math
import re
from collections import Counter

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

def embed(text):
    counts = Counter(tokenize(text))
    vector = [0] * len(vocab)
    for word, idx in vocab.items():
        vector[idx] = counts.get(word, 0)
    return vector

def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)

# Precompute chunk embeddings
chunk_embeddings = [embed(chunk) for chunk in chunks]

# User query
query = "What is blockchain?"
query_embedding = embed(query)

# Find best matching chunk
scores = []
for i, emb in enumerate(chunk_embeddings):
    score = cosine_similarity(query_embedding, emb)
    scores.append((score, chunks[i]))

best_match = max(scores, key=lambda x: x[0])

print("User Query:", query)
print("Most Relevant Chunk:")
print(best_match[1])
print("Similarity Score:", best_match[0])