import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



def executeThisFunction():
    x = np.linspace(-2, 2, 21)
    y = np.linspace(-2, 2, 21)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2
    plt.contour(X, Y, Z, 10)
    st.pyplot(plt)

if __name__ == "__main__":
    executeThisFunction()