import math
import numpy as np
import matplotlib.pyplot as plt


def table_of_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef


def newton(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[0][0]
    for k in range(1, n + 1):
        p += coef[0][k] * (math.prod([(x - x_data[i]) for i in range(k)]))
    return p


def lagrange(x_data, y_data, x):
    L = np.zeros_like(x)
    for i in range(len(x_data)):
        li = np.ones_like(x)
        for j in range(len(x_data)):
            if i != j:
                li *= (x - x_data[j]) / (x_data[i] - x_data[j])
        L += y_data[i] * li
    return L


def gauss(x_data, y_data, x):
    n = len(x_data)
    a = np.zeros((n, n))
    a[:, 0] = y_data
    for j in range(1, n):
        for i in range(n - j):
            a[i, j] = (a[i + 1, j - 1] - a[i, j - 1]) / (x_data[i + j] - x_data[i])
    G = np.zeros_like(x)
    for k in range(n):
        term = a[0, k]
        for i in range(k):
            term *= (x - x_data[i])
        G += term
    return G


def plot_graphs(x, y, x_new, y_new_lagrange, y_new_newton, y_new_gauss):
    plt.scatter(x, y, color='red', label='точки точечки')
    plt.plot(x_new, y_new_lagrange, label='лагранж', color='green')
    plt.plot(x_new, y_new_newton, label='ньютон', color='blue')
    plt.plot(x_new, y_new_gauss, label='гаусс', color='purple')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графики интерполяции')
    plt.show()


x = list(map(float, input("введите x через пробел: ").split()))
y = list(map(float, input("введите y через пробел: ").split()))
table = table_of_differences(x, y)
print(table)

x_val = float(input("в каком х?: "))
y_newton = newton(table, x, x_val)
y_lagrange = lagrange(x, y, np.array([x_val]))[0]
y_gauss = gauss(x, y, np.array([x_val]))[0]

print(f"метод лагранжа: {y_lagrange}")
print(f"метод ньютона с разделенными разностями: {y_newton}")
print(f"метод гаусса: {y_gauss}")

x_new = np.linspace(min(x), max(x), 1000)
y_new_lagrange = lagrange(x, y, x_new)
y_new_newton = newton(table, x, x_new)
y_new_gauss = gauss(x, y, x_new)

plot_graphs(x, y, x_new, y_new_lagrange, y_new_newton, y_new_gauss)
