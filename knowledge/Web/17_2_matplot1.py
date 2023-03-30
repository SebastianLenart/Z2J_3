from matplotlib import pyplot as plt
plt.plot([2, 4, 6, 8, 10], "g-o")
plt.show()

"""
The line plt.plot([1, 2, 3, 4, 5]) creates a plot with a line through
the points (0, 1), (1, 2), (2, 3), (3, 4), and (4, 5). The list [1, 2, 3, 4, 5]
that you passed to the plt.plot() function represents the y-values of
the points in the plot. Since you didn’t specify any x-values, matplotlib
automatically uses the indices of the list elements which, since Python
starts counting at 0, are 0, 1, 2, 3 and 4.
"""

xs = [1, 2, 3, 4, 5]
ys = [2, 4, 6, 8, 10]
plt.plot(xs, ys)
plt.show()

xs = [1, 2, 3, 4, 5]
ys = [3, -1, 4, 0, 6]
plt.plot(xs, ys)
plt.show()