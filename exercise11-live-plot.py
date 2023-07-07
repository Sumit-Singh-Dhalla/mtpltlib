import random
from datetime import datetime
from itertools import count

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("seaborn")

x = []
y = []
index = count()


def animate(i):
    x.append(next(index))
    y.append(random.randint(-10, 10))

    plt.cla()
    plt.plot(x[-10:], y[-10:])
    plt.axhline(0, color="black")
    plt.ylim(-10, 10)
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
