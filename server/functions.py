from scipy.spatial.distance import cosine

def cosine_similarity(x, y):
    """
    Compute the cosine similarity between two sparse binary vectors x and y.

    Parameters:
    x (numpy array): The first sparse binary vector.
    y (numpy array): The second sparse binary vector.

    Returns:
    similarity (float): The cosine similarity between x and y.
    """
    # Compute the cosine distance between x and y
    distance = cosine(x, y)

    # Compute the cosine similarity as 1 - cosine distance
    similarity = 1 - distance

    return similarity


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)



def csr_matrix(data, indices, indptr, shape):
    """
    Create a CSR (Compressed Sparse Row) matrix from the given data, indices,
    indptr, and shape.
 
    Args:
        data (list): The non-zero values in the matrix, row-wise.
        indices (list): The column indices corresponding to the non-zero values
            in the data list, row-wise.
        indptr (list): The indices where each row starts in the data and indices
            lists.
        shape (tuple): The shape of the matrix, as a tuple of (num_rows, num_cols).
 
    Returns:
        csr_matrix: The CSR matrix created from the given data, indices, indptr,
        and shape.
    """
    num_rows, num_cols = shape
    num_nonzeros = len(data)
 
    # Initialize the row and column index arrays
    row_indices = [0] * num_nonzeros
    col_indices = [0] * num_nonzeros
 
    # Fill the row and column index arrays
    for i in range(num_rows):
        for j in range(indptr[i], indptr[i+1]):
            row_indices[j] = i
            col_indices[j] = indices[j]
 
    # Create the CSR matrix
    csr_data = data.copy()
    csr_row_indices = row_indices.copy()
    csr_indptr = indptr.copy()
    csr_shape = shape
    return (csr_data, csr_row_indices, csr_indptr, csr_shape)
 