z = [1, 1j, -1, -1j]


def get_mapping_to_z(vector, permutation_z=z):
    return [vector.p1 * permutation_z[0],
            vector.p2 * permutation_z[1],
            vector.p3 * permutation_z[2],
            vector.p4 * permutation_z[3]]


def get_sum_of_signs(vector):
    return vector.p1 + vector.p2 + vector.p3 + vector.p4


def get_average_w(w):
    sum = 0
    for i in w:
        sum += i

    return sum / 4


def get_b_normalized_to_a(b, a):
    return b / a
