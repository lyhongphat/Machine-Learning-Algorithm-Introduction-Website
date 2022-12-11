from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)
N = 150


def executeThisFunction():
    centers = [[2, 3], [5, 5], [1, 8]]
    n_classes = len(centers)
    data, labels = make_blobs(n_samples=N,
                              centers=np.array(centers),
                              random_state=1)

    nhom_0 = []
    nhom_1 = []
    nhom_2 = []

    for i in range(0, N):
        if labels[i] == 0:
            nhom_0.append([data[i, 0], data[i, 1]])
        elif labels[i] == 1:
            nhom_1.append([data[i, 0], data[i, 1]])
        else:
            nhom_2.append([data[i, 0], data[i, 1]])

    nhom_0 = np.array(nhom_0)
    nhom_1 = np.array(nhom_1)
    nhom_2 = np.array(nhom_2)
    plt.plot(nhom_0[:, 0], nhom_0[:, 1], 'og', markersize=2)
    plt.plot(nhom_1[:, 0], nhom_1[:, 1], 'or', markersize=2)
    plt.plot(nhom_2[:, 0], nhom_2[:, 1], 'ob', markersize=2)
    plt.legend(['Nhom 0', 'Nhom 1', 'Nhom 2'])
    # plt.show()
    st.pyplot(plt)

    res = train_test_split(data, labels,
                           train_size=0.8,
                           test_size=0.2,
                           random_state=1)

    train_data, test_data, train_labels, test_labels = res
    # default k = n_neighbors = 5
    #         k = 3
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_data, train_labels)
    predicted = knn.predict(test_data)
    sai_so = accuracy_score(test_labels, predicted)
    print('sai so:', sai_so)
    st.write("Sai số:", sai_so)

    my_test = np.array([[2.5, 4.0]])
    ket_qua = knn.predict(my_test)
    st.write('Kết quả nhận đang là nhóm:', ket_qua[0])

    code = '''data, labels = make_blobs(n_samples=N,
                              centers=np.array(centers),
                              random_state=1)'''
    st.code(code, language="python")
    st.write("Hàm make_blobs() có thể được sử dụng để tạo các đốm màu với phân phối Gaussian.")

    code = '''    for i in range(0, N):
        if labels[i] == 0:
            nhom_0.append([data[i, 0], data[i, 1]])
        elif labels[i] == 1:
            nhom_1.append([data[i, 0], data[i, 1]])
        else:
            nhom_2.append([data[i, 0], data[i, 1]])'''
    st.code(code, language="python")
    st.write("Tiến hành gán giá trị cho các mảng label")

    code = '''knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_data, train_labels)
    predicted = knn.predict(test_data)
    sai_so = accuracy_score(test_labels, predicted)'''
    st.code(code, language="python")
    st.write("Để sử dụng thuật toán KNN, chỉ cần tạo một phiên bản của KNeighborsClassifier là đủ")
    st.write("Khi một dự đoán được đưa ra, KNN sẽ so sánh đầu vào với dữ liệu huấn luyện mà nó đã lưu trữ. Nhãn lớp của điểm dữ liệu có độ tương tự tối đa với đầu vào được truy vấn được đưa ra dưới dạng dự đoán.")
    st.write("Sử dụng knn.predict() để dự đoán và lưu kết quả vào biến predicted, từ đó tính được sự sai đó trong lần sự đoán đó")

# if __name__ == '__main__':
#     main()
