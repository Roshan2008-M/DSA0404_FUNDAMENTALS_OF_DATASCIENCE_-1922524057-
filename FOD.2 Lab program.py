import numpy as np

sales = np.array([
    [100, 150, 200],
    [120, 180, 160],
    [90,  140, 190]
])


average_price = np.mean(sales)

print("Average price of all products:", average_price)
