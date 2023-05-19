#最小二乗法計算機 y軸片対数ver

import math
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
    yl = []

    plt_title = str(input("Title: "))
    x_label = str(input("x label: "))
    y_label = str(input("y label: "))
    elem_num = int(input("Number of Elements: "))

    for i in range(elem_num):
        v = input("x-{}: ".format(i))
        x.append(v)
        v = input("y-{}: ".format(i))
        y.append(v)
        yl.append(math.log10(float(v)))

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    yl = np.array(yl, dtype=float)
    a, b = reg1dim(x, yl)

    print("[i] inclination: " + str(a))
    print("[i] intercept: " + str(pow(10, b)))
    fig, ax = plt.subplots()
    ax.set(title=plt_title, xlabel=x_label, ylabel=y_label)
    ax.set_yscale('log')
    plt.scatter(x, y, color="k")
    plt.plot([0, x.max()], [pow(10, b), pow(10, a * x.max() + b)])
    ax.minorticks_on()
    ax.grid(which='major', color='gray', linestyle='-')
    ax.grid(which='minor', color='gray', linestyle='dotted')
    filename = str(input("File Name: "))
    plt.savefig(filename + ".png")