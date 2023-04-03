import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def data():
    VY = [2.23, 2.29, 2.27, 2.62, 2.72, 2.82, 3.13, 3.49, 3.82, 3.95, 4.22, 4.48, 5.06, 5.50, 5.68, 6.19, 6.42, 7.04, 7.57, 8.10]
    VX = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
    return VY, VX

def chart():
    VY, VX = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    pf = np.polyfit(VX, VY, 1)  # [3.10406015 1.22073684]
    pv = np.polyval(pf, VX)  # 1.53114286 1.84154887 2.15195489 2.4623609  2.77276692 3.08317293 3.39357895 3.70398496 4.01439098 4.32479699 4.63520301 4.94560902 5.25601504 5.56642105 5.87682707 6.18723308 6.4976391  6.80804511 7.11845113 7.42885714
    lin.plot(VX, VY, '*r')
    lin.plot(VX, pv, '-b')
    lin.set_title('Линейная регрессия')
    plt.grid()
    plt.show()

chart()

