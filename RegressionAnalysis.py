z = [1, 1j, -1, -1j]


def get_mapping_to_z(vector, permutation_z=z, offset=0):
    return [vector.rz1 * permutation_z[0],
            vector.iz1 * permutation_z[1],
            vector.rz2 * permutation_z[2],
            vector.iz2 * permutation_z[3]]


def get_sum_of_signs(vector):
    return vector.rz1 + vector.rz2 + vector.iz1 + vector.iz2


def get_average_w(w):
    sum = 0
    for i in w:
        sum += i

    return sum / 4


def get_b_normalized_to_a(b, a):
    return b / a
