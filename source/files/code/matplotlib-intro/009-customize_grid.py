import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.colors import colorConverter


data = [10, 20, 15, 30, 25]

# set up the xaxis
xaxis = plt.axes().xaxis
xaxis.set_major_locator(MultipleLocator(2))
xaxis.set_minor_locator(MultipleLocator(1))
xaxis.set_major_formatter(FormatStrFormatter('%dQ'))

xaxis.grid(True, which = 'major', linewidth = 2, color = colorConverter.to_rgb('#662020'))
xaxis.grid(True, which = 'minor', linewidth = 1, color = colorConverter.to_rgb('#202020'))

# set up the yaxis
yaxis = plt.axes().yaxis
yaxis.set_major_locator(MultipleLocator(10))
yaxis.set_minor_locator(MultipleLocator(5))
yaxis.grid(True, which = 'major', linewidth = 2, color='r')
yaxis.grid(True, which = 'minor', linewidth = 1, color='g')


plt.plot(data)
plt.savefig('pngs/009-customize_grid.png')
