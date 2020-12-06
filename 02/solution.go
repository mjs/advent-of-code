package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type parsed struct {
	i, j     int
	ch       string
	password string
}

func parseLine(line string) (parsed, error) {
	var p parsed
	_, err := fmt.Sscanf(line, "%d-%d %1s: %s", &p.i, &p.j, &p.ch, &p.password)
	return p, err
}
func isValidPart1(p parsed) bool {
	count := strings.Count(p.password, p.ch)
	return p.i <= count && count <= p.j
}

func isValidPart2(p parsed) bool {
	if p.j > len(p.password) {
		return false
	}
	ch := p.ch[0]
	return (p.password[p.i-1] == ch) != (p.password[p.j-1] == ch)
}

func main() {
	part1Count := 0
	part2Count := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line, err := parseLine(scanner.Text())
		if err != nil {
			fmt.Printf("failed to parse %q: %v\n", scanner.Text(), err)
		} else {
			if isValidPart1(line) {
				part1Count++
			}
			if isValidPart2(line) {
				part2Count++
			}
		}
	}

	fmt.Println("part 1:", part1Count)
	fmt.Println("part 1:", part2Count)
}
