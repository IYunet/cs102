package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
)

func readSudoku(filename string) ([][]byte, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	grid := group(filter(data), 9)
	return grid, nil
}

func filter(values []byte) []byte {
	filteredValues := make([]byte, 0)
	for _, v := range values {
		if (v >= '1' && v <= '9') || v == '.' {
			filteredValues = append(filteredValues, v)
		}
	}
	return filteredValues
}

func display(grid [][]byte) {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid); j++ {
			fmt.Print(string(grid[i][j]))
		}
		fmt.Println()
	}
}

func group(values []byte, n int) [][]byte {
	l := len(values)
	blocksCount := l / n
	if l%n != 0 {
		blocksCount += 1
	}
	result := make([][]byte, blocksCount)
	for i := 0; i < len(values); i++ {
		result[i/n] = append(result[i/n], values[i])
	}
	return result
}

func getRow(grid [][]byte, row int) []byte {
	return grid[row]
}

func getCol(grid [][]byte, col int) []byte {
	var column []byte
	for i := 0; i < len(grid); i++ {
		column = append(column, grid[i][col])
	}
	return column
}

func getBlock(grid [][]byte, row int, col int) []byte {
	var colValues2 []byte
	addPoss := (row / 3) * 3
	addPoss1 := (col / 3) * 3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			colValues2 = append(colValues2, grid[i+addPoss][j+addPoss1])
		}
	}
	return colValues2
}

func findEmptyPosition(grid [][]byte) (int, int) {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == '.' {
				return i, j
			}
		}
	}
	return -1, -1
}

func contains(values []byte, search byte) bool {
	for _, v := range values {
		if v == search {
			return true
		}
	}
	return false
}

func findPossibleValues(grid [][]byte, row int, col int) []byte {
	fRow := getRow(grid, row)
	fCol := getCol(grid, col)
	block := getBlock(grid, row, col)

	var blackList = [][]byte{fRow, fCol, block}
	var ans []byte
	for i := '1'; i <= '9'; i++ {
		flag := true
		for j := 0; j < len(blackList); j++ {
			for k := 0; k < len(blackList[j]); k++ {
				if byte(i) == blackList[j][k] {
					flag = false
				}
			}
			if !flag {
				break
			}
		}
		if flag {
			ans = append(ans, byte(i))
		}
	}
	return ans
}

func solve(grid [][]byte) ([][]byte, bool) {
	row, col := findEmptyPosition(grid)
	if row == -1 {
		return grid, true
	}
	for _, v := range findPossibleValues(grid, row, col) {
		grid[row][col] = v
		res, status := solve(grid)
		if status {
			return res, true
		}
	}

	grid[row][col] = '.'
	return nil, false
}

func checkSolution(grid [][]byte) bool {
	for i, _ := range grid {
		result := getRow(grid, i)
		if len(result) != 9 {
			return false
		}
	}

	for i, _ := range grid {
		result := getCol(grid, i)
		if len(result) != 9 {
			return false
		}
	}

	for i, _ := range grid {
		for j, _ := range grid[i] {
			result := getBlock(grid, i, j)
			if len(result) != 9 {
				return false
			}
		}
	}
	return true
}

func generateSudoku(N int) [][]byte {
	var sudoku1 [9][]byte
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			sudoku1[i] = append(sudoku1[i], '.')
		}
	}
	grid, status := solve(sudoku1[:])
	if !status {
		return [][]byte{nil}
	}
	if N > 81 {
		N = 81
	}
	N = 81 - N
	for N > 0 {
		row := rand.Intn(9)
		col := rand.Intn(9)
		if grid[row][col] != '.' {
			grid[row][col] = '.'
			N--
		}
	}
	return grid
}

func main() {
	grid, _ := readSudoku("puzzle1.txt")
	fmt.Println(solve(grid))
}
