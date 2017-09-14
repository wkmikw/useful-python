#coding=utf-8
import matplotlib.pyplot as plt
from random_walk import RandomWalk
#python t.py

rw = RandomWalk(1000)
rw.fill_walk()
plt.figure(dpi=141, figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1)
#plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
#highligt the start and end
plt.scatter(0,0,c='green',edgecolor='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

plt.show()

'''
keep_running = input("Make another walk?(y/n):")
if keep_running == 'n':
	break
'''



