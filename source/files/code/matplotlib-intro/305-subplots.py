import matplotlib.pyplot as plt
plt.style.use('ggplot')





# fig, ax = plt.subplots()
# xdata = range(100)
# ydata = [i ** 1.5 for i in range(100)]
# ax.plot([1,2], [10,20])



fig, axarr = plt.subplots(2, sharex = False)
axarr[0].bar([0,1,2,3,4], [2,4,6,3,8])
axarr[1].bar([0,1,2,3,4], [5,3,9,2,7])
plt.savefig('subplots-bar-2-no-sharex.png')

fig, axarr = plt.subplots(2, sharex = True)
axarr[0].bar([0,1,2,3,4], [2,4,6,3,8])
axarr[1].bar([0,1,2,3,4], [5,3,9,2,7])
plt.savefig('subplots-bar-2-sharex.png')

fig, axarr = plt.subplots(2, sharex = True)
axarr[0].bar([0,1,2,3,4], [2,4,6,3,8])
axarr[1].bar([5,6,7,8,9], [5,3,9,2,7])
plt.savefig('subplots-bar-2-sharex-oops.png')
