import matplotlib.pyplot as plt
#python scatter_squares.py

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
#
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
#
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0,5100,0,1e11])

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')