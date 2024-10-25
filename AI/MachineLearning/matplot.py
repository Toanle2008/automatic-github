import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt(r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\univariate.txt", delimiter=",")
theta = np.loadtxt(r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\univariate_theta.txt", delimiter=",")

y = np.copy(x[:, -1])
x[:, 1] = x[:, 0]
x[:, 0] = 1

predict = x@theta * 10000
# print("%d persons: %.2f$" %(x[0,1]*10000, predict[0]) )
# print("{} persons: {}$".format(x[0,1]*10000, predict[0]))

plt.plot(x[:, 1:], y, "rx")
# plt.plot(predict/10000,y,"-b")
plt.show()
















