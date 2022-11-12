import numpy as np
from matplotlib import pyplot as plt

def circle(x_Circles, y_Circles):
    r = 0.5
    circle = plt.Circle((x_Circles + 0.5, y_Circles + 0.5), r, color='red')
    plt.gca().add_patch(circle)
    return

def vector(xBegin, yBegin, xEnd, yEnd):
    plt.quiver(xBegin + 0.5, yBegin + 0.5, xEnd, yEnd, color="black", scale_units='xy', scale=5)
    return

def draw(x1):
    y1 = x1 ** 2 + 10 * np.sin(x1)
    dx = 1
    dy = 2 * x1 + 10 * np.cos(x1)
    if dy > 0:
        dy = -dy
    circle(x1, y1)
    vector(x1, y1, dx, dy)
    return

def main():
    X = np.linspace(-5, 5, 1000)
    y = X ** 2 + 10 * np.sin(X)

    plt.figure(figsize=(10, 10), dpi=80)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(X, y)

    draw(-3.5)
    # draw(0)

    plt.fill_between(x, y, -10)
    plt.axis([-6, 6, -10, 40])
    plt.show()


if __name__ == "__main__":
    main()