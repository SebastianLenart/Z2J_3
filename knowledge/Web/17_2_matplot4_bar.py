from matplotlib import pyplot as plt
import numpy as np
from numpy import random


xs = np.arange(1, 6)
tops = np.arange(2, 12, 2)
plt.bar(xs, tops)
plt.show()

fruits = {
"apples": 10,
"oranges": 16,
"bananas": 9,
"pears": 4,
}
plt.bar(fruits.keys(), fruits.values())
plt.show()


plt.hist(random.randn(10000), 20)
plt.show()

xs = np.arange(1, 6)
tops = np.arange(2, 12, 2)
plt.bar(xs, tops)
plt.savefig("bar.png")
"""
If you want to both save a figure and display it on the screen,
make sure that you save it first before displaying it!
The show() function pauses execution of your code and closing
the display window destroys the graph, so trying to save the figure
after calling show() results in an empty file.
"""























