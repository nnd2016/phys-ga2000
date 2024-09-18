# -*- coding: utf-8 -*-

# Question 2

import numpy as np

# Using 32-bit floating point
epsilon_32 = np.float32(1.0)
increment_32 = np.float32(1.0)

while np.float32(1.0) + increment_32 == np.float32(1.0):
    increment_32 /= np.float32(2.0)

print(f"Minimum value for 32-bit float that when added to 1 changes the result: {increment_32}")

# Using 64-bit floating point
epsilon_64 = np.float64(1.0)
increment_64 = np.float64(1.0)
while np.float64(1.0) + increment_64 == np.float64(1.0):
    increment_64 /= np.float64(2.0)

print(f"Minimum value for 64-bit float that when added to 1 changes the result: {increment_64}")


# Step 2: Find the minimum and maximum representable values (dynamic range)

# Minimum positive number for 32-bit
min_pos_32 = np.float32(np.finfo(np.float32).tiny)
print(f"Minimum positive number for 32-bit float: {min_pos_32}")

# Minimum positive number for 64-bit
min_pos_64 = np.float64(np.finfo(np.float64).tiny)
print(f"Minimum positive number for 64-bit float: {min_pos_64}")

# Maximum positive number for 32-bit
max_pos_32 = np.float32(np.finfo(np.float32).max)
print(f"Maximum positive number for 32-bit float: {max_pos_32}")

# Maximum positive number for 64-bit
max_pos_64 = np.float64(np.finfo(np.float64).max)
print(f"Maximum positive number for 64-bit float: {max_pos_64}")

