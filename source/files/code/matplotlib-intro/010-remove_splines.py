import matplotlib.pyplot as plt
data = [10, 20, 15, 30, 25]
plt.axes().spines['right'].set_visible(False)
plt.axes().spines['top'].set_visible(False)
plt.axes().xaxis.set_ticks_position('bottom')
plt.axes().yaxis.set_ticks_position('left')
plt.plot(data)
plt.savefig('pngs/010-remove_splies.png')
#http://stackoverflow.com/questions/9750699/how-to-display-only-a-left-and-bottom-box-border-in-matplotlib
