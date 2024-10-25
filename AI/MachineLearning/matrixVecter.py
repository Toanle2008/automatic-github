import numpy as np
# a = [[1,2,3], [4,5,6], [7,8,9]]
# b = [10,11,12]
# path = r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\text.txt"
# loadFile = np.loadtxt(path, delimiter=",")
# # print(loadFile[:3, 1:])
# np.savetxt(r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\save.txt", loadFile, fmt="%.3f", delimiter=" , ")
x = np.loadtxt(r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\univariate.txt", delimiter=",")
theta = np.loadtxt(r"C:\Users\wibun\OneDrive\Desktop\code\AI\MachineLearning\univariate_theta.txt", delimiter=",")

y = np.copy(x[:, -1])
x[:, 1] = x[:, 0]
x[:, 0] = 1

predict = x@theta * 10000
# print("%d persons: %.2f$" %(x[0,1]*10000, predict[0]) )
print("{} persons: {}$".format(x[0,1]*10000, predict[0]))
