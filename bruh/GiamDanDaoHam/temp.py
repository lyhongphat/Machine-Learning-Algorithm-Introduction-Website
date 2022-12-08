import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import streamlit as st

def executeThisFunction():
    ax = plt.axes(projection="3d")

    X = np.linspace(-2, 2, 21)
    Y = np.linspace(-2, 2, 21)
    X, Y = np.meshgrid(X, Y)
    Z = X * X + Y * Y
    ax.plot_wireframe(X, Y, Z)
    st.pyplot(plt)


if __name__ == "__main__":
    executeThisFunction()