import numpy as np
import matplotlib.pyplot as plt

# Data from the table
trial = np.array([1, 2, 3, 4, 5])
m = np.array([25000, 50000, 100000, 200000, 400000])
k = np.array([64, 32, 16, 8, 4])
p = np.array([0.54, 0.53, 0.53, 0.57, 0.58])
t_lookup = np.array([0.11972, 0.03027, 0.00837, 0.00207, 0.00059])

# Plotting the data
plt.plot(trial, t_lookup)
plt.xscale('log')
plt.xlabel('Number of Chains (m)')
plt.ylabel('Time per Lookup (t/lookup)')
plt.title('Rainbow Table Lookup Attack Experiment')
plt.show()
