import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.array([])
y = np.array([])

def MNK(x, y):
  """
  строит график методом наименьших квадратов
  """
    mpl.rcParams['font.size'] = 16
    plt.figure(figsize=(7, 7))
    plt.title(r"")
    plt.ylabel("$T^{2} a$")
    plt.xlabel(r"$a^2$")
    xy = x*y
    xx = x*x
    yy = y*y
    k = (xy.mean()-x.mean()*y.mean())/(xx.mean()-x.mean()*x.mean())
    b = y.mean() - k * x.mean()
    sigmak = ((yy.mean() - y.mean() * y.mean()) / (xx.mean() - x.mean() * x.mean()) - k ** 2) / (len(x) - 2)
    sigmab = sigmak * (xx.mean() - x.mean() * x.mean()) ** 0.5
    epsilonk = sigmak * 100/ k
    epsilonb = sigmab * 100/ b
    a1 = np.linspace(x.min()/10, x.max()+x.min()/10, 100)
    y1 = k * a1 + b
    A = np.asarray([['k', 'b', 'sigmak', 'sigmab', 'epsilonk', 'epsilonb'], [k, b, sigmak, sigmab, epsilonk, epsilonb]])
    A1 = A.T
    print(A1)
    plt.plot(x, y, 'r.')
    plt.plot(a1, y1, 'b')
    plt.errorbar(x, y, yerr=0.0065, xerr=0.002, fmt='r.')
    plt.grid(which='major', axis='both', alpha=1)
    plt.grid(which='minor', axis='both', alpha=0.5)
    plt.show()

MNK(x,y)
