import numpy

from Plot import Plot
from Vector import Vector

import numpy as np
import pandas as pd
import RegressionAnalysis as ra
import Utils as utls
import seaborn as sns


def get_vectors_from_csv(file):
    resultList = []
    for i in file.values:
        v = Vector(rz1=i[0], iz1=i[1], rz2=i[2], iz2=i[3])
        resultList.append(v)
    return resultList


def draw_contours(plot, vectors, x_limits, y_limits):
    v1 = vectors[33]
    v2 = vectors[78]
    v3 = vectors[110]
    plot.set_limits(x_limits, y_limits)
    plot.draw_unit_contour()
    plot.draw_сontour(v1)
    plot.draw_сontour(v2)
    plot.draw_сontour(v3)


def draw_regression_analysis(plot, vectors, number_of_permutation=0):
    permutations = utls.get_permutations(ra.z)
    permutation = ra.z
    i = 0
    for item in permutations:
        if i == number_of_permutation:
            permutation = item
            break
        i += 1

    i = 0
    color = 'r'
    for vector in vectors:
        w = ra.get_mapping_to_z(vector, permutation)
        a = ra.get_sum_of_signs(vector)
        b = ra.get_average_w(w)
        p = ra.get_b_normalized_to_a(b, a)
        if i == 0 or i == 50 or i == 100:
            color = numpy.random.rand(3, )
        plot.draw_regression_analysis(p, color)
        i += 1


def main():
    file = pd.read_csv("data/input.csv")
    vectors = get_vectors_from_csv(file)
    plot = Plot()
    X = np.arange(-10, 10, 1).tolist()
    Y = np.arange(-5, 5, 0.8).tolist()

    # draw_contours(plot, vectors, X, Y)
    draw_regression_analysis(plot, vectors, 1)

    plot.show_plot()


if __name__ == "__main__":
    main()
