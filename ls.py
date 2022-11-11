#最小二乗法計算機

import numpy as np
import matplotlib.pyplot as plt

def reg1dim(x, y):
    n = len(x)
    a = ((np.dot(x, y)- y.sum() * x.sum()/n)/
        ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum())/n
    return a, b

if __name__ == "__main__":
    x = []
    y = []

    plt_title = str(input("Title: "))
    x_label = str(input("x label: "))
    y_label = str(input("y label: "))
    elem_num = int(input("Number of Elements: "))

    for i in range(elem_num):
        v = input("x-{}: ".format(i))
        x.append(v)
        v = input("y-{}: ".format(i))
        y.append(v)

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    a, b = reg1dim(x, y)

    print("[i] inclination: " + str(a))
    print("[i] intercept: " + str(b))
    fig, ax = plt.subplots()
    ax.set(title=plt_title, xlabel=x_label, ylabel=y_label)
    plt.scatter(x, y, color="k")
    plt.plot([0, x.max()], [b, a * x.max() + b])
    ax.minorticks_on()
    ax.grid(which='major', color='gray', linestyle='dotted')
    plt.show()