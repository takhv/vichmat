def f(x):
    return 2 * x ** 3 - 2 * x ** 2 + 7 * x - 14


def left_rectangle_method(a, b, n):
    h = (b - a) / n
    integral = sum(f(a + i * h) for i in range(n))
    return h * integral


def right_rectangle_method(a, b, n):
    h = (b - a) / n
    integral = sum(f(a + (i + 1) * h) for i in range(n))
    return h * integral


def middle_rectangle_method(a, b, n):
    h = (b - a) / n
    integral = sum(f((a + (i + 0.5) * h)) for i in range(n))
    return h * integral


def trapez_method(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n))
    return h * integral


def simpsons_method(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    integral *= h / 3
    return integral


def runge_rule(prev_result, curr_result, k):
    return abs(curr_result - prev_result) / (2 ** k - 1)


def integrate(method, a, b, tol=0.01, max_iter=1000, k=2):
    n = 1
    prev_result = 0

    for j in range(max_iter):
        result = method(a, b, n)
        error = runge_rule(prev_result, result, k)
        if error < tol:
            return result, n
        prev_result = result
        n *= 2

    raise Exception("недостаточно итераций")


print(f"левые прямоугольники {integrate(left_rectangle_method, 2, 4)}")
print(f"правые прямоугольники {integrate(right_rectangle_method, 2, 4)}")
print(f"середины прямоугольников {integrate(middle_rectangle_method, 2, 4)}")
print(f"трапеции {integrate(trapez_method, 2, 4)}")
print(f"симпсон {integrate(simpsons_method, 2, 4)}")
