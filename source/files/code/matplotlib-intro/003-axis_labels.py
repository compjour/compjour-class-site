import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
plt.xlabel('X Factor', fontsize = 20)
plt.ylabel('Y Combos', fontsize = 16)
plt.plot(data)
plt.savefig('pngs/003-axis_labels.png')
