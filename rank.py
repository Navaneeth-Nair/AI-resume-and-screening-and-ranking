from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score


model = SentenceTransformer("microsoft/mpnet-base")

def jobdescsimilarity(job_description, resume_text):
    if not resume_text:
        return [] 

    if not isinstance(job_description, str) or job_description.strip() == "":
        raise ValueError("Job description must be a non-empty string.")

    if not all(isinstance(text, str) and text.strip() for text in resume_text):
        raise ValueError("All resumes must be non-empty text strings.")

    
    all_texts = [job_description] + resume_text
    embeddings = model.encode(all_texts, convert_to_numpy=True)

    job_embedding = embeddings[0].reshape(1, -1) 
    resume_embeddings = embeddings[1:]
    
    scores = cosine_similarity(job_embedding, resume_embeddings)[0]

    
    scores_percentage = [score * 100 for score in scores]  

    
    ranked_resumes = sorted(zip(resume_text, scores_percentage), key=lambda x: x[1], reverse=True)

    return ranked_resumes, accuracy_score
