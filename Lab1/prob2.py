import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(start=-numpy.pi, stop=numpy.pi, num=700)
sin_x = numpy.sin(x)
sin_5x = numpy.sin(5 * x)
sin_10x = numpy.sin(10 * x)

plt.plot(x, sin_x, 'b+', label='k = 1', markersize=2)
plt.plot(x, sin_10x, 'C1x', label='k = 10', markersize=4)
plt.plot(x, sin_5x, 'g-',label='k = 5', markersize=1)
plt.legend()
plt.grid()
plt.figure()

plt.plot(x, sin_x, 'b-',label='sin(x)', markersize=1)
plt.plot(x, sin_x ** 2, 'g*',label='sin(x) * sin(x)', markersize=0.75)
plt.legend()
plt.grid()

plt.show()


