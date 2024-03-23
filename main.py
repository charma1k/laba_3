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

def generate_triangle_submatrix(size, triangle_type):
    submatrix = []
    for i in range(size):
        if triangle_type == 'upper':
            submatrix.append([0] * i + [i + 1] * (size - i))
        elif triangle_type == 'lower':
            submatrix.append([i + 1] * (i + 1) + [0] * (size - i - 1))
    return submatrix

matrix_size = int(input("Введите размер матрицы: "))

matrix_a = generate_matrix(matrix_size)
print("Матрица A:")
print_matrix(matrix_a)

size_half = matrix_size // 2
matrix_b = generate_triangle_submatrix(size_half, 'upper')
matrix_c = generate_triangle_submatrix(size_half, 'lower')
matrix_d = generate_triangle_submatrix(size_half, 'upper')
matrix_e = generate_triangle_submatrix(size_half, 'lower')

print("\nПодматрица B:")
print_matrix(matrix_b)
print("\nПодматрица C:")
print_matrix(matrix_c)
print("\nПодматрица D:")
print_matrix(matrix_d)
print("\nПодматрица E:")
print_matrix(matrix_e)

def count_greater_than_K_in_even_columns(matrix, K):
    count = 0
    for i in range(len(matrix) // 2):
        for j in range(0, i + 1, 2):
            if matrix[i][j] > K:
                count += 1
    for i in range(len(matrix) // 2, len(matrix)):
        for j in range(0, len(matrix) - (i + 1), 2):
            if matrix[i][j] > K:
                count += 1
    return count

def product_in_odd_rows(matrix):
    product = 1
    for i in range(len(matrix) // 2, len(matrix), 3):
        for j in range(len(matrix) - (i + 1) + 1, len(matrix) // 2):
            product *= matrix[i][j]
    for i in range(len(matrix) // 2, len(matrix), 3):
        for j in range(len(matrix) // 2, i):
            product *= matrix[i][j]
    return product

K_value = 5
print("\nКоличество элементов больше K в четных столбцах:", count_greater_than_K_in_even_columns(matrix_e, K_value))
print("Произведение элементов в нечетных строках:", product_in_odd_rows(matrix_e))
