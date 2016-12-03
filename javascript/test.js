var assert = require('assert');
var gol = require('./main.js');

describe('the functions', function() {

  describe('the grid function', function(){
    it('should be able return a small grid of the requested size', function() {
      assert.deepEqual([[0, 0], [0, 0]], gol.grid(2, 2));
    });

    it('should be able return a larger grid', function() {
      assert.deepEqual([[0, 0], [0, 0], [0, 0], [0, 0]], gol.grid(4, 2));
    });
  });

  describe('the plant_seeds fuction', function() {
    beforeEach(function(){
      this.grid = [[0, 0], [0, 0]];
    });

    it('should be able to update the grid points specified', function() {
      var updatedGrid = [[0, 1], [1, 0]];
      var seeds = [{x:0, y: 1}, {x: 1, y: 0}];
      assert.deepEqual(updatedGrid, gol.plant_seeds(seeds, this.grid));
    });

    it('should ignore seeds outside of the grid rows', function(){
      var seeds = [{x: 5, y: 0}];
      assert.deepEqual(this.grid, gol.plant_seeds(seeds, this.grid));
    });

    it('should ignore seeds outside of the grid columns', function(){
      var seeds = [{x: 0, y: 5}];
      assert.deepEqual([[0, 0], [0, 0]], gol.plant_seeds(seeds, this.grid));
    });
  });

});
