from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("vector_store/data.txt", "r") as f:
    documents = f.readlines()

doc_embeddings = model.encode(documents)

def search(query):
    query_embedding = model.encode([query])
    scores = np.dot(doc_embeddings, query_embedding.T)
    best_match = documents[np.argmax(scores)]
    return best_match
