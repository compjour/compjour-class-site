import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
plt.xticks(rotation = 'vertical')
plt.yticks(rotation = 45)
plt.plot(data)
plt.savefig('pngs/004-format_ticks.png')
