from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

labels = ["JS", "HTML/CSS", "SQL", "Python", "Java"]
slices = [35000, 37456, 36785, 37890, 40455]
explode = [0, 0, 0, 0.1, 0]
plt.pie(slices, labels=labels, explode=explode,
        shadow=True, startangle=0, autopct="%1.1f%%",
        wedgeprops={'edgecolor': 'black'})

plt.title("My Pie Chart")
plt.legend()
plt.tight_layout()
plt.show()
