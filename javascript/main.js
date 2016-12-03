
/* Generates a grid with given rows and columns */
function grid(rows, columns){
  var grid = [];
  var row;
  for (var i = 0; i < rows; i++){
    row = [];
    for (var k = 0; k < columns; k++){
      row.push(0);
    }
    grid.push(row);
  }
  return grid;
}

/* Plants an array of initial seeds in the grid */
function plant_seeds(seeds, grid){
  for (var i = 0; i < seeds.length; i++){
    if (grid.length >= seeds[i].x){
      if (grid[seeds[i].x].length >= seeds[i].y){
        grid[seeds[i].x][seeds[i].y] = 1;
      }
    }
  }
  return grid;
}

/* Runs the game! */
function run(){
  initial_grid = grid(3,3);
  intial_seed = [{x: 0, y: 0}, {x: 0, y: 1}];
}
exports.grid = grid;
exports.plant_seeds = plant_seeds;
