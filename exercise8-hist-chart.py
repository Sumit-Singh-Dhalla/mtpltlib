from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

axes = [34, 23, 56, 34, 67, 32, 67, 19, 45, 65]

plt.hist(axes, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], edgecolor="black")
plt.axvline(40, color="#fc4f30")
plt.axhline(2, color="#fc4f30")
plt.xlabel("ages")

plt.title("Age Histogram")
plt.legend()
# plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()
