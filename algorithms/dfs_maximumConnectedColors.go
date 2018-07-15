package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

var already_seen [][]bool

type stack []Pair

func (s stack) Empty() bool { return len(s) == 0 }
func (s stack) Peek() Pair  { return s[len(s)-1] }
func (s *stack) Put(i Pair) { (*s) = append((*s), i) }
func (s *stack) Pop() Pair {
	d := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return d
}

type Pair struct {
	i, j int
}

func isValid(board [][]string, i, j int) bool {
	if (i >= 0 && i < len(board) && j >= 0 && j < len(board[0])) {
		if already_seen[i][j] == true {
			return false
		}
		return true
	}
	return false
}

func dfs(board [][]string, i, j int, val string) int {
	area := 0
	var stack stack
	stack.Put(Pair{i, j})

	for !stack.Empty() {
		v := stack.Pop()
		if isValid(board, v.i, v.j) {
			if board[v.i][v.j] == val {
				area++
				already_seen[v.i][v.j] = true
				stack.Put(Pair{v.i + 1, v.j})
				stack.Put(Pair{v.i - 1, v.j})
				stack.Put(Pair{v.i, v.j - 1})
				stack.Put(Pair{v.i, v.j + 1})
			}

		}
	}
	return area;
}

func maximumConnectedColors(board [][]string) int {
	m := 0
	already_seen = make([][]bool, len(board))
	for i := range board {
		already_seen[i] = make([]bool, len(board[i]))
	}

	for i := range board {
		for j := range board[i] {
			r := dfs(board, i, j, board[i][j])
			m = max(m, r)
		}
	}

	return m
}

func main() {

	board := [][]string{
		[]string{"LBLUE", "RED", "LBLUE", "RED"},
		[]string{"LBLUE", "LBLUE", "LBLUE", "BLUE"},
		[]string{"RED", "BLUE", "BLUE", "RED"},
	}

	res := maximumConnectedColors(board)

	fmt.Println(res)
	if res != 5 {
		fmt.Println("Wrong")
	}
}
