import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
plt.yticks([15, 30], ['Meh', 'Whoa!'])
plt.xticks([0, 1, 2, 3, 4], ['Zero', 'Un', 'Deuz', 'Tres', 'Cinco'])
plt.plot(data)
plt.savefig('pngs/006-rename_ticks.png')
