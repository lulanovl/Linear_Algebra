from re import I
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

category = {
    "cafe": ["Oasis",'Oasis2'],
    "karaoke": ['karaoke1', 'karaoke2'],
    "cinema" : ['asdvasd', 'asdvsD'],
    "fast food" : ['afadvsd', 'asdfasdfv'],
    "restourant" : ['afb','asdgv']
}

places = {
    'cafe': [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    'karaoke': [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    'cinema': [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    'fast food': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    'restourant': [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
}

# def cosine_similarity(x, y):
#     """
#     Compute the cosine similarity between two sparse binary vectors x and y.
    
#     Parameters:
#     x (numpy array): The first sparse binary vector.
#     y (numpy array): The second sparse binary vector.
    
#     Returns:
#     similarity (float): The cosine similarity between x and y.
#     """
#     # Compute the cosine distance between x and y
#     distance = cosine(x, y)
    
#     # Compute the cosine similarity as 1 - cosine distance
#     similarity = 1 - distance
    
#     return similarity


# def csr_matrix(data, indices, indptr, shape):
#     """
#     Create a CSR (Compressed Sparse Row) matrix from the given data, indices,
#     indptr, and shape.
#     Args:
#         data (list): The non-zero values in the matrix, row-wise.
#         indices (list): The column indices corresponding to the non-zero values
#             in the data list, row-wise.
#         indptr (list): The indices where each row starts in the data and indices
#             lists.
#         shape (tuple): The shape of the matrix, as a tuple of (num_rows, num_cols).
#  
#     Returns:
#         csr_matrix: The CSR matrix created from the given data, indices, indptr,
#         and shape.
#     """
#     num_rows, num_cols = shape
#     num_nonzeros = len(data)
#  
#     # Initialize the row and column index arrays
#     row_indices = [0] * num_nonzeros
#     col_indices = [0] * num_nonzeros
#  
#     # Fill the row and column index arrays
#     for i in range(num_rows):
#         for j in range(indptr[i], indptr[i+1]):
#             row_indices[j] = i
#             col_indices[j] = indices[j]
#  
#     # Create the CSR matrix
#     csr_data = data.copy()
#     csr_row_indices = row_indices.copy()
#     csr_indptr = indptr.copy()
#     csr_shape = shape
#     return (csr_data, csr_row_indices, csr_indptr, csr_shape)

def matching_algo(user_likes):

    attributes = ['food', 'entertainment', 'cultural & historical', 'outdoor activities', 'trips', 
                'get drunk', 'student', 'friends', 'family', 'couples', 'tourists']
    str_list = user_likes.split(',')
    user_prefs = [eval(i) for i in str_list]
  
    place_attrs = []
    for place in places.values():
        place_attrs.append(place)
    place_attrs = csr_matrix(place_attrs)

    user_prefs = csr_matrix(user_prefs)

    similarities = cosine_similarity(user_prefs, place_attrs).flatten()

    sorted_indices = np.argsort(similarities)[::-1]
    sorted_places = list(places.keys())
    sorted_places = [sorted_places[i] for i in sorted_indices]

    output = []
    for place in sorted_places:
        if place in category:
            output.append(category[place])
    
    return output
