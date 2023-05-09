from re import I
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from .local_data import category
from .data_matrix import places
from sklearn.feature_extraction.text import TfidfVectorizer
import ast



def recommend_places(place_attributes, user_preferences, k=5):
    vectorizer = TfidfVectorizer(analyzer=lambda x: x)

    tfidf_matrix = vectorizer.fit_transform(place_attributes.values())

    user_pref_matrix = vectorizer.transform([user_preferences])

    cosine_similarities = cosine_similarity(user_pref_matrix, tfidf_matrix).flatten()

    indices = cosine_similarities.argsort()[::-1][:k]
    recommendations = [list(place_attributes.keys())[i] for i in indices]

    return recommendations

def matching_algo(user_likes):

    attributes = ['Food', 'Entertainment', 'Cultural & Historical', 'Outdoor Activities', 
                'Trips', 'Get Drunk', 'Student', 'Friends', 'Family', 'Couples', 'Tourists']


    list_of_strings = ast.literal_eval(user_likes)
    sorted_places = recommend_places(places, list_of_strings, k=10)
    output = []
    for place in sorted_places:
        if place in category:
            output.append(category[place])
    
    return output
