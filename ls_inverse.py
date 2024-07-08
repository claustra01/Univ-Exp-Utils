# 反比例最小二乗法計算機

import numpy as np
import matplotlib.pyplot as plt

def inverse_regression(x, y):
    z = y * x
    n = len(x)
    a = ((np.dot(x, z) - z.sum() * x.sum() / n) /
         ((x ** 2).sum() - x.sum() ** 2 / n))
    b = (z.sum() - a * x.sum()) / n
    return a, b

def main():
    x = []
    y = []

    plt_title = str(input("Title: "))
    x_label = str(input("x label: "))
    y_label = str(input("y label: "))
    elem_num = int(input("Number of Elements: "))

    for i in range(elem_num):
        x_val = float(input("x-{}: ".format(i)))
        y_val = float(input("y-{}: ".format(i)))
        x.append(x_val)
        y.append(y_val)

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    a, b = inverse_regression(x, y)

    print("[i] coefficient a: " + str(a))
    print("[i] coefficient b: " + str(b))
    
    fig, ax = plt.subplots()
    ax.set(title=plt_title, xlabel=x_label, ylabel=y_label)
    plt.scatter(x, y, color="k")

    x_curve = np.linspace(min(x), max(x), 100)
    y_curve = a + b / x_curve
    plt.plot(x_curve, y_curve, color="blue")

    ax.minorticks_on()
    ax.grid(which='major', color='gray', linestyle='dotted')
    filename = str(input("File Name: "))
    plt.savefig(filename + ".png")

if __name__ == "__main__":
    main()
