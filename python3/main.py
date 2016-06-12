#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy


def generate_grid(rows, columns):
	"""
	Generates a grid of nested lists of size x*y
	"""
	grid = []
	for row in range(0, rows):
		column = [0 for k in range(0, columns)]
		grid.append(column)
	return grid
	
	
def prepare_grid(grid, config_matrix):
	"""
	Prepares a grid using a config matrix, setting up alive cells.
	"""
	for i in config_matrix:
		grid[ i[0] ][ i[1] ] = 1
	return grid
	
	
def parse_row(grid, row, x, y):
	"""
	Parses a grid's row, counting live cells.
	"""
	score = grid[row].count(1)
	if row == x and grid[x][y] == 1:
		return score - 1
	return score
	
	
def cell_score(grid, x, y):
	"""
	Calculates the score of a cell. A cell's score is 
	the number of neighbouring cell with a value of 1.
	"""
	score = 0
	score += parse_row(grid, x, x, y)
	if x > 0:
		score += parse_row(grid, x-1, x, y)
	if x < len(grid[x]) - 1:
		score += parse_row(grid, x+1, x, y)
	return score


def walk(plane, turns):
	original_plane = copy.deepcopy(plane)
	x = 0
	y = 0
	for t in range(0, turns):
		for i in plane:
			for k in i:
				score = neighbours(original_plane, x, y)
				if score <= 1 or score >= 4:
					plane[x][y] = 0
				elif score == 3:
					plane[x][y] = 1
				y += 1
			x += 1
			y = 0
		x = 0
		original_plane = copy.deepcopy(plane)
		print(original_plane)


if __name__ == '__main__':
	r = generate_grid(3,3)
	s = [ [1,0], [1,1], [1,2]]
	prepare_grid(r, s)
	walk(r, 3)