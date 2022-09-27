import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt 
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")

data=pd.read_csv("data.csv")

# when date not sorted
# data["Date"]=pd.to_datetime(data["Date"])
# data.sort_values("Date",inplace=True)

price_date=data["Date"]
price_close=data["Low_Close"]

plt.plot_date(price_date,price_close,linestyle="solid")

date_format=mpl_dates.DateFormatter( "%b,%d %y ")
plt.gca().xaxis.set_major_formatter(date_format)

plt.gcf().autofmt_xdate()


plt.title("Bitcoin Prices")
plt.xlabel("Dates")
plt.ylabel("Closing Price")
plt.tight_layout()
plt.show()