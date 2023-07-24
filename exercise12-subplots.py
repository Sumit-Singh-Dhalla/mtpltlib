from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [35000, 37456, 36785, 37890, 40455, 40238, 41675, 42545, 42986, 43958, 43987]
py_dev_y = [45000, 47456, 47785, 48890, 49455, 50238, 51675, 53545, 53986, 53958, 54987]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
# print(ax)

ax1.plot(dev_x, dev_y, label="All Dev")
ax1.set_title("All Dev Salaries")
ax1.set_ylabel("Salaries(INR)")

ax2.plot(dev_x, py_dev_y, label="Python Dev")
ax2.set_xlabel("Ages")
ax2.set_ylabel("Salaries(INR)")
plt.show()
