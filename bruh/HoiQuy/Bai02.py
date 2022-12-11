from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def display():
    displayDemo()
    st.header("Giải thích")
    displayDes()


def displayDemo():
    # height (cm), input Data, each row is a Data point
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
    y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

    regr = linear_model.LinearRegression()
    regr.fit(X, y)  # in scikit-learn, each sample is one row
    # Compare two results
    print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)

    fig, ax = plt.subplots()

    X = X[:, 0]
    ax.plot(X, y, 'ro')
    a = regr.coef_[0]
    b = regr.intercept_
    x1 = X[0]
    y1 = a * x1 + b
    x2 = X[12]
    y2 = a * x2 + b
    x = [x1, x2]
    y = [y1, y2]

    ax.plot(x, y)
    st.pyplot(fig, clear_figure=True)


def displayDes():
    st.markdown \
        ("""
        ### Bảng dữ liệu

Ta có bảng dữ liệu từ ví dụ 1

| Chiều cao | 147 | 150 | 153 | 158 | 163 | 165 | 168 | 170 | 173 | 175 | 178 | 180 | 183 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cân nặng | 49 | 50 | 51 | 54 | 58 | 59 | 60 | 62 | 63 | 64 | 66 | 67 | 68 |

### Tính các hệ số

Chúng ta sẽ sử dụng thư viện scikit-learn để tìm nghiệm.

```python
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets, linear_model
# fit the model by Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, y) # in scikit-learn, each sample is one row
# Compare two results
print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)
print("our solution : w_1 = ", w[1], "w_0 = ", w[0])
```
        """)
    st.subheader("Output:")
    st.write \
        ("""
        scikit-learn solution : w_1 = [ 0.55920496] w_0 = [-33.73541021]\n
our solution : w_1 = [ 0.55920496] w_0 = [-33.73541021]
        """)

    st.markdown("""### Biểu diễn ra biểu đồ bằng mathplotlib

```python
fig, ax = plt.subplots()

X = X[:, 0]
ax.plot(X, y, 'ro')
a = regr.coef_[0]
b = regr.intercept_
x1 = X[0]
y1 = a * x1 + b
x2 = X[12]
y2 = a * x2 + b
x = [x1, x2]
y = [y1, y2]

ax.plot(x, y)
```""")


