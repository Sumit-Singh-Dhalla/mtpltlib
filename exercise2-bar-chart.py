from matplotlib import pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(dev_x))
width = 0.25
dev_y = [35000, 37456, 36785, 37890, 40455, 40238, 41675, 42545, 42986, 43958, 43987]
py_dev_y = [45000, 47456, 47785, 48890, 49455, 50238, 51675, 53545, 53986, 53958, 54987]
js_dev_y = [40000, 42456, 42785, 42890, 43455, 45238, 46675, 47545, 47986, 48958, 49987]

plt.bar(x_indexes-width, dev_y, label="all dev", width=width)
plt.bar(x_indexes, py_dev_y, label="Python dev", width=width, color="g")
plt.bar(x_indexes+width, js_dev_y, label="JS dev", width=width)
plt.xlabel("ages")
plt.ylabel("Salary (INR)")
plt.title("Developer Salary (INR) as per ages")
plt.legend()
plt.xticks(ticks=x_indexes, labels=dev_x)
# plt.grid(True)
plt.show()
