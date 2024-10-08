def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor, rounding to 2 decimal places."""
    
    # Check if matrix is a list of lists and if all elements are integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div, rounding to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]

