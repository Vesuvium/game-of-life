# -*- coding: utf-8 -*-
import random


import pytest


from main import generate_grid, prepare_grid, parse_row


@pytest.fixture(scope='function')
def rows():
  return random.randint(1,10)


@pytest.fixture(scope='function')
def columns():
  return random.randint(1,10)


@pytest.fixture(scope='function')
def grid(rows, columns):
  grid = []
  for i in range(0, rows):
    grid.append( [0 for k in range(0,columns)] )
  return grid


def test_generate_grid(rows, columns):
  """
  Tests the size of a generated grid.
  """
  grid = generate_grid(rows, columns)
  for row in grid:
    assert len(row) == columns
    

def test_generate_grid_values(rows, columns):
  """
  Tests the values of a generated grid.
  """
  grid = generate_grid(rows, columns)
  for row in grid:
    for cell in row:
      assert cell == 0
      
      
def test_prepare_grid(grid, rows, columns):
  """
  Tests whether prepare_grid can correctly use a config matrix to setup values.
  """
  config_matrix = []
  # generates a random config matrix
  for i in range(0, random.randint(1, rows*columns)):
    random_cell = [random.randint(0, rows-1), random.randint(0, columns-1)]
    config_matrix.append(random_cell)
  new_grid = prepare_grid(grid, config_matrix)
  for row in config_matrix:
    assert new_grid[ row[0] ][row[1]] == 1
    
    
def test_parse_row(grid):
	"""
	Tests whether parse_row can correctly parse a grid's row
	"""
	x = random.randint(0, len(grid)-1)
	y = random.randint(0, len(grid[x])-1)
	counter = 0
	while counter < len(grid):
		score = parse_row(grid, counter, x, y)
		assert score == grid[counter].count(1)
		counter += 1
    