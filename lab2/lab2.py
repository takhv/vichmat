import numpy as np


def f1(x):
    return 2.3 * (x ** 3) + 5.75 * (x ** 2) - 7.41 * x - 10.6


def df1(x):
    return 2.3 * 3 * (x ** 2) + 5.75 * 2 * x - 7.41


def g1(x):
    return x - f1(x) / df1(x)


def f2(x):
    return -2.4 * (x ** 3) + 1.27 * (x ** 2) - 8.63 * x + 2.31


def df2(x):
    return -2.4 * 3 * (x ** 2) + 1.27 * 2 * x + 8.63


def g2(x):
    return x - f2(x) / df2(x)


def f3(x):
    return 5.74 * (x ** 3) - 2.95 * (x ** 2) - 10.28 * x - 3.23


def df3(x):
    return 5.74 * 3 * (x ** 2) - 2.95 * 2 * x - 10.28


def g3(x):
    return x - f3(x) / df3(x)


def f4(x):
    return -0.38 * (x ** 3) - 3.42 * (x ** 2) + 2.51 * x + 8.75


def df4(x):
    return -0.38 * 3 * (x ** 2) - 3.42 * 2 * x + 2.51


def g4(x):
    return x - f4(x) / df4(x)


def systemFirstEq1(x, y):
    return 2 + np.cos(x)


def systemSecondEq1(x, y):
    return 0.8 - np.cos(y-1)


def systemFirstEq2(x, y):
    return 1.5 - np.sin(x - 1)


def systemSecondEq2(x, y):
    return 1 + np.sin(y + 1)


def hords_method(a, b, epsilon, max_iter=1000):
    iter_count = 0
    while abs(f(b)) > epsilon and iter_count < max_iter:
        x_next = b - f(b) * (b - a) / (f(b) - f(a))
        if f(a) * f(x_next) < 0:
            b = x_next
        else:
            a = x_next
        iter_count += 1
    if abs(f(b)) > epsilon:
        print("слишком много итераций")
    return b, f(b)


def secant_method(f, x0, x1, epsilon, max_iter=1000):
    iter_count = 0
    while abs(f(x1)) > epsilon and iter_count < max_iter:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_next
        iter_count += 1
    if abs(f(x1)) > epsilon:
        print("слишком много итераций")
    return x1, f(x1)


def simple_iteration_method(f, g, x0, epsilon, max_iter=1000):
    iter_count = 0
    while abs(f(x0)) > epsilon and iter_count < max_iter:
        x_next = g(x0)
        x0 = x_next
        iter_count += 1
    if abs(f(x0)) > epsilon:
        print("слишком много итераций")
    return x0, f(x0)


def simple_iteration_for_system_method(firstEq, secondEq, x0, y0, epsilon, max_iter=1000):
    x_prev, y_prev = x0, y0
    for i in range(max_iter):
        x_new = firstEq(x_prev, y_prev)
        y_new = secondEq(x_prev, y_prev)
        if np.abs(x_new - x_prev) < epsilon and np.abs(y_new - y_prev) < epsilon:
            return x_new, y_new
        x_prev, y_prev = x_new, y_new

    raise Exception("слишком много итераций")


def number_checker(number):
    try:
        float(number)
        return True
    except ValueError:
        print("советую проверить ввод")
        return False


def verification(a, b):
    if f(a) * f(b) < 0:
        print("корень есть")
        return True
    else:
        print("на этом участке корня нет или их четное количество")
        return False


# Исходные данные
epsilon = 0.01
type_of_equation = input("уравнение(1) или система уравнений(2)?: ")
if type_of_equation == "1":
    print("1. 2,3x^3 + 5,75x^2 - 7,41x - 10,6")
    print("2. -2,4x^3 + 1,27x^2 + 8,63x + 2,31")
    print("3. 5,74x^3 - 2,95x^2 - 10,28x - 3,23")
    print("4. -0,38x^3 - 3,42x^2 + 2,51x + 8,75")
    number_of_equation = input("номер уравнения которое хотите решить: ")
    print("введите данные")
    a = input("a: ")
    b = input("b: ")
    if number_of_equation == "1":
        f = f1
        df = df1
        g = g1
    elif number_of_equation == "2":
        f = f2
        df = df2
        g = g2
    elif number_of_equation == "3":
        f = f3
        df = df3
        g = g3
    elif number_of_equation == "4":
        f = f4
        df = df4
        g = g4
    else:
        print("вы ввели чтото не то")
    if number_checker(a) and number_checker(b):
        if verification(float(a), float(b)):
            print(f"метод хорд - {hords_method(float(a), float(b), epsilon)}")
            print(f"метод секущих - {secant_method(f, float(a), float(b), epsilon)}")
            print(f"метод простой итерации - {simple_iteration_method(f, g, float(a), epsilon)}")
elif type_of_equation == "2":
    print("1. y - cosx = 2")
    print("   x + cos(y-1) = 0,8")
    print("2. sin(x-1) + y = 1,5")
    print("   x - sin(y+1) = 1")
    number_of_system = input("номер системы: ")
    if number_of_system == "1":
        systemFirst = systemFirstEq1
        systemSecond = systemSecondEq1
    elif number_of_system == "2":
        systemFirst = systemFirstEq2
        systemSecond = systemSecondEq2
    else:
        print("вы ввели чтото не то")
    print(f"метод простой итерации - {simple_iteration_for_system_method(systemFirst, systemSecond, 0, 0, epsilon)}")
else:
    print("?некорректный ввод?")


# 1.79 0.144
