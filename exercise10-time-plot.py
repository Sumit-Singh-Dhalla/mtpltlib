from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mlt_dates


plt.style.use("seaborn")
data = pd.read_csv("date_data.csv")
# dates = data["Date"]
data["Date"] = pd.to_datetime(data["Date"])
data.sort_values("Date", inplace=True)

plt.plot_date(data['Date'], data['Close'], linestyle="solid")
plt.gcf().autofmt_xdate()
plt.xlabel("Dates")

plt.title("Datetime Plot")
plt.legend()
# plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()
