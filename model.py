import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_influencers(brand_niche):
    data = pd.read_csv("data.csv")

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data["niche"].tolist() + [brand_niche])

    similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    data["score"] = similarity * data["engagement_rate"]

    return data.sort_values("score", ascending=False)[["name", "score"]].to_dict(orient="records")
