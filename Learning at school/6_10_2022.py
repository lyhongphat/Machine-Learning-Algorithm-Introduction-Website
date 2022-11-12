import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression

N = 1000

np.random.seed(100)
X = np.random.rand(N)
y = 4 + 3 * X + .5*np.random.randn(N)  # noise added

model = LinearRegression()
model.fit(X.reshape(-1, 1), y.reshape(-1, 1))

w, b = model.coef_[0][0], model.intercept_[0]
print('b = %f \nw = %f' % (b, w))

ones = np.ones((X.shape[0], 1))
Xbar = np.concatenate((ones, X.reshape(-1, 1)), axis=1)

A = 1000/(2*N)
B = np.sum(X**2)/(2*N)
C = -2*np.sum(y)/(2*N)
D = -2*np.sum(X*y)/(2*N)
E = 2*np.sum(X)/(2*N)
F = np.sum(y**2)/(2*N)

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w))**2

def myGD(w_init, grad, eta):
    w = [w_init]
    for it in range(100):
        w_new = w[-1] - eta*grad(w[-1])
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
            break
        w.append(w_new)
    return (w, it)

one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one, X.reshape(-1, 1)), axis = 1)
w_init = np.array([[2], [1]])
(w1, it1) = myGD(w_init, grad, 1)
print('Sol found by GD: w = ’, w1[-1].T, ’,\nafter %d iterations.' %(it1+1))


b = np.linspace(-2,2,20)
w = np.linspace(-2,2,20)

b,w = np.meshgrid(b,w)
Z = A*b**2 + B*w**2 + C*b + D*w + E*b*w + F

ax = plt.axes(projection='3d')
ax.plot_wireframe(b,w,Z)
plt.show()