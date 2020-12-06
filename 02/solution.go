package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func isValidPart1(line string) bool {
	min, max, c, password := parseLine(line)
	if min < 0 {
		return false
	}
	count := strings.Count(password, c)
	return min <= count && count <= max
}

func isValidPart2(line string) bool {
	i, j, c, password := parseLine(line)
	if i < 0 {
		return false
	}
	if j > len(password) {
		return false
	}
	ch := c[0]
	a := password[i-1]
	b := password[j-1]
	return (a == ch || b == ch) && a != b
}

var reLine = regexp.MustCompile(`^(\d+)-(\d+) (.): (.+)$`)

func parseLine(line string) (int, int, string, string) {
	m := reLine.FindStringSubmatch(line)
	if m == nil {
		return -1, 0, "", ""
	}
	a, _ := strconv.Atoi(m[1])
	b, _ := strconv.Atoi(m[2])
	return a, b, m[3], m[4]
}

func main() {
	part1Count := 0
	part2Count := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		if isValidPart1(line) {
			part1Count++
		}
		if isValidPart2(line) {
			part2Count++
		}
	}

	fmt.Println("part 1:", part1Count)
	fmt.Println("part 1:", part2Count)
}
