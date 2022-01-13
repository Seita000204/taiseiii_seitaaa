import numpy

a = numpy.array((1, 2, 3, 4))
b = numpy.array((4, 3, 2, 1))

print(numpy.linalg.norm(a-b))