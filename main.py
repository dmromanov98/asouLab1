from Plot import Plot
from Vector import Vector
import numpy as np


def readFile(path):
    file = open(path, 'r')
    resultList = []
    for line in file:
        coords = line.split("\t")
        v = Vector(rz1=float(coords[0]), iz1=float(coords[1]), rz2=float(coords[2]), iz2=float(coords[3]))
        resultList.append(v)

    return resultList


def main():
    vectors = readFile("data/input.txt")
    v1 = vectors[33]
    v2 = vectors[78]
    v3 = vectors[110]

    plot = Plot()
    X = np.arange(-10, 10, 0.5).tolist()
    Y = np.arange(-5, 5, 0.5).tolist()
    plot.set_limits(X, Y)

    plot.draw_unit_contour()
    plot.draw_сontour(v1)
    plot.draw_сontour(v2)
    plot.draw_сontour(v3)
    plot.show_plot()


if __name__ == "__main__":
    main()
