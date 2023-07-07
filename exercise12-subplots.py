from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [35000, 37456, 36785, 37890, 40455, 40238, 41675, 42545, 42986, 43958, 43987]
py_dev_y = [45000, 47456, 47785, 48890, 49455, 50238, 51675, 53545, 53986, 53958, 54987]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(dev_x, dev_y, label="all dev")
ax1.set_title("Developer Salary (INR) as per ages")
ax1.set_ylabel("Salary (INR)")

ax2.plot(dev_x, py_dev_y, label="Python dev")
ax2.set_xlabel("ages")
ax2.set_ylabel("Salary (INR)")
# plt.legend()
plt.show()
