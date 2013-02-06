import math

class node(object):

	path_cost = 0
	x = 0
	y = 0		
	state = '?'

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.state)

	def __eq__(self,other):
		if other.x == self.x and other.y == self.y:
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

		return math.ceil(math.sqrt((x**2) + (y**2)))

	def evaluation_function(node,goal):
		print("Evaluating ",node.x,node.y,node.path_cost,goal.x,goal.y)
		return node.path_cost + node.distance_to(goal)

	def info(self):
		return str(self.x+self.y)

