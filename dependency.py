import numpy as np

def create_matrix_with_diagonal(round_number):
    # 创建一个5x5的矩阵，对角线上的元素为round_number，其他元素为0
    matrix = np.zeros((5, 5), dtype=int)
    np.fill_diagonal(matrix, -round_number)
    return matrix