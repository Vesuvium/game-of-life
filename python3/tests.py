# -*- coding: utf-8 -*-
import random


import pytest


from main import generate_grid, prepare_grid


@pytest.fixture
def rows():
  return random.randint(1,10)


@pytest.fixture
def columns():
  return random.randint(1,10)


@pytest.fixture
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
      
      
def test_prepare_grid():
  """
  Tests whether prepare_grid can correctly use a config matrix to setup values.
  """
  grid = [ [0,0,0], [0,0,0], [0,0,0] ]
  rows = len(grid)
  columns = len(grid[0])
  config_matrix = []
  # generates a random config matrix
  for i in range(0, random.randint(1, rows*columns)):
    random_cell = [random.randint(0, rows-1), random.randint(0, columns-1)]
    config_matrix.append(random_cell)
  new_grid = prepare_grid(grid, config_matrix)
  for row in config_matrix:
    assert new_grid[ row[0] ][row[1]] == 1
    