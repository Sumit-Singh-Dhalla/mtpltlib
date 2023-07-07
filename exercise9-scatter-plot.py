from matplotlib import pyplot as plt
import pandas as pd


plt.style.use("seaborn")

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
