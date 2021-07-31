import pandas as pd
import matplotlib.pyplot as plt


houses = pd.read_csv("AmesHousing.txt", sep="\t")
print(houses.columns)

fig = plt.figure(figsize=(15, 7))
subplot1 = fig.add_subplot(1, 3, 1)
subplot2 = fig.add_subplot(1, 3, 2)
subplot3 = fig.add_subplot(1, 3, 3)

houses.plot(x="Garage Area", y="SalePrice", ax=subplot1, kind="scatter")
houses.plot(x="Gr Liv Area", y="SalePrice", ax=subplot2, kind="scatter")
houses.plot(x="Overall Qual", y="SalePrice", ax=subplot3, kind="scatter")

plt.show()

