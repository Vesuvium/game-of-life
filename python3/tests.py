# -*- coding: utf-8 -*-
import random


import pytest


from main import generate_grid


@pytest.fixture
def rows():
  return random.randint(1,10)


@pytest.fixture
def columns():
  return random.randint(1,10)


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