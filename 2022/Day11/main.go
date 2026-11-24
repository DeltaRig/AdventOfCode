// Daniela Rigoli November 2026
// Advent of Code 2022 - Day 11
// https://adventofcode.com/2022/day/11
// Usage: go run main.go <phase> <rounds>


package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"sort"
)

type Monkey struct {
	Items      []int64
	Operator   byte
	Operand    int64
	UseOld    bool
	Divisor    int64
	IfTrue    int
	IfFalse   int
	Inspected int64
}

func (m *Monkey) apply(old int64) int64 {
	operand := m.Operand
	if m.UseOld {
		operand = old
	}

	switch m.Operator {
	case '+':
		return old + operand
	case '*':
		return old * operand
	default:
		panic("unknown operator")
	}
}

func simulate(monkeys []Monkey, rounds int) int64 {
	for round := 0; round < rounds; round++ {
		for i := range monkeys {
			m := &monkeys[i]

			// Processa todos os itens, inclusive os que
			// eventualmente forem adicionados durante o turno.
			for len(m.Items) > 0 {
				item := m.Items[0]
				m.Items = m.Items[1:]

				m.Inspected++

				// Aplica a operação de preocupação.
				item = m.apply(item)

				// Part 1: o macaco fica aliviado.
				item /= 3

				// Decide para qual macaco enviar.
				target := m.IfFalse
				if item%m.Divisor == 0 {
					target = m.IfTrue
				}

				monkeys[target].Items = append(
					monkeys[target].Items,
					item,
				)
			}
		}
	}

	// Coleta os totais de inspeção.
	counts := make([]int64, len(monkeys))
	for i, m := range monkeys {
		counts[i] = m.Inspected
		fmt.Printf("Monkey %d inspected %d items\n",
			i, m.Inspected)
	}

	// Ordena do maior para o menor.
	sort.Slice(counts, func(i, j int) bool {
		return counts[i] > counts[j]
	})

	// Monkey business = os dois maiores multiplicados.
	return counts[0] * counts[1]
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int64) int64 {
	return a / gcd(a, b) * b
}

func getModulus(monkeys []Monkey) int64 {
	mod := int64(1)

	for _, m := range monkeys {
		mod = lcm(mod, m.Divisor)
	}

	return mod
}

func simulateP2(monkeys []Monkey, rounds int) int64 {
	mod := getModulus(monkeys)

	for round := 0; round < rounds; round++ {
		for i := range monkeys {
			m := &monkeys[i]

			// Processa todos os itens, inclusive os que
			// eventualmente forem adicionados durante o turno.
			for len(m.Items) > 0 {
				item := m.Items[0]
				m.Items = m.Items[1:]

				m.Inspected++

				// Aplica a operação de preocupação.
				item = m.apply(item)

				// Part 1: o macaco fica aliviado.
				item %= mod

				// Decide para qual macaco enviar.
				target := m.IfFalse
				if item%m.Divisor == 0 {
					target = m.IfTrue
				}

				monkeys[target].Items = append(
					monkeys[target].Items,
					item,
				)
			}
		}
	}

	// Coleta os totais de inspeção.
	counts := make([]int64, len(monkeys))
	for i, m := range monkeys {
		counts[i] = m.Inspected
		fmt.Printf("Monkey %d inspected %d items\n",
			i, m.Inspected)
	}

	// Ordena do maior para o menor.
	sort.Slice(counts, func(i, j int) bool {
		return counts[i] > counts[j]
	})

	// Monkey business = os dois maiores multiplicados.
	return counts[0] * counts[1]
}

func parseMonkeys(r io.Reader) ([]Monkey, error) {
	scanner := bufio.NewScanner(r)
	var monkeys []Monkey
	var m Monkey
	var insideMonkey bool

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		if line == "" {
			continue
		}

		if strings.HasPrefix(line, "Monkey ") {
			if insideMonkey {
				monkeys = append(monkeys, m)
			}

			m = Monkey{}
			insideMonkey = true
			continue
		}

		switch {
		case strings.HasPrefix(line, "Starting items:"):
			raw := strings.TrimPrefix(line, "Starting items:")
			raw = strings.TrimSpace(raw)

			if raw == "" {
				m.Items = []int64{}
				continue
			}

			for _, item := range strings.Split(raw, ",") {
				item = strings.TrimSpace(item)

				n, err := strconv.ParseInt(item, 10, 64)
				if err != nil {
					return nil, err
				}

				m.Items = append(m.Items, n)
			}

		case strings.HasPrefix(line, "Operation:"):
			fields := strings.Fields(line)

			// Example: Operation: new = old * 19
			m.Operator = fields[4][0]

			if fields[5] == "old" {
				m.UseOld = true
			} else {
				n, err := strconv.ParseInt(fields[5], 10, 64)
				if err != nil {
					return nil, err
				}
				m.Operand = n
			}

		case strings.HasPrefix(line, "Test:"):
			fields := strings.Fields(line)
			n, err := strconv.ParseInt(fields[len(fields)-1], 10, 64)
			if err != nil {
				return nil, err
			}
			m.Divisor = n

		case strings.HasPrefix(line, "If true:"):
			fields := strings.Fields(line)
			m.IfTrue, _ = strconv.Atoi(fields[len(fields)-1])

		case strings.HasPrefix(line, "If false:"):
			fields := strings.Fields(line)
			m.IfFalse, _ = strconv.Atoi(fields[len(fields)-1])
		}
	}

	if insideMonkey {
		monkeys = append(monkeys, m)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return monkeys, nil
}



func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	monkeys, err := parseMonkeys(file)
	if err != nil {
		log.Fatal(err)
	}
	// receive by parameter the number of rounds to simulate
	toGetAllArgs := os.Args[1:]
	typeSim := toGetAllArgs[0]
	r, _ := strconv.Atoi(toGetAllArgs[1])

	if typeSim == "1" {
		
		fmt.Println("--- Result for " + strconv.Itoa(r) + " rounds p1---")
		result := simulateP2(monkeys, r)
		fmt.Println("Monkey business:", result)
	} else {
		
		fmt.Println("--- Result for " + strconv.Itoa(r) + " rounds p2 ---")
		result := simulateP2(monkeys, r)
		fmt.Println("Monkey business:", result)
	}
	
	
	

}
