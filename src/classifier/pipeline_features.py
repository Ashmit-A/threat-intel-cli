import numpy as np
from src.classifier.embeddings import generate_embedding

def build_embedding_matrix(texts):

    return np.array([generate_embedding(t) for t in texts])