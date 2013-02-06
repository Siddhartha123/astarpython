from board import board

class a_star_search(object):

	board = 0
	open_list = []
	closed_list = []
	solution_path = []

	def __init__(self):
		self.board = board()
		self.board.start.set_state('S')
		self.board.goal.set_state('G')
		self.expand_node(self.board.start)
		self.solution_path.append(self.board.start)
		self.closed_list.append(self.board.start)
		while 1:
			leaf_node = self.choose_node_for_expansion()
			leaf_node.set_state('.')
			print "Standing at ",leaf_node.x,leaf_node.y
			self.open_list = list(set(self.open_list))
			
			if leaf_node.x == self.board.goal.x and leaf_node.y == self.board.goal.y:
				self.closed_list.append(leaf_node)
				self.solution_path.append(leaf_node)
				print "Finished!"
				break

			else:
				self.expand_node(leaf_node)
				self.closed_list.append(leaf_node)
				self.solution_path.append(leaf_node)
		
			print(self.board)

	def choose_node_for_expansion(self):
	
		self.open_list = sorted(self.open_list, key=lambda node: node.evaluation_function(self.board.goal))
		for item in self.open_list:
			print("open ",item.x,item.y)
		print("We are choosing node ",self.open_list[0].x,self.open_list[0].y, " with a pathcost of ",self.open_list[0].path_cost)
		return self.open_list.pop(0)

	def expand_node(self,node):
		print("Expanding node ", node.x,node.y)
		#print "Open list "
		#for item in self.open_list:
		#	print("open ",item.x,item.y)

		if len([closed_node for closed_node in self.closed_list if closed_node == node]) != 0:
			print "Item is already in closed list!"
			return
		#	return # item is already in list

		if node.x < board.length-1: # expand right
			new_node = self.board.nodes[node.x+1][node.y]
			new_node.path_cost = new_node.path_cost + node.path_cost
			print "Node should be x+1 y yet",new_node.x,new_node.y
			self.append_open(new_node)
	
		if node.x > 0: # expand left
			new_node = self.board.nodes[node.x-1][node.y]
			new_node.path_cost = new_node.path_cost + node.path_cost
			print "Node should be x-1 y yet",new_node.x,new_node.y
			self.append_open(new_node)
		
		if node.y < board.height-1: # expand down
			new_node = self.board.nodes[node.x][node.y+1]
			new_node.path_cost = new_node.path_cost + node.path_cost
			print "Node should be x y+1 yet",new_node.x,new_node.y
			self.append_open(new_node)
		
		if node.y > 0: # expand up
			new_node = self.board.nodes[node.x][node.y-1]
			new_node.path_cost = new_node.path_cost + node.path_cost
			print "Node should be x y-1 yet",new_node.x,new_node.y
			self.append_open(new_node)
		
		#for item in self.open_list:
		#	print("list-",item.path_cost)

	def append_open(self,node):
		# check if we already have the item in the closed list, if so, don't open again
		print "Appending ",node.x,node.y
		if len([closed_node for closed_node in self.closed_list if closed_node == node]) == 0:
			self.open_list.append(node)

	def print_num_equals_open(self):
		print("Number of dupes = ",len(self.open_list) - len(set(self.open_list)))

a = a_star_search()



				
					
