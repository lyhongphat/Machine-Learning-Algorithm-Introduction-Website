from subprocess import call


def open_my_file(fileOpen):
    call(["python", fileOpen])


import streamlit as st
from streamlit_option_menu import option_menu


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

        # ============================================================================
        elif selected == 'Gradient descent':
            import bruh.GiamDanDaoHam.Sumary
            bruh.GiamDanDaoHam.Sumary.display()

        # ============================================================================
        elif selected == 'Gradient descent momentum':
            import bruh.GiamDanDaoHamMomentum.Sumary
            bruh.GiamDanDaoHamMomentum.Sumary.display()

        # ============================================================================
        elif selected == 'Linear regression':
            import bruh.HoiQuy.Sumary
            bruh.HoiQuy.Sumary.display()

        # ============================================================================
        elif selected == 'KNN':
            st.title("KNN")

        # ============================================================================
        elif selected == 'Overfitting':
            from bruh.Overfitting import Sumary
            Sumary.display()

        # ============================================================================
        elif selected == 'SVM':
            import bruh.SVM.Sumary
            bruh.SVM.Sumary.display()

        # ============================================================================
        else:
            st.title('')

        # st.file_uploader("Hello", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False, label_visibility="visible")

    # def run(runfile):
    #     with open(runfile, "r") as rnf:
    #         exec(rnf.read())


p = Main()
