import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
plt.yticks([15, 30])
plt.xticks([0, 1, 2, 3, 4])
plt.plot(data)
plt.savefig('pngs/005-set_ticks.png')
