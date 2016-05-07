package main

import "fmt"

func print(a ...interface{}) {
	fmt.Println(a)
}

func make_map(x, y int) [][]int {
	/* Generates a cartesian plane of size x*y */
	plane := [][]int{}
	for i := 0; i < x; i++ {
		row := make([]int, y)
		plane = append(plane, row)
	}
	return plane
}

func plant_seed(plane [][]int, seeds [][2]int) {
	/* Plants an initial seed */
	for i := 0; i < len(seeds); i++ {
		plane[seeds[i][0]][seeds[i][1]] = 1
	}
}

func neighbours(plane [][]int, x, y int) int {
	neighbours := 0
	
	if x > 0 {
		if plane[x-1][y] != 0 {neighbours++}
		if y > 0 {
			if plane[x-1][y-1] != 0 {neighbours++}
		}
		
		if y < len( plane[x] ) -1 {
			if plane[x-1][y+1] != 0 {neighbours++}
		}
	}
	
	if x < len( plane ) - 1 {
		if plane[x+1][y] != 0 {neighbours++}
		if y > 0 {
			if plane[x+1][y-1] != 0 {neighbours++}
		}
		
		if y < len( plane[x] ) -1 {
			if plane[x+1][y+1] != 0 {neighbours++}
		}
	}
	
	if y < len( plane[x] ) - 1 {
		if plane[x][y+1] != 0 {neighbours++}
	}
	
	if y > 0 {
		if plane[x][y-1] != 0 {neighbours++}
	}
	
	return neighbours
}

func copy_plane (plane [][]int) [][]int {
	/* Deep copies a cartesian plane */
	original := [][]int{}
	for i := 0; i < len(plane); i++ {
		row := make([]int, len(plane[i]))
		original = append(original, row)
		for k := 0; k < len(plane[i]); k++ {
			original[i][k] = plane[i][k]
		}
	}
	return original
}

func walk(plane [][]int, turns int) {
	/* Walks! */
	original_plane := copy_plane(plane)
	print(original_plane)
	for t := 0; t < turns; t++ {
		for i := 0; i < len(plane); i++ {
			for j := 0; j < len(plane[i]); j++ {
				score := neighbours(original_plane, i, j)
				if score <= 1 || score >= 4 {
					plane[i][j] = 0
				}
				if score == 3 {
					plane[i][j] = 1
				}
			}
		}
		original_plane = copy_plane(plane)
		print(original_plane)
	}
}

func main() {
	r := make_map(3, 3)
	s := [][2]int{[2]int{1,0}, [2]int{1, 1}, [2]int{1, 2}}
	plant_seed(r, s)
	walk(r, 3)
}
