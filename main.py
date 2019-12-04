
from Plot import Plot
from Vector import Vector


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
    plot.setLimits()
    plot.drawUnitContour()
    plot.drawСontour(v1)
    plot.drawСontour(v2)
    plot.drawСontour(v3)
    plot.showPlot()


if __name__ == "__main__":
    main()
