import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    inclinations = []
    plt_title = str(input("Title: "))
    x_label = str(input("x label: "))
    y_label = str(input("y label: "))
    elem_num = int(input("Number of Elements: "))
    x_max = float(input("x max: "))
    
    for i in range(elem_num):
        v = input("inclination-{}: ".format(i))
        inclinations.append(v)
    
    fig, ax = plt.subplots()
    ax.set(title=plt_title, xlabel=x_label, ylabel=y_label)
    for i in range(elem_num):
        plt.plot([0, x_max], [0, float(inclinations[i]) * x_max])
    ax.minorticks_on()
    ax.grid(which='major', color='gray', linestyle='dotted')
    filename = str(input("File Name: "))
    plt.savefig(filename + ".png")