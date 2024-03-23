# Вариант 15
# Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, 
# чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: AF– KA^T . 
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

def generate_matrix(size):
    matrix = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

def submatrix(matrix, row_start, row_end, col_start, col_end):
    return [row[col_start:col_end] for row in matrix[row_start:row_end]]

def check_condition(submatrix, k_value):
    even_columns_sum = 0
    for col in range(len(submatrix[0])):
        for row in range(len(submatrix)):
            if submatrix[row][col] > k_value:
                even_columns_sum += 1

    odd_rows_sum = 0
    for row in range(1, len(submatrix), 2):
        for col in range(len(submatrix[row])):
            odd_rows_sum += submatrix[row][col]

    return even_columns_sum > odd_rows_sum

def swap_submatrices(matrix, sub1, sub2):
    for i in range(len(sub1)):
        for j in range(len(sub1[i])):
            matrix[sub1[i][j]], matrix[sub2[i][j]] = matrix[sub2[i][j]], matrix[sub1[i][j]]

def transpose(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            elem = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(elem)
        result.append(row)
    return result

def scalar_multiplication(matrix, scalar):
    result = [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return result

matrix_size = int(input("Введите размер матрицы: "))

matrix_a = generate_matrix(matrix_size)
print("Матрица A:")
print_matrix(matrix_a)

matrix_b = submatrix(matrix_a, 0, matrix_size//2, 0, matrix_size//2)
matrix_c = submatrix(matrix_a, 0, matrix_size//2, matrix_size//2, matrix_size)
matrix_d = submatrix(matrix_a, matrix_size//2, matrix_size, 0, matrix_size//2)
matrix_e = submatrix(matrix_a, matrix_size//2, matrix_size, matrix_size//2, matrix_size)
print("\nПодматрица B:")
print_matrix(matrix_b)
print("\nПодматрица C:")
print_matrix(matrix_c)
print("\nПодматрица D:")
print_matrix(matrix_d)
print("\nПодматрица E:")
print_matrix(matrix_e)

k_value = 5
if check_condition(matrix_e, k_value):
    swap_submatrices(matrix_e, [[0, 0], [1, 0]], [[1, 1], [0, 1]])
else:
    swap_submatrices(matrix_b, [[0, 0], [1, 0]], [[1, 1], [0, 1]])
print("\nМатрица E после преобразования:")
print_matrix(matrix_e)

matrix_f_transposed = transpose(matrix_e)
result = matrix_multiplication(matrix_a, matrix_e)
k_times_a_transposed = scalar_multiplication(transpose(matrix_a), k_value)
final_result = [[result[i][j] - k_times_a_transposed[i][j] for j in range(len(result[0]))] for i in range(len(result))]
print("\nРезультат выражения A*F - K*AT:")
print_matrix(final_result)
