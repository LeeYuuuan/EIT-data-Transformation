import numpy as np

day = 1
count = 1
day_data = np.load(f"eit_physical_data/dday/day{day}.npy")
one_data = np.load(f"eit_physical_data/vol_day{day}_{count}.npy")

print(day_data[1] == one_data)
print(one_data)