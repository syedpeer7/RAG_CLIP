import faiss
import numpy as np

index = faiss.IndexFlatL2(512)

def add_to_index(embeddings):
    index.add(np.array(embeddings))

def search_similar(query_embedding, k=5):
    D, I = index.search(np.array([query_embedding]), k)
    return I[0], D[0]
