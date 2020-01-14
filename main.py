import numpy

from Plot import Plot
from Vector import Vector

import numpy as np
import pandas as pd
import RegressionAnalysis as ra
import Utils as utls


def get_z(vectors=[], best=False):
    result = ra.z
    max_std = 0
    if best:
        permutations = utls.get_permutations(ra.z)
        for item in permutations:
            ps = []
            permutation = item
            for vector in vectors:
                w = ra.get_mapping_to_z(vector, permutation)
                a = ra.get_sum_of_signs(vector)
                b = ra.get_average_w(w)
                p = ra.get_b_normalized_to_a(b, a)
                ps.append(p)

            print(ps)
            std = np.std(np.abs(ps))
            if std > max_std:
                max_std = std
                result = item

    return result


def get_vectors_from_csv(file):
    resultList = []
    for i in file.values:
        v = Vector(p1=i[0], p2=i[1], p3=i[2], p4=i[3])
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


def draw_regression_analysis(plot, vectors):
    permutationZ = get_z(vectors, False)
    print("Permutation = ", permutationZ)
    permutation = []
    for axis in permutationZ:
        if axis == 1:
            permutation.append(0)
        elif axis == 1j:
            permutation.append(1)
        elif axis == -1:
            permutation.append(2)
        elif axis == -1j:
            permutation.append(3)

    print(permutation)
    color = 'r'
    i = 0
    for vector in vectors:
        ch_vector = [vector.p1, vector.p2, vector.p3, vector.p4]
        ch_vector[0], ch_vector[1], ch_vector[2], ch_vector[3] = \
            ch_vector[permutation[0]], ch_vector[permutation[1]], ch_vector[permutation[2]], ch_vector[permutation[3]]
        new_vector = Vector(ch_vector[0], ch_vector[1], ch_vector[2], ch_vector[3])
        w = ra.get_mapping_to_z(new_vector, ra.z)
        a = ra.get_sum_of_signs(new_vector)
        b = ra.get_average_w(w)
        p = ra.get_b_normalized_to_a(b, a)
        if i == 0 or i == 50 or i == 100:
            color = numpy.random.rand(3, )
        plot.draw_dot(p, color)
        i += 1


# Normalization method
def standardization(vectors, type=1):
    result = []
    X = []
    for item in vectors:
        X.append(item.p1)
        X.append(item.p2)
        X.append(item.p3)
        X.append(item.p4)

    std = np.std(X)
    mean = np.mean(X)
    min = np.min(X)
    max = np.max(X)

    for item in vectors:
        if type == 1:
            result.append([(item.p1 - min) / (max - min),
                           (item.p2 - min) / (max - min),
                           (item.p3 - min) / (max - min),
                           (item.p4 - min) / (max - min)])
        elif type == 2:
            result.append([(item.p1 - mean) / std,
                           (item.p2 - mean) / std,
                           (item.p3 - mean) / std,
                           (item.p4 - mean) / std])
    return result


def draw_principal_component_method(plot, vectors):
    new_X = standardization(vectors, 2)
    G = pd.DataFrame(new_X).corr()

    eig_values, eig_vectors = np.linalg.eig(G)  # eigenvector and value

    # sorting matrix
    for i in range(0, len(eig_values) - 1):
        for j in range(i + 1, len(eig_values)):
            if eig_values[i] < eig_values[j]:
                eig_values[i], eig_values[j] = eig_values[j], eig_values[i]
                eig_vectors[i], eig_vectors[j] = eig_vectors[j], eig_vectors[i]

    v1 = eig_vectors[0]
    v2 = eig_vectors[1]
    X = np.array(new_X)
    P = X.dot(v1) + 1j * (X.dot(v2))
    color = 'r'
    i = 0
    for dot in P:
        if i == 0 or i == 50 or i == 100:
            color = numpy.random.rand(3, )
        plot.draw_dot(dot, color)
        i += 1


def main():
    file = pd.read_csv("data/input.csv")
    vectors = get_vectors_from_csv(file)
    plot = Plot()
    X = np.arange(-10, 10, 1).tolist()
    Y = np.arange(-5, 5, 0.8).tolist()
    # draw_contours(plot, vectors, X, Y)
    draw_regression_analysis(plot, vectors)
    # draw_principal_component_method(plot, vectors)

    plot.show_plot()


if __name__ == "__main__":
    main()
