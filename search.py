from square import square
from board import board
import math
import sys

class search(object):

	closedset = set()
	openset = set()
	came_from = {}
	g_score = {}
	f_score = {}
	theboard = ""

	def __init__(self):

		i = 0
		for sq in self.run():
			print "i = " + str(i)
			print str(sq)
			self.theboard.squares[sq.x][sq.y].state = '*'
			i = i + 1
		print self.theboard
	

	def run(self):
		""" See /docs/pseudocode.txt for full algorithm pseudocode """
	
		self.theboard = board(sys.argv[1],sys.argv[2],sys.argv[3])
		print self.theboard
		start = self.theboard.start
		goal = self.theboard.goal

		self.g_score[start] = 0
		self.f_score[start] = self.g_score[start]+ self.heuristic_cost_estimate(start,goal)
		self.openset.add(start)

		while self.count(self.openset) > 0:
			f_score_sorted = sorted(self.f_score, key=lambda square: self.g_score[square] + self.heuristic_cost_estimate(square,goal))
			i = 0
			for f_score_sq in f_score_sorted:
				i = i + 1


			i = 0
			# pick the best square that hasn't already been evaluated
			for i in range(len(f_score_sorted)-1):
				if(f_score_sorted[i] not in self.closedset):
					break

			current = f_score_sorted[i]
			if current == goal:
				return self.reconstruct_path(goal)

			self.openset.remove(current)
			self.closedset.add(current)
			for neighbour in self.neighbour_nodes(current):
				if neighbour not in self.closedset:
					
					temp_g_score = self.g_score[current] + 1 #self.distance_to(current,neighbour)
					if (neighbour not in self.openset) or (temp_g_score < self.g_score[neighbour]):
						# pick this path..
						self.came_from[neighbour] = current
						self.g_score[neighbour] = temp_g_score
						self.f_score[neighbour] = self.g_score[neighbour] + self.heuristic_cost_estimate(neighbour,goal)
						
						if neighbour not in self.openset:
							self.openset.add(neighbour)
				
			
		print "Reached the end of nodes to expand, failure"				


	def neighbour_nodes(self,node):
		neighbours = set()

		if node.north != 0:
			neighbours.add(node.north)
		if node.east != 0:
			neighbours.add(node.east)
		if node.west != 0:
			neighbours.add(node.west)
		if node.south != 0:
			neighbours.add(node.south)

		return neighbours


	def distance_to(self,start_node,end_node):
		x = start_node.x - end_node.x
		y = start_node.y - end_node.y

		return 1 * max(abs(x),abs(y))

	def evaluation_function(self,node,goal):
		return (node.self.distance_to(goal) + node.path_cost)

	def heuristic_cost_estimate(self,start_node,end_node):
		heuristic = self.distance_to(start_node,end_node)
		return heuristic 

	def reconstruct_path(self, current_node):

		try: 
			self.came_from[current_node]
			p = self.reconstruct_path(self.came_from[current_node])
			return_path = []
			return_path.extend(p)
			return_path.append(current_node)
			return return_path
		except KeyError,e:
			return [current_node]

	def count(self,set_to_count):
		total_count = 0
		for i in set_to_count:
			total_count = total_count + 1
		return total_count
		

search()
