import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2
#
# def draw(x, y):
#     plt.plot(x, y)
#     plt.xlabel("X values")
#     plt.ylabel("Y values")
#     plt.title("My graph")
#     plt.show()
#
# draw(x, y)

# def sub_plot(x, y):
#     plt.subplot(1, 2, 1)
#     plt.plot(x, y, 'r')
#
#     plt.subplot(1, 2, 2)
#     plt.plot(x**5, y**5, 'b')
#     plt.show()
#
# sub_plot(x, y)

# OBJECT ORIENTED:

def object_oriented(x, y):
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(x, y)
    axes.set_xlabel("X values")
    axes.set_ylabel("Y values")
    axes.set_title("Object Oriented")
    plt.legend()
    plt.show()

object_oriented(x, y)


def nested(x, y):
    fig = plt.figure()
    axis_one = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axis_two = fig.add_axes([0.2, 0.5, 0.4, 0.3])
    # axis one lables
    axis_one.set_xlabel("X values")
    axis_one.set_ylabel("Y values")
    axis_one.set_title("Nested plots")

    axis_one.plot(x, y)


    #axis two labels
    axis_two.set_xlabel("xxx")
    axis_two.set_ylabel("yyy")
    axis_two.set_title("Inner plot")


    axis_two.plot(y, x)
    plt.show()

nested(x, y)



