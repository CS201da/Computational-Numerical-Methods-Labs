import numpy
import matplotlib.pyplot as plt

a = 1
mu = 0

y0 = 1
x = numpy.linspace(start=-5, stop=5, num=300)
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'b.', label='y0 = 1', markersize = 1)

y0 = 10
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'C1x', label='y0 = 10')

y0 = 20
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'g-', label='y0 = 20')

plt.title('Variation in y0')
plt.grid()
plt.legend()
plt.figure()

a = 1
mu = 0
y0 = 1
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'b.', label='a = 1')

a = 10
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'C1x', label='a = 10')

a = 20
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'g-', label='a = 20')

plt.title('Variation in a')
plt.grid()
plt.legend()
# plt.show()

plt.figure()

a = 1
mu = 0
y0 = 1
x = numpy.linspace(start=-20, stop=20, num=1000)
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'b.', label='mu = 0')

mu = 10
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'C1x', label='mu = 10')

mu = -10
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
plt.plot(x, gaussian, 'g-', label='mu = -10')

plt.title('Variation in mu')
plt.legend()
plt.grid()

plt.figure()

# Lorentz function y = 1 / 1 + x^2
x = numpy.linspace(start=-10, stop=10, num=1000)
y0 = 1
a = 1
mu = 0
gaussian = y0 * numpy.exp(-a * ((x - mu) ** 2))
lorentz = 1 / (1 + x ** 2)
plt.plot(x, gaussian, label='Gaussian')
plt.plot(x, lorentz, label='Lorentz')
plt.legend()
plt.grid()
plt.title('Lorentz vs Gaussian')

plt.figure()
plt.plot(x, lorentz - gaussian)
plt.title('Difference in Lorentz and Gaussian function')
plt.show()
