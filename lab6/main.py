import numpy as np
import matplotlib.pyplot as plt


def euler(f, y0, x0, xn, h):
    num_points = int((xn - x0) / h) + 1
    x = [x0 + i * h for i in range(num_points)]
    y = [y0]

    for i in range(1, num_points):
        x_prev, y_prev = x[i - 1], y[i - 1]
        y_next = y_prev + h * f(x_prev, y_prev)
        y.append(y_next)

    return x, y


def runge_kutt(f, y0, x0, xn, h):
    num_points = int((xn - x0) / h) + 1
    x = [x0 + i * h for i in range(num_points)]
    y = [y0]

    for i in range(1, num_points):
        x_prev, y_prev = x[i - 1], y[i - 1]
        k1 = h * f(x_prev, y_prev)
        k2 = h * f(x_prev + h / 2, y_prev + k1 / 2)
        k3 = h * f(x_prev + h / 2, y_prev + k2 / 2)
        k4 = h * f(x_prev + h, y_prev + k3)
        y_next = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y.append(y_next)

    return x, y


def milne(f, y0, x0, xn, h):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n + 1)
    y = np.zeros(n + 1)
    y[:4] = runge_kutt(f, y0, x0, x0 + 3 * h, h)[1]

    for i in range(3, n):
        y[i + 1] = y[i - 3] + 4 * h / 3 * \
                          (2 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]) +
                           2 * f(x[i - 2], y[i - 2]))

    return x, y


def f1(x, y):
    return x + y


def f2(x, y):
    return x - y


def f3(x, y):
    return x * y


y0 = float(input("Введите начальное значение y (y0): "))
x0 = float(input("Введите начальное значение x (x0): "))
xn = float(input("Введите конечное значение x (xn): "))
h = float(input("Введите шаг (h): "))
a = int(input("Select function: "))


def solution1(x):
    return 2 * np.exp(x) - x - 1


def solution2(x):
    return 2 / np.exp(x) + x - 1


def solution3(x):
    return np.exp(x**2 / 2)


if a == 1:
    x_euler, y_euler = euler(f1, y0, x0, xn, h)
    x_rk4, y_rk4 = runge_kutt(f1, y0, x0, xn, h)
    x_milne, y_milne = milne(f1, y0, x0, xn, h)
    x = np.linspace(x0, xn, 100)
    y = solution1(x)
elif a == 2:
    x_euler, y_euler = euler(f2, y0, x0, xn, h)
    x_rk4, y_rk4 = runge_kutt(f2, y0, x0, xn, h)
    x_milne, y_milne = milne(f2, y0, x0, xn, h)
    x = np.linspace(x0, xn, 100)
    y = solution2(x)
elif a == 3:
    x_euler, y_euler = euler(f3, y0, x0, xn, h)
    x_rk4, y_rk4 = runge_kutt(f3, y0, x0, xn, h)
    x_milne, y_milne = milne(f3, y0, x0, xn, h)
    x = np.linspace(x0, xn, 100)
    y = solution3(x)
else:
    print("ты кажется перепутал...")

plt.plot(x, y, label="Точное решение", color='blue')
plt.plot(x_euler, y_euler, label="Метод Эйлера", linestyle='--', color='green')
plt.plot(x_rk4, y_rk4, label="Метод Рунге-Кутта 4-го порядка", linestyle='--', color='red')
plt.plot(x_milne, y_milne, label="Метод Милна", linestyle='--', color='yellow')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Приближенное и точное решение ОДУ')
plt.legend()
plt.grid(True)
plt.show()
