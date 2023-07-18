from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("seaborn")

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

x1 = np.array([6, 7, 3, 5, 3, 18, 3, 10, 3, 10, 11, 10, 5])
y1 = np.array([99, 86, 89, 84, 101, 82, 101, 89, 91, 74, 76, 83, 85])

plt.scatter(x, y, c=np.divide(y, x), edgecolors="black", cmap="Blues")
plt.scatter(x1, y1, c=np.divide(y1, x1), edgecolors="black", cmap="Accent")

bar = plt.colorbar()
bar.set_label("Top Speed/Age ratio")

plt.xlabel("Age")
plt.ylabel("Top Speed")
plt.title("Cars Top Speed with Age")
plt.show()














"""
csv_input = pd.read_csv("2019-05-31-data.csv")

views = csv_input["view_count"]
likes = csv_input['likes']
ratio = csv_input['ratio']


plt.scatter(views, likes, c=ratio, edgecolors="black",
            cmap="summer")
bar = plt.colorbar()
bar.set_label("like/dislike Ratio")

plt.title("Video Likes Scatter Plot")
plt.xscale("log")
plt.yscale("log")
plt.legend()
# plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()
"""