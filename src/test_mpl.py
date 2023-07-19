import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# create the main figure and the main grid
fig = plt.figure()
grid = GridSpec(nrows=2, ncols=2, figure=fig)

# create the first sub-figure and its grid
subgrid1 = grid[0, 0].subgridspec(2, 1)
ax1_1 = fig.add_subplot(subgrid1[0])
ax1_2 = fig.add_subplot(subgrid1[1])

# create the second sub-figure and its grid
subgrid2 = grid[0, 1].subgridspec(1, 2)
ax2_1 = fig.add_subplot(subgrid2[0])
ax2_2 = fig.add_subplot(subgrid2[1])

# create the third sub-figure and its grid
subgrid3 = grid[1, :].subgridspec(1, 3)
ax3_1 = fig.add_subplot(subgrid3[0])
ax3_2 = fig.add_subplot(subgrid3[1])
ax3_3 = fig.add_subplot(subgrid3[2])

# add some content to the subfigures
ax1_1.plot([1, 2, 3], [4, 5, 6])
ax1_2.scatter([1, 2, 3], [4, 5, 6])
ax2_1.hist([1, 1, 2, 2, 2, 3])
ax2_2.bar([1, 2, 3], [4, 5, 6])
ax3_1.plot([1, 2, 3], [6, 5, 4])
ax3_2.scatter([1, 2, 3], [6, 5, 4])
ax3_3.hist([3, 3, 2, 2, 2, 1])

# add some titles to the subfigures
ax1_1.set_title("Subplot 1.1")
ax1_2.set_title("Subplot 1.2")
ax2_1.set_title("Subplot 2.1")
ax2_2.set_title("Subplot 2.2")
ax3_1.set_title("Subplot 3.1")
ax3_2.set_title("Subplot 3.2")
ax3_3.set_title("Subplot 3.3")

# add a title to the main figure
fig.suptitle("Main Figure")

# show the plot
plt.show()
