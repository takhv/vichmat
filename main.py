import numpy as np

def checkDiagonal(A):
    # ПРОВЕРКА ДИАГОНАЛЬНОГО ПРЕОБЛАДАНИЯ
    diagon = A.diagonal()
    checkDiag = []
    for i in range(0, A.shape[0]):
        a = np.sum(np.abs(A[i])) - np.abs(diagon[i])
        checkDiag.append(a)
    # checker = np.abs(diagon) > np.abs(checkDiag)
    # print("\n\nПРОВЕРКА ДИАГОНАЛЬНОГО ПРЕОБЛАДАНИЯ\n")
    # print(checker)

def reorder_rows(A, B):
    n = len(A)
    for i in range(n):
        max_idx = np.argmax(np.abs(A[i:, i])) + i
        if max_idx != i:
            A[[i, max_idx]] = A[[max_idx, i]]
            B[[i, max_idx]] = B[[max_idx, i]]

def gauss_zeidel(A, B, eps, max_iter=100):
    n = len(B)
    if not checkDiagonal(A):
        reorder_rows(A, B)
    x = np.zeros(n)
    iteration = 0
    errors = []
    while iteration < max_iter:
        x_new = np.copy(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (B[i] - sum1 - sum2) / A[i, i]
        print(iteration, x_new, x, np.linalg.norm(x_new - x))
        errors.append(np.linalg.norm(x_new - x))
        if errors[-1] < eps:
            return "OTVET: " + str(x_new)
        x = x_new
        iteration += 1
    raise ValueError("error")


print("Вариант: 14")

inputFile = open('matrix.txt', 'r')
epsilon = float(inputFile.readline())
inputMatrix = [line.rstrip().split() for line in inputFile]
matrix = np.array(inputMatrix, 'int')

Amatrix = np.delete(matrix, -1, axis=1)
Bmatrix = matrix[:, -1]
diag = Amatrix.diagonal()



# ПРЕОБРАЗОВАННАЯ МАТРИЦА С КОЭФ 1 ПЕРЕД ДИАГ ЭЛЕМЕНТАМИ
preobrazMatrix = matrix.astype(float)
for i in range(0, preobrazMatrix.shape[0]):
    preobrazMatrix[i] = preobrazMatrix[i] / diag[i]
# ЧТОБЫ МАТРИЦА БЫЛА ТИПА "ВЫРАЖЕН ДИАГОНАЛЬНЫЙ ЭЛЕМ" НУЖНО ПОМЕНЯТЬ ЗНАКИ У Б МАТРИЦЫ И ДИАГОНАЛИ
preobrazMatrix[:, :-1] = preobrazMatrix[:, :-1] * (-1)
for i in range(0, preobrazMatrix.shape[0]):
    preobrazMatrix[i][i] = preobrazMatrix[i][i] * (-1)

# ПРЕОБРАЖЕННАЯ А МАТРИЦА
aPreoMatrix = np.delete(preobrazMatrix, -1, axis=1)

# ПРЕОБРАЖЕННАЯ Б МАТРИЦА
bPreoMatrix = preobrazMatrix[:, -1]
# ВЫВОД ВЕКТОРА
print("\n\nВЕКТОPS НЕИЗВЕСТНЫХ\n")
for i, elem in enumerate(aPreoMatrix):
    total = f'x{i + 1} = '
    vectors = []
    for j, koef in enumerate(elem):
        if j != i:
            vectors.append(f"{koef}*x{j + 1}")
    total += ' + '.join(vectors)
    total += f' + {bPreoMatrix[i]}'
    print(total)


# РЕШЕНИЕ
# x = np.linalg.solve(Amatrix, Bmatrix)
# print(x)

print("\n\nРЕШЕНИЕ, КОЛИЧЕСТВО ИТЕРАЦИЙ И ПОГРЕШНОСТИ\n")
print(gauss_zeidel(Amatrix, Bmatrix, epsilon))
