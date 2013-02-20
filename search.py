from board import board
from collections import defaultdict
import sys

class a_star_search(object):

	board = 0
	open_list = []
	closed_list = []
	solution_path = []

	def __init__(self):
		self.board = board()
		self.board.start.set_state('S')
		self.board.goal.set_state('G')

		# initial start node
		self.open_list.append(self.board.start)
		self.expand_node(self.board.start)
		self.closed_list.append(self.board.start)
		

		# expansion loop for normal nodes
		while 1:
			leaf_node = self.choose_node_for_expansion()
			print "len after expand ",len(self.open_list)
			leaf_node.set_state('.')
			
			if leaf_node.x == self.board.goal.x and leaf_node.y == self.board.goal.y:
				self.open_list.append(leaf_node)
				self.closed_list.append(leaf_node)
				self.solution_append(leaf_node)
				print "Finished!"
				print "Took ",len(self.solution_path), "steps"
				#for n in self.solution_path:
				#	print n.x,n.y,n.path_cost
				break

			else:
				self.close_all_other_open_nodes()
				self.open_list.append(leaf_node)
				self.expand_node(leaf_node)
				self.solution_append(leaf_node)
				self.open_list.remove(leaf_node)
				self.closed_list.append(leaf_node)
		
			print(self.board)

	def solution_append(self,node):
		for dupe_node in self.solution_path: 
			if dupe_node.x == node.x and dupe_node.y == node.y:
				if node.evaluation_function(self.board.goal) < dupe_node.evaluation_function(self.board.goal):
					print "updating solution"
					self.solution_path.remove(dupe_node)
					self.solution_path.add(node)
					return
		self.solution_path.append(node)
			

	def choose_node_for_expansion(self):

		self.open_list = sorted(self.open_list, key=lambda node: node.evaluation_function(self.board.goal))
		print "len before pop ",len(self.open_list)
		node_to_expand = self.open_list.pop(0)	
		print "len after pop ",len(self.open_list)
		#print "open list - "
		#for i in self.open_list:
		#	print i.x,i.y,i.path_cost
		print node_to_expand
		print("We are choosing node ",node_to_expand.x,node_to_expand.y, " with a pathcost of ",node_to_expand.path_cost)
		self.print_num_equals_open()
		print "Length of open list = " , len(self.open_list)
		return node_to_expand

	def close_all_other_open_nodes(self):
		pass

	def expand_node(self,node):
		print("Expanding node ", node.x,node.y)

		if len([closed_node for closed_node in self.closed_list if closed_node == node]) != 0:
			print "Item is already in closed list!"
			return

		if node.x < board.length-1: # expand right
			new_node = self.board.nodes[node.x+1][node.y]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"
	
		if node.x > 0: # expand left
			new_node = self.board.nodes[node.x-1][node.y]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"
		
		if node.y < board.height-1: # expand down
			new_node = self.board.nodes[node.x][node.y+1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"
	
		if node.y > 0: # expand up
			new_node = self.board.nodes[node.x][node.y-1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"

		if node.y > 0 and node.x > 0: # expand diagonal up left
			new_node = self.board.nodes[node.x-1][node.y-1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"

		if node.y > 0 and node.x < board.length-1: # expand diagonal up right
			new_node = self.board.nodes[node.x+1][node.y-1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					print "appending node up right ",new_node.x,new_node.y
					self.open_list.append(new_node)
				else:
					print "Ran into obstacle on diagonal up right"

		if node.y < board.height-1 and node.x > 0: # expand diagonal down left
			new_node = self.board.nodes[node.x-1][node.y+1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"


		if node.y < board.height-1 and node.x < board.length-1: # expand diagonal down right
			new_node = self.board.nodes[node.x+1][node.y+1]
			if len([open_node for open_node in self.open_list if open_node == new_node]) == 0:
				if(str(new_node) != '7'): # isn't an obstacle
					new_node.path_cost = new_node.path_cost + node.path_cost
					self.open_list.append(new_node)
					print "appending node ",new_node.x,new_node.y
				else:
					print "Ran into obstacle"


	def print_num_equals_open(self):

		appearances = defaultdict(int)
		for curr in self.open_list:
			appearances[curr] += 1
		print("Number of dupes = ",len(self.open_list) - len(appearances))

a = a_star_search()



				
					
