from subprocess import call


def open_my_file(fileOpen):
    call(["python", fileOpen])


import streamlit as st
from streamlit_option_menu import option_menu

import bruh.GiamDanDaoHam.Bai01 as GDDH_01
import bruh.GiamDanDaoHam.Bai02 as GDDH_02
import bruh.GiamDanDaoHam.Bai02a as GDDH_2a
import bruh.GiamDanDaoHam.Bai03 as GDDH_03
import bruh.GiamDanDaoHam.Bai04 as GDDH_04
import bruh.GiamDanDaoHam.Bai05 as GDDH_05
import bruh.GiamDanDaoHam.temp as GDDH_temp
import bruh.GiamDanDaoHamMomentum.Bai01 as GDDHM_01


class Main():
    def __init__(self):
        self.initUI()

    def initUI(self):
        with st.sidebar:
            selected = option_menu("Main Menu",
                                   [
                                       "Linear regression",
                                       "Overfitting",
                                       'Gradient descent',
                                       'Gradient descent momentum',
                                       "KNN",
                                       "SVM",
                                       "End to end project"],
                                   icons=['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣'],
                                   menu_icon="cast", default_index=1)
            selected

        if selected == "End to end project":
            import bruh.End_to_End_Project.Sumary
            bruh.End_to_End_Project.Sumary.display()

        elif selected == 'Gradient descent':
            st.title("Giam dan dao ham")
            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", 'Bai02', "Bai02a", "Bai03", "Bai04", "Bai05", "Temp"))

                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
                if option == "Bai01":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai02":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai02a":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai03":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai04":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai05":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Temp":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")

            with col2:
                if option == "Bai01":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_01.executeThisFunction()
                if option == "Bai02":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_02.executeThisFunction()
                if option == "Bai02a":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_2a.executeThisFunction()
                if option == "Bai03":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_03.executeThisFunction()
                if option == "Bai04":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_04.executeThisFunction()
                if option == "Bai05":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_05.executeThisFunction()
                if option == "Temp":
                    # self.onGiamDanDaoHamBai01()
                    GDDH_temp.executeThisFunction()

        elif selected == 'Gradient descent momentum':
            st.title("Giam dam dao ham momentum")

            # click = st.button('Negative')
            # if click:
            #     st.text("Click there!")
            # st.button('Logarit')
            # st.button('Power')
            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01"))

                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
                if option == "Bai01":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
            with col2:
                if option == "None":
                    st.write("")
                if option == "Bai01":
                    # self.onGiamDanDaoHamBai01()
                    GDDHM_01.executeThisFunction()


        elif selected == 'Linear regression':
            import bruh.HoiQuy.Sumary as sum
            sum.display()

        # ============================================================================
        elif selected == 'KNN':
            st.title("KNN")

        # ============================================================================
        elif selected == 'Overfitting':
            from bruh.Overfitting import Sumary
            Sumary.display()

        # ============================================================================
        elif selected == 'SVM':
            st.title("SVM")

        # ============================================================================
        else:
            st.title('Nhận diện phép toán')

        # st.file_uploader("Hello", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False, label_visibility="visible")

    # def run(runfile):
    #     with open(runfile, "r") as rnf:
    #         exec(rnf.read())

    def onGiamDanDaoHamBai01(self):
        open_my_file("GiamDanDaoHam\\Bai01.py")


p = Main()
