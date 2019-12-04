import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Vector import Vector


class Plot:
    def setLimits(self):
        plt.axes().set_xlim(-7, 7)
        plt.axes().set_ylim(-7, 7)
        plt.axes().set_aspect(1)

    def getDots(self, vector):
        result = []
        complexNumbers = [vector.rz1 + 0j, 0 + vector.iz1 * 1j, -vector.rz2 + 0j, 0 + vector.iz2 * -1j, vector.rz1 + 0j]
        X = [x.real for x in complexNumbers]
        Y = [x.imag for x in complexNumbers]
        result.append(X)
        result.append(Y)
        return result

    def drawUnitContour(self):
        dots = self.getDots(Vector(1, 1, 1, 1))
        plt.plot(dots[0], dots[1], color='red')
        # plt.scatter(X, Y, color='red')

    def drawСontour(self, vector):
        dots = self.getDots(vector)
        X = dots[0]
        Y = dots[1]
        style = "Simple,tail_width=0.01,head_width=3,head_length=3"
        kw = dict(arrowstyle=style, color=numpy.random.rand(3,))
        for i in range(0, 4):
            arrow = patches.FancyArrowPatch((X[i], Y[i]), (X[i + 1], Y[i + 1]), **kw)
            plt.gca().add_patch(arrow)


    def showPlot(self):
        plt.show()
