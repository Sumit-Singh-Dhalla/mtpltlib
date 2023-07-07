from matplotlib import pyplot as plt


dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [35000, 37456, 36785, 37890, 40455, 40238, 41675, 42545, 42986, 43958, 43987]
py_dev_y = [45000, 47456, 47785, 48890, 49455, 50238, 51675, 53545, 53986, 53958, 54987]


plt.plot(dev_x, dev_y, label="All Dev", c="r")
plt.plot(dev_x, py_dev_y, label="Python", c="g")
plt.xlabel("Ages")
plt.ylabel("salaries(INR)")
plt.title("Dev salaries as per their ages")
plt.legend()
plt.grid()
plt.show()















"""

plt.style.use("fivethirtyeight")
plt.xkcd()
py_dev_y = [45000, 47456, 47785, 48890, 49455, 50238, 51675, 53545, 53986, 53958, 54987]
plt.plot(dev_x, py_dev_y, label="Python dev")
plt.xlabel("ages")
plt.ylabel("Salary (INR)")
plt.title("Developer Salary (INR) as per ages")

plt.legend()
plt.grid(True)
"""