import numpy
import matplotlib.pyplot as plt
import math

from Vector import Vector


class Plot:
    def __init__(self):
        fig, self.ax = plt  .subplots()
        self.ax.set_xlabel('ReZ')
        self.ax.set_ylabel('ImZ')

    def set_limits(self, X, Y):
        self.ax.set_xticks(X)
        self.ax.set_yticks(Y)

    @staticmethod
    def get_dots(vector):
        result = []
        complexNumbers = [vector.rz1 + 0j, 0 + vector.iz1 * 1j, -vector.rz2 + 0j, 0 + vector.iz2 * -1j, vector.rz1 + 0j]
        X = [x.real for x in complexNumbers]
        Y = [x.imag for x in complexNumbers]
        result.append(X)
        result.append(Y)
        return result

    def draw_unit_contour(self):
        self.draw_сontour(Vector(1, 1, 1, 1), 0)

    def draw_сontour(self, vector, head_length=0.2):
        global y, x
        dots = self.get_dots(vector)
        X = dots[0]
        Y = dots[1]
        color = numpy.random.rand(3, )

        for i in range(1, 5):
            dx = X[i] - X[i - 1]
            dy = Y[i] - Y[i - 1]

            x = (2 * head_length) / math.sqrt(3) / 2.2
            y = head_length / math.sqrt(3) / 2.2

            x = -x if dx > 0 else x
            y = -y if dy > 0 else y
            print(x, y)
            self.ax.arrow(X[i - 1], Y[i - 1], dx + x, dy + y, head_length=head_length, width=0.02, facecolor=color,
                          edgecolor=color,
                          head_width=0.2,
                          overhang=-head_length / 2)

    def show_plot(self):
        plt.show()
