import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(start=-3, stop=3, num=200)

exponential_positive_x = numpy.exp(x)
exponential_negative_x = numpy.exp(-x)
linear_y = x
logarithmic_y = numpy.log(x)

exp_positive_x = plt.plot(x, exponential_positive_x, 'k.', label='Positive Exponential', markersize=3)
linear = plt.plot(x, linear_y, 'kx', label = 'Linear', markersize=3)
logarithmic = plt.plot(x, logarithmic_y, 'k-',label='Logarithmic', markersize=2.5)
plt.grid()
plt.legend()
plt.figure()

plt.plot(x, exponential_positive_x, 'k.', label = 'Positive Exponential')
plt.plot(x, exponential_negative_x, 'k-', label='Negative Exponential')
plt.legend()
plt.grid()
plt.show()
