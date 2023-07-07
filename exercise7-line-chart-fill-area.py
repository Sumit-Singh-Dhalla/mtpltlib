import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)

# plotting the lines
a1 = 4 - 2*x
a2 = 3 - 0.5*x
a3 = 1 -x

# The upper edge of
# polygon
a4 = np.minimum(a1, a2)

# Setting the y-limit
plt.ylim(0, 5)

# Plot the lines
plt.plot(x, a1,
		x, a2,
		x, a3)
print(a4)
# Filling between line a3
# and line a4
plt.fill_between(x, a3, a4, color='green',
				alpha=0.5)
plt.show()
