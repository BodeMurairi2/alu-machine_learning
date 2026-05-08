#!/usr/bin/env python3

"""
This module computes an histogram
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
# your code here
plt.hist(student_grades, bins=10, edgecolor="black", linewidth=2.0)
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.show()
