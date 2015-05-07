import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
# plot() the data first, so
#  that xlim, ylim are autoscaled
plt.plot(data)
# then adjust xlim, ylim
plt.xlim([0, 10])
plt.ylim(ymin = 0) #leave ymax unchanged
plt.savefig('pngs/007-limit_axis.png')
