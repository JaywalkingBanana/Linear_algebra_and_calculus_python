import numpy as np


def main():
    matrix = np.array([[3, 4, 1], [1, 7, 0], [1, 55, 1]])
    
    eigvals, eigvects = np.linalg.eig(matrix)
    imatrix = np.linalg.inv(matrix)
    diagmatrix = np.diag(eigvals)
    diagonalMatrix = np.matmul(np.linalg.inv(eigvects), np.matmul(matrix, eigvects))
    
main()    
