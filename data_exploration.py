import matplotlib.pyplot as plt
from numpy import NaN
import pandas


datapath = "./data/BFI_raw/bfi-weekend-box-office-report-2020-07-03-05.xls"
df = pandas.read_excel(datapath, skiprows=1)

df.head(1000)

print(df.columns)
print(df.dtypes)
print(df.shape)

print(df.head(10))
print(df.tail(5))

#######  After concatenating sheets   ########
##############################################

datapath = "./data/BFI_Merged.xlsx"
df = pandas.read_excel(datapath)

# initial stats
print(df.describe(datetime_is_numeric=True))
print("Rows x Columns:  " + str(df.shape))
print(df.dtypes)

df.boxplot(column=["Weekend Gross"])
plt.yscale("log")  # very big discrepancy, thus log scale
plt.show()
df.boxplot(column=["Weeks on release"])
plt.show()
df.boxplot(column=["API Budget"])
plt.show()

# Plot premiere week revenue over time (very big discrepancy, thus log scale)
g1 = df.loc[df["Weeks on release"] == 1].plot.scatter(
    x="API Release Date", y="Weekend Gross", s=0.5
)
g1.set_yscale("log")
plt.savefig("./data/graphs/g1.png")
plt.show()

# Plot rating against revenue
df.loc[df["API Budget"] != NaN].plot.scatter(x="API Budget", y="API Rating", s=0.5)
plt.savefig(fname="./data/graphs/g2.png")
plt.show()

# Plot Budget against revenue
df.loc[df["API Budget"] != NaN].plot.scatter(x="API Budget", y="Weekend Gross", s=0.5)
plt.savefig(fname="./data/graphs/g3.png")
plt.show()
