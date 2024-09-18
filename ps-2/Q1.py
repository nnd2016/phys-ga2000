# -*- coding: utf-8 -*-


#Question 1

import numpy as np

# Step 1: Original number
original_number = 100.98763
print(f"Step 1: Original Nummber = {original_number}")

# Step 2: Convert the original number to 32-bit floating-point format
float32_representation = np.float32(original_number)
print(f"Step 2: 32-bit floating-point representation = {float32_representation}")

# Step 3: Extract the binary representation of the 32-bit floating-point number
binary_rep = ''.join(f'{c:08b}' for c in np.float32(float32_representation).tobytes()[::-1])
print(f"Step 3: Binary representation of the 32-bit float = {binary_rep}")

# Step 4: Reconstruct the number from the 32-bit floating-point representation
#         Convert back from the 32-bit binary float to a number
reconstructed_number = np.float32(float32_representation)
print(f"Step 4: Reconstructed number from 32-bit float = {reconstructed_number}")

# Step 5: Compute the difference between the original number and its 32-bit float representation
difference = np.abs(original_number - float32_representation)

print(f"Step 5: Difference between original and 32-bit float = {difference:.12f}")
