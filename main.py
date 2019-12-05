from Plot import Plot
from Vector import Vector
import numpy as np
import pandas as pd


def get_vectors_from_csv(file):
    resultList = []
    for i in file.values:
        v = Vector(rz1=i[0], iz1=i[1], rz2=i[2], iz2=i[3])
        resultList.append(v)
    return resultList


def main():
    file = pd.read_csv("data/input.csv")
    vectors = get_vectors_from_csv(file)
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
