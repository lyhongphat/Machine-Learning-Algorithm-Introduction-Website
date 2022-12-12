from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn import datasets
from skimage import exposure
import numpy as np

import sklearn
import streamlit as st
import os
from PIL import Image
def executeThisFunction():
    # take the MNIST Data and construct the training and testing split, using 75% of the
    # Data for training and 25% for testing
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "../assets/images/KNN/digit.jpg")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    mnist = datasets.load_digits()
    (trainData, testData, trainLabels, testLabels) = train_test_split(np.array(mnist.data),
                                                                      mnist.target, test_size=0.25, random_state=42)

    # now, let's take 10% of the training Data and use that for validation
    (trainData, valData, trainLabels, valLabels) = train_test_split(trainData, trainLabels,
                                                                    test_size=0.1, random_state=84)

    print("training Data points: ", len(trainLabels))
    print("validation Data points: ", len(valLabels))
    print("testing Data points: ", len(testLabels))
    st.write("testing Data points: ", len(testLabels))
    st.write("training Data points: ", len(trainLabels))
    st.write("validation Data points: ", len(valLabels))
    model = KNeighborsClassifier()
    model.fit(trainData, trainLabels)
    # evaluate the model and update the accuracies list
    score = model.score(valData, valLabels)
    print("accuracy = %.2f%%" % (score * 100))
    st.write("accuracy = %.2f%%" % (score * 100))

    # loop over a few random digits
    for i in list(map(int, np.random.randint(0, high=len(testLabels), size=(5,)))):
        # grab the image and classify it
        image = testData[i]
        prediction = model.predict(image.reshape(1, -1))[0]

        # convert the image for a 64-dim array to an 8 x 8 image compatible with OpenCV,
        # then resize it to 32 x 32 pixels so we can see it better
        image = image.reshape((8, 8)).astype("uint8")

        image = exposure.rescale_intensity(image, out_range=(0, 255))
        # image = imutils.resize(image, width=32, inter=cv2.INTER_CUBIC)

        # show the prediction
        print("I think that digit is: {}".format(prediction))
        st.write("I think that digit is: {}".format(prediction))
        # cv2.imshow("Image", image)
        # img_array = np.array(image)
        # cv2.imwrite('digitOut.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        # image = Image.open('digitOut.jpg')
        # st.image(image, caption='Output', use_column_width=True)
        # st.pyplot(image)


    code = '''mnist = datasets.load_digits()'''
    st.code(code, language ="python")
    st.write("Hàm load_digits() giúp tải và trả về tập dữ liệu chữ số. Phân loại này chứa các điểm dữ liệu, trong đó mỗi điểm dữ liệu là một hình ảnh 8X8 của một chữ số")

    code = '''(trainData, testData, trainLabels, testLabels) = train_test_split(np.array(mnist.data),
                                                            mnist.target, test_size=0.25, random_state=42)'''
    st.code(code, language="python")
    st.write("train_test_split là một chức năng trong lựa chọn mô hình Sklearn để chia mảng dữ liệu thành hai tập hợp con: dành cho dữ liệu huấn luyện và dữ liệu thử nghiệm. Với chức năng này, bạn không cần phải chia tập dữ liệu theo cách thủ công.")

    code = '''score = model.score(valData, valLabels)'''
    st.code(code, language="python")
    st.write("Điểm mô hình là một toán tử AI Studio lưu trữ giá trị được dự đoán bởi mô hình học tập có giám sát cho trường mục tiêu.")


