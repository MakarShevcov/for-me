import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.array([0.402, 0.322, 0.257, 0.208, 0.165])
y = np.array([0.2065, 0.1659, 0.1325, 0.1076, 0.0851])
def MNK(x, y):
    mpl.rcParams['font.size'] = 16
    plt.figure(figsize=(7, 7))
    plt.title(r"")
    plt.ylabel("$\Omega, с^{-1}$")
    plt.xlabel(r"$M, Нм$")
    xx = x*x
    yy = y*y
    xy = x*y
    k = (xy.mean())/(xx.mean())
    sigmak = ((xx.mean()* yy.mean() - xy.mean()*xy.mean()) / (len(x)*xx.mean()*xx.mean()))**0.5
    epsilonk = sigmak * 100/ k
    a1 = np.linspace(x.min()/10, x.max()+x.min()/10, 100)
    y1 = k * a1
    A = np.asarray([['k', 'sigmak', 'epsilonk'], [k, sigmak, epsilonk]])
    AT = A.T
    print(AT)
    plt.plot(x, y, 'r.')
    plt.plot(a1, y1, 'b')
    plt.errorbar(x, y, yerr=0.0004, xerr=0.0026, fmt='r.')
    plt.grid(which='major', axis='both', alpha=1)
    plt.grid(which='minor', axis='both', alpha=0.5)
    plt.show()
MNK(x,y)
