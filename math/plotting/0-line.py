#!/usr/bin/env python3

"""
This is a simple example of plotting a line graph using matplotlib.
It uses numpy to create an array of y values that are the cubes of
the x values.The x values are generated using the arange function from numpy,
which creates an array of values from 0 to 10 (inclusive) with a step of 1.
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here
plt.plot(y, color="red")
plt.show()
