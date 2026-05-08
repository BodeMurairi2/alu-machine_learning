#!/usr/bin/env python3

"""
plot all 5 previous examples in one graph
"""

import numpy as np
import matplotlib.pyplot as plt
from helpers import (
    simple_plot,
    scatter_plot,
    change_scale,
    plot_2_lines,
    plot_frequency
    )


y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
plt.figure(figsize=(10, 14))
# suptitle sets a title for the whole figure, not a single subplot
plt.suptitle("All in One")

# 3-row, 2-col grid; each call sets the active subplot by (row, col)
plt.subplot2grid((3, 2), (0, 0))
simple_plot(y=y0)

plt.subplot2grid((3, 2), (0, 1))
scatter_plot(x=x1, y=y1)

plt.subplot2grid((3, 2), (1, 0))
change_scale(x=x2, y=y2)

plt.subplot2grid((3, 2), (1, 1))
plot_2_lines(x=x3, y1=y31, y2=y32)

# colspan=2 makes the histogram span both columns in the last row
plt.subplot2grid((3, 2), (2, 0), colspan=2)
plot_frequency(x=student_grades)

# rect top=0.96 reserves space for suptitle; h_pad adds vertical spacing between rows
plt.tight_layout(rect=[0, 0, 1, 0.96], h_pad=4)
plt.show()
