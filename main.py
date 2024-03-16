# Вариант 15
# Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, 
# чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: AF– KAT . 
# Выводятся по мере формирования А, F и все матричные операции последовательно.


import random


def generate_matrix(N):
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def get_submatrix(matrix, start_row, start_col, size):
    submatrix = []
    for i in range(start_row, start_row + size):
        submatrix.append(matrix[i][start_col:start_col + size])
    return submatrix


def count_greater_than_K(matrix, K):
    count = 0
    for row in matrix:
        for num in row:
            if num > K:
                count += 1
    return count


def swap_submatrices(matrix, submatrix1, submatrix2, start_row, start_col, size):
    for i in range(size):
        for j in range(size):
            matrix[start_row + i][start_col + j], matrix[submatrix1[0] + i][submatrix1[1] + j] = \
                matrix[submatrix1[0] + i][submatrix1[1] + j], matrix[start_row + i][start_col + j]
            matrix[start_row + i][start_col + j], matrix[submatrix2[0] + i][submatrix2[1] + j] = \
                matrix[submatrix2[0] + i][submatrix2[1] + j], matrix[start_row + i][start_col + j]


def calculate_F(matrix, K):
    E = get_submatrix(matrix, 1, 1, 2)
    B = get_submatrix(matrix, 0, 0, 2)
    C = get_submatrix(matrix, 0, 2, 2)
    D = get_submatrix(matrix, 2, 0, 2)

    count_even_cols_E = count_greater_than_K(E, K)
    sum_odd_rows_D = sum(matrix[2]) + sum(matrix[3])

    if count_even_cols_E > sum_odd_rows_D:
        swap_submatrices(matrix, (0, 0), (2, 0), 1, 1, 2)
    else:
        swap_submatrices(matrix, (0, 0), (0, 2), 1, 1, 2)


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Матрица A:")
    print_matrix(A)
    print()

    calculate_F(A, K)
    print("Матрица F:")
    print_matrix(A)
    print()

    A_transpose = transpose_matrix(A)
    print("Матрица A транспонированная:")
    print_matrix(A_transpose)
    print()

    A_times_F = matrix_multiplication(A, A_transpose)
    print("A * F:")
    print_matrix(A_times_F)
    print()

    K_times_A_transpose = [[-K * num for num in row] for row in A_transpose]
    print("K * Матрицу A транспонированную:")
    print_matrix(K_times_A_transpose)
    print()

    result = [[A_times_F[i][j] + K_times_A_transpose[i][j] for j in range(N)] for i in range(N)]
    print("Результат:")
    print_matrix(result)


main()
