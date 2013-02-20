import math

class node(object):

	path_cost = 1
	x = 0
	y = 0		
	state = '?'

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.state)

	def __eq__(self,other):
		if other.x == self.x and other.y == self.y and other.path_cost == self.path_cost:
			return True
		else:
			return False

	def set_state(self,state):
		self.state = state
		if(state == '7'): # obstacle
			self.path_cost = 999999999999 # or as close to inf. as we can get
	
	def distance_to(self,other_node):
		x = self.x - other_node.x
		y = self.y - other_node.y

		return math.floor(math.sqrt((x**2) + (y**2)))

	def evaluation_function(node,goal):
		return (node.distance_to(goal) + node.path_cost)

	def info(self):
		return str(self.x+self.y)

