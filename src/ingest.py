from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('data/documents.txt', 'r') as f:
    text = f.read()

chunks = text.split('\n')

embeddings = model.encode(chunks)

os.makedirs("vector_store", exist_ok=True)

with open("vector_store/data.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + "\n")

print("Documents stored successfully in Endee (vector database)")
