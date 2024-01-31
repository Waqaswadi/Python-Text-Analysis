# 22096309 -  Student ID



import numpy as np

# Solution for Question 2.a ;



def matrix_multiplication(*argv):
    """
    Definition:
    Perform matrix multiplication on an arbitrary number of matrices.
    Matrices must have compatible dimensions for multiplication, i.e. the number of columns in each matrix
    must match the number of rows in the next matrix.
    
    Parameters:
    *argv (np.ndarray): Arbitrary number of matrices to be multiplied.

    Returns:
    np.ndarray: Result of matrix multiplication.
    
    """
    # check that the matrices have compatible dimensions for multiplication
    for i in range(len(argv) - 1):
        if argv[i].shape[1] != argv[i+1].shape[0]:
            print("Matrix dimension mismatch")
            return None
    
    # create an empty result matrix
    result = np.zeros((argv[0].shape[0], argv[-1].shape[1]))

    # perform matrix multiplication on the first two matrices
    for i in range(argv[0].shape[0]):
        for j in range(argv[1].shape[1]):
            for k in range(argv[0].shape[1]):
                result[i][j] += argv[0][i][k] * argv[1][k][j]

    # create a numpy array to hold the result of the first multiplication
    temp = np.array(result)

    # loop through the remaining matrices
    for m in range(2, len(argv)):
        # reset the result matrix to all zeros
        result = np.zeros((temp.shape[0], argv[m].shape[1]))

        # perform matrix multiplication on the temporary matrix and the current matrix
        for i in range(temp.shape[0]):
            for j in range(argv[m].shape[1]):
                for k in range(temp.shape[1]):
                    result[i][j] += temp[i][k] * argv[m][k][j]

        # update the temporary matrix with the result of the multiplication
        temp = np.array(result)

    # return the final result
    return result



# Solution for Question 2.b ;

def linear_solver(A, b):
    """
    Definition:
    Solves a system of linear equations Ax = b using matrix inversion.

    Parameters:
    A (np.ndarray): Coefficient matrix of the linear system of equations. Must be a square matrix.
    b (np.ndarray): Constant vector of the linear system of equations. Must have the same number of rows as A.

    Returns:
    np.ndarray: Solution vector x of the linear system of equations.
    """
    # Verify that the coefficients and constants have the correct shapes
    if A.shape[0] != A.shape[1]: 
        # Checking if the co-efficient matrix is square
        print("The Inputs are not suitable for a linear system of equations.")
    elif A.shape[0] < b.shape[0]:
        # Number of equations must not be greater than number of variables
        print("Number of equations must not be greater than number of variables")
    elif A.shape[0] > b.shape[0]:
        # Number of equations must not be less than number of variables
        print("Number of equations must not be less than number of variables")
    else:
        print('Unique Solution')
        # Invert the coefficients matrix using the NumPy linalg.inv() function
        Ainv = np.linalg.inv(A)

        # Solve the system of equations by multiplying the inverted coefficients matrix by the constants vector
        res = matrix_multiplication(Ainv, b)

        # Print the solutions
        return res


# Solution for Question 2.c ;


def LLS(A, b):
    """
    Definition:
    Solves a linear least squares problem of the form Ax = b using the normal equations method.
    χ = A+ * b
    where A+ = (AT A)−1AT is the Moore–Penrose inverse of matrix A

    Parameters:
    A (np.ndarray): Coefficient matrix of the linear system of equations.
    b (np.ndarray): Constant vector of the linear system of equations.

    Returns:
    np.ndarray: Solution vector x (written as result) of the linear least squares problem.
    """
    # calculate the transpose of A
    A_Trans = np.transpose(A)

    # calculate the product of the transpose of A and A
    A_T_A = matrix_multiplication(A_Trans , A)

    # calculate the inverse of the product from step 2
    A_T_A_inv = np.linalg.inv(A_T_A)

    # calculate the product of the inverse and the transpose of A
    A_plus = matrix_multiplication(A_T_A_inv , A_Trans)

    # calculate the product of the result from step 4 and b
    result = matrix_multiplication(A_plus , b)

    return result

