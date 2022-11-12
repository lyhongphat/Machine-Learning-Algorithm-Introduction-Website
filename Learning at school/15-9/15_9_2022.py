import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

np.random.seed(100)

N = 30
X = np.random.rand(N,1)*5
y = 3*(X - 2) * (X-3)*(X-4) + 10*np.random.rand(N,1)
# giá trị mẫu

N_test = 20
X_test = (np.random.rand(N_test,1) - 1/8) *10
y_test = 3*(X_test - 2) * (X_test - 3)*(X_test-4) + 10*np.random.randn(N_test, 1)
# bộ giá trị test

poly_features = PolynomialFeatures(degree=16, include_bias=True)

X_poly = poly_features.fit_transform(X)
X_poly_test = poly_features.fit_transform(X_test)

lin_reg = linear_model.LinearRegression(fit_intercept=False)
lin_reg.fit(X_poly,y)

x_draw = np.linspace(0,8,1000)
y_draw = np.zeros(1000, dtype=np.float64)

x_draw_poly = poly_features.fit_transform(np.array([x_draw]).T)
y_draw = np.matmul(x_draw_poly, lin_reg.coef_.T)

y_real = 3*(x_draw - 2) * (x_draw-3)*(x_draw-4)

# Sai số trainning
y_train_predict = lin_reg.predict(X_poly)
meanSquaredError = mean_squared_error(y,y_train_predict)
print("Sai so binh phuong trung binh: %.6f" %(meanSquaredError/2))

# Sai số test
y_train_predict_test = lin_reg.predict(X_poly_test)
meanSquaredError_test = mean_squared_error(y_test,y_train_predict_test)
print("Sai so binh phuong trung binh (test): %.6f" %(meanSquaredError_test/2))

plt.axis([-4, 10, np.amin(y_test) - 10, np.amax(y) + 10])
plt.plot(X,y,'ro')
plt.plot(X_test,y_test,'s')
plt.plot(x_draw,y_draw,'b')
plt.plot(x_draw,y_real,'--')
plt.show()

