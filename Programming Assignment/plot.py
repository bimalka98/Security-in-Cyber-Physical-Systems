import numpy as np
import matplotlib.pyplot as plt

# Data from the table
trial = np.array([1, 2, 3, 4, 5])
m = np.array([25000, 50000, 100000, 200000, 400000])
k = np.array([64, 32, 16, 8, 4])
p = np.array([0.54, 0.53, 0.53, 0.57, 0.58])
t_lookup = np.array([0.11972, 0.03027, 0.00837, 0.00207, 0.00059])

# Plotting the data

# make the figure size 4:3 ratio
plt.figure(figsize=(12, 9))

# Plotting the time per lookup in scatter plot, connecting the points using a dashed line
plt.plot(trial, t_lookup, 'o--', label='Time per Lookup', color='red', linewidth=2, markersize=12)

# x ticks must be integers
plt.xticks(trial)

# activate the grid
plt.grid()

plt.xlabel('Trial number')
plt.ylabel('Time per Lookup (s)')
plt.title('Rainbow Table Lookup Attack Experiment')

# Saving the plot with maximum quality
plt.savefig('plot.png', dpi=1000)

plt.show()
