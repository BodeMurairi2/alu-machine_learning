#!/usr/bin/env python3

"""
This module computes a stacking bar
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
labels = ['apples', 'bananas', 'oranges', 'peaches']
x = np.arange(len(people))

bottoms = np.zeros(len(people))
for i, (color, label) in enumerate(zip(colors, labels)):
    plt.bar(x, fruit[i], width=0.5, bottom=bottoms, color=color, label=label)
    bottoms += fruit[i]

plt.xticks(x, people)
plt.yticks(np.arange(0, 81, 10))
plt.ylim(0, 80)
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
