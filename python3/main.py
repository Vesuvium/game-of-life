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
	the number of neighbouring cells with a value of 1.
	"""
	score = 0
	score += parse_row(grid, x, x, y)
	if x > 0:
		score += parse_row(grid, x-1, x, y)
	if x < len(grid[x]) - 1:
		score += parse_row(grid, x+1, x, y)
	return score


def next_generation(grid):
	"""
	Calculates the next generation of a given grid.
	"""
	x = 0
	while x < len(grid):
		y = 0
		while y < len(grid[x]):
			score = cell_score(grid, x, y)
			if score <= 1 or score >= 4:
				grid[x][y] = 0
			elif score == 3:
				grid[x][y] = 1
			y += 1
		x += 1
	return grid


def next_generations(grid, generations):
	for i in range(0, generations):
		grid = next_generation(grid)
	return grid


def run():
	grid = generate_grid(3, 3)
	seed = [[1, 0], [1, 1], [1, 2]]
	prepare_grid(grid, seed)
	next_generations(grid, 3)


if __name__ == '__main__':
	run()
