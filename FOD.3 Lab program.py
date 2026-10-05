import numpy as np

house_data = np.array([
    [3, 1500, 250000],
    [5, 2000, 350000],
    [4, 1800, 300000],
    [6, 2500, 450000]
])

# Select houses with more than 4 bedrooms
houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(houses[:, 2])

print("Average sale price of houses with more than 4 bedrooms:", average_price)
