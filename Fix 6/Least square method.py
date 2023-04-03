import numpy as np
import matplotlib.pyplot as plt

def data():
    VY = [2.23, 2.29, 2.27, 2.62, 2.72, 2.82, 3.13, 3.49, 3.82, 3.95, 4.22, 4.48, 5.06, 5.50, 5.68, 6.19, 6.42,
          7.04, 7.57, 8.10]
    VX = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
    return VX, VY

def approximation(X, Y, m):
    A = np.array([[np.sum([np.power(X[t], j) for t in range(0, len(X))])
                   for j in range(i, i+m+1)] for i in range(0, m+1)])
    B = np.array([np.sum([np.power(X[j], i)*Y[j] for j in range(0, len(X))])
                  for i in range(0, m+1)])
    return np.linalg.solve(A, B)

def predict(x, p):
    return np.sum([p[i]*np.power(x, i) for i in range(len(p))])

def error(t, s):
    return (np.sqrt(np.sum(np.power((t-s),2))/len(t)))

def stdev():
    err = []
    for i in range(20):
        p = approximation(VX, VY, i+1)
        err.append(error(np.array([predict(VX[j], p) for j in range(len(VX))]),VY))
    return err


def chart1():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p1 = approximation(VX, VY, 1)
    p2 = approximation(VX, VY, 2)
    p3 = approximation(VX, VY, 3)
    plt.plot(x, np.array([predict(x[i], p1) for i in range(len(x))]), '-b', label = 'm = 1')
    plt.plot(x, np.array([predict(x[i], p2) for i in range(len(x))]), '-g', label = 'm = 2')
    plt.plot(x, np.array([predict(x[i], p3) for i in range(len(x))]), '--y', label = 'm = 3')
    plt.legend()
    plt.grid()
    plt.show()

def chart2():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p4 = approximation(VX, VY, 4)
    p5 = approximation(VX, VY, 5)
    p6 = approximation(VX, VY, 6)
    plt.plot(x, np.array([predict(x[i], p4) for i in range(len(x))]), '-b', label='m = 4')
    plt.plot(x, np.array([predict(x[i], p5) for i in range(len(x))]), '-g', label='m = 5')
    plt.plot(x, np.array([predict(x[i], p6) for i in range(len(x))]), '--y', label='m = 6')
    plt.legend()
    plt.grid()
    plt.show()

def chart3():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p7 = approximation(VX, VY, 7)
    p8 = approximation(VX, VY, 8)
    plt.plot(x, np.array([predict(x[i], p7) for i in range(len(x))]), '-b', label='m = 4')
    plt.plot(x, np.array([predict(x[i], p8) for i in range(len(x))]), '--g', label='m = 5')
    plt.legend()
    plt.grid()
    plt.show()


def chart4():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    plt.ylim(0, 8)
    lin.plot(VX, VY, '*r')
    p11 = approximation(VX, VY, 11)
    plt.plot(x, np.array([predict(x[i], p11) for i in range(len(x))]), '-b', label='m = 10')
    plt.legend()
    plt.grid()
    plt.show()


VX, VY = data()
print(stdev()[6])
chart3()
