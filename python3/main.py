#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy


def make_map(x,y):
	plane = []
	for i in range(0, x):
		shard = [0 for k in range(0,y)]
		plane.append(shard)
	return plane
	

def plant_seeds(plane, seeds):
	for i in seeds:
		plane[ i[0] ][ i[1] ] = 1
	return plane
	
	
def parse_row(plane, row, x, y):
	score = 0
	if row != x and plane[row][y] != 0:
		score += 1
		
	if y > 0:
		if plane[row][y-1] != 0:
				score += 1
		
	if y < len(plane[row])-1:
		if plane[row][y+1] != 0:
			score += 1
	return score
	
	
def neighbours(plane, x, y):
	score = 0
	
	if x > 0:
		row = x - 1
		score += parse_row(plane, row, x, y)
			
	if x < len(plane[x])-1:
		row = x + 1
		score += parse_row(plane, row, x, y)
	
	score += parse_row(plane, x, x, y)
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
	r = make_map(3,3)
	s = [ [1,0], [1,1], [1,2]]
	plant_seeds(r, s)
	walk(r, 3)
