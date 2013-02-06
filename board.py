from node import node

class board(object):

	start = 0
	goal = 0
	length = 50
	height = 50
	nodes = []

	def __init__(self):
		self.nodes = [[node(x,y) for x in range(self.length)] for y in range(self.height)] 
		for x in range(self.length):
			for y in range(self.height):
				self.nodes[x][y] = node(x,y)

		with open('board50obs.txt') as input_data:
			x = 0
			y = 0
			for y in range(self.height):
				line = input_data.readline().strip()
				for x in range(self.length):
					self.nodes[x][y].set_state(line[x])
				y = y + 1

			self.start = self.nodes[0][0]
			self.goal = self.nodes[self.length-1][self.height-1]

	def __str__(self):
		toreturn = ''
		for x in range(self.length):
			for y in range(self.height):
				 #toreturn += str(self.nodes[x][y].x)+','+str(self.nodes[x][y].y)+' '
				 toreturn += str(self.nodes[x][y])
			toreturn += "\n"
		return toreturn

#b = board()
#print(b)
#print(b.start.distance_to(b.goal))
#print(b.goal.distance_to(b.start))
#print(b.nodes[5][5].distance_to(b.start))
#print(b.start.distance_to(b.nodes[5][5]))

