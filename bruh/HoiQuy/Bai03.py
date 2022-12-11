from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def display():
    displayDemo()
    displayDes()


def displayDemo():
    m = 100
    X = 6 * np.random.rand(m, 1) - 3
    y = 0.5 * X ** 2 + X + 2 + np.random.randn(m, 1)
    X2 = X ** 2
    # print(X)
    # print(X2)
    X_poly = np.hstack((X, X2))
    # print(X_poly)

    lin_reg = linear_model.LinearRegression()
    lin_reg.fit(X_poly, y)
    print(lin_reg.intercept_)
    print(lin_reg.coef_)
    a = lin_reg.intercept_[0]
    b = lin_reg.coef_[0, 0]
    c = lin_reg.coef_[0, 1]
    print(a)
    print(b)
    print(c)

    x_ve = np.linspace(-3, 3, m)
    y_ve = a + b * x_ve + c * x_ve ** 2

    fig, ax = plt.subplots()

    ax.plot(X, y, 'o')
    ax.plot(x_ve, y_ve, 'r')

    # Tinh sai so
    loss = 0
    for i in range(0, m):
        y_mu = a + b * X_poly[i, 0] + c * X_poly[i, 1]
        sai_so = (y[i] - y_mu) ** 2
        loss = loss + sai_so
    loss = loss / (2 * m)
    print('loss = %.6f' % loss)

    # Tinh sai so cua scikit-learn
    y_train_predict = lin_reg.predict(X_poly)
    # print(y_train_predict)

    sai_so_binh_phuong_trung_binh = mean_squared_error(y, y_train_predict)
    print('sai so binh phuong trung binh: %.6f' % (sai_so_binh_phuong_trung_binh / 2))
    st.pyplot(fig)


def displayDes():
    st.header("Giải thích")
    st.markdown("""Hàm số $y ≈ f(x) = x^T w$ là một hàm tuyến tính theo cả $w$ và $x$. Trên thực tế, linear
regression có thể áp dụng cho các mô hình chỉ cần tuyến tính theo $w$. Ví dụ,

$y ≈ w_1x_1 + w_2x_2 + w_3x^2_1 + w4sin(x_2) + w_5x_1x_2 + w_0$

là một hàm tuyến tính theo $w$ và vì vậy cũng có thể được giải bằng linear regression.
Với mỗi vector đặc trưng $x = [x1, x2]^T$, chúng ta tính toán vector đặc trưng mới mới $x˜ = [x_1, x_2, x^2_1, sin(x_2), x_1x_2]^T$ rồi áp dụng linear regression với dữ liệu mới này. 

Tuy nhiên, việc tìm ra các hàm số $sin(x_2)$ hay $x_1x_2$ là tương đối không tự nhiên. 

**Hồi quy đa thức (polynomial regression)** thường được sử dụng nhiều hơn với các vector đặc trưng mới có dạng $[1, x_1, x^2_1, . . . ]^T$

Một ví dụ về hồi quy đa thức bậc 3 được thể hiện ở trên""")
