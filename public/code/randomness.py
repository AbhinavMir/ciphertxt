import numpy as np
import matplotlib.pyplot as plt

# Parameters for the two distributions
mean1, std_dev1 = 0, 1
mean2, std_dev2 = 3, 2

# Generate random data
data1 = np.random.normal(mean1, std_dev1, 10000) # I would normally use quantumrandom here 
# but it's not available right now!
data2 = np.random.normal(mean2, std_dev2, 10000)

# Plot the two distributions
plt.figure(figsize=(10,6))
plt.hist(data1, bins=100, alpha=0.5, color='red', label='Output of PRG')
plt.hist(data2, bins=100, alpha=0.5, color='blue', label='True Randomness')
plt.title('From PRG Output to True Randomness: A Hybrid Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('public/images/hybrid-distribution.png', dpi=100)
