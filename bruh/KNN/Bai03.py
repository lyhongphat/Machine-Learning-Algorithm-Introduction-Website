import joblib
import os
import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from tensorflow import keras

import streamlit as st
import os
from PIL import Image

def hehe():
    mnist = keras.datasets.mnist
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    # 784 = 28x28
    RESHAPED = 784
    X_train = X_train.reshape(60000, RESHAPED)
    X_test = X_test.reshape(10000, RESHAPED)

    # now, let's take 10% of the training Data and use that for validation
    (trainData, valData, trainLabels, valLabels) = train_test_split(X_train, Y_train, test_size=0.1, random_state=84)

    model = KNeighborsClassifier()
    model.fit(trainData, trainLabels)

    # save model, sau này ta sẽ load model để dùng
    # if os.path.exists("bruh/KNN/Model/knn_mnist.pkl"):
    #     os.remove("bruh/KNN/Model/knn_mnist.pkl")
    joblib.dump(model, "bruh/KNN/knn_mnist.pkl")

    # Đánh giá trên tập validation
    predicted = model.predict(valData)
    do_chinh_xac = accuracy_score(valLabels, predicted)
    print('Độ chính xác trên tập validation: %.0f%%' % (do_chinh_xac * 100))

    # Đánh giá trên tập test
    predicted = model.predict(X_test)
    do_chinh_xac = accuracy_score(Y_test, predicted)
    print('Độ chính xác trên tập test: %.0f%%' % (do_chinh_xac * 100))


def executeThisFunction():
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "../assets/images/KNN/digit.jpg")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)

    filepath = os.path.join(currentDir, "../assets/images/KNN/so0.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)


    code = '''mnist = keras.datasets.mnist
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()'''
    st.code(code, language="python")
    st.write("Bộ MNIST là một tập hợp lớn các chữ số viết tay. Nó là một bộ dữ liệu rất phổ biến trong lĩnh vực xử lý hình ảnh.")

    code = '''joblib.dump(model, "bruh/KNN/knn_mnist.pkl")'''
    st.code(code, language="python")
    st.write("save model, sau này ta sẽ load model để dùng")

    code = '''X_train = X_train.reshape(60000, RESHAPED)
    X_test = X_test.reshape(10000, RESHAPED)'''
    st.code(code, language="python")
    st.write("Phương thức reshape() là thay đổi hình dạng của một mảng, chuyển đổi dữ liệu từ dạng rộng sang dạng dài và ngược lại")

    code = '''predicted = model.predict(valData)
    do_chinh_xac = accuracy_score(valLabels, predicted)
    print('Độ chính xác trên tập validation: %.0f%%' % (do_chinh_xac * 100))'''
    st.code(code, language="python")
    st.write("Đánh giá trên tập validation")

    code = '''predicted = model.predict(X_test)
    do_chinh_xac = accuracy_score(Y_test, predicted)
    print('Độ chính xác trên tập test: %.0f%%' % (do_chinh_xac * 100))'''
    st.code(code, language="python")
    st.write("Đánh giá trên tập test")



