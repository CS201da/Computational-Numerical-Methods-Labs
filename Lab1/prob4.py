import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(start=0, stop=2, num=200000)
y = x * numpy.log(x)
derivative = 1 + numpy.log(x)
plt.plot(x[1:], y[1:], label='xlnx')
plt.legend()
plt.title('y=xlnx for 0 < x < 2')
plt.grid()
plt.figure()
x = numpy.linspace(start=0, stop=50, num=200000)
y = x * numpy.log(x)
plt.plot(x, y, label='xlnx')
plt.title('y=xlnx at large values of x')
plt.legend()
plt.grid()
plt.show()
