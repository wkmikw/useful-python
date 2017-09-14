#coding=utf-8
from random import choice
#python random_walk.py

class RandomWalk(object):
	"""random walk"""
	def __init__(self, num_points=5000):
		self.num_points = num_points
		
		#begin on (0,0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""calculate all points"""

		#add points
		while len(self.x_values) < self.num_points:
			# dicide direction and distance
			x_direction = choice([-1,1])
			x_distance =choice([0,1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([-1,1])
			y_distance =choice([0,1,2,3,4])
			y_step = y_direction * y_distance

			#refuse to stand still
			if x_step == 0 and y_step == 0:
				continue

			#calculate next point's place
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)
