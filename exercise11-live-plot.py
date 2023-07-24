from itertools import count

import pandas
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

index = count()
x, y = [], []

def animate(i):
    df = pandas.read_csv("dummy_data.csv")
    x = df["x_value"]
    y1 = df["total_1"]
    y2 = df["total_2"]

    plt.cla()
    plt.plot(x[-10:], y1[-10:], label="plot 1")
    plt.plot(x[-10:], y2[-10:], label="plot 2")
    plt.legend()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
