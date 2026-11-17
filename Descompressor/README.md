Challenge created by João Batista de Oliveira

Solution developed by Daniela Rigoli at 2026

# Description
The purpose of this program is to calculate the length of a decompressed string without actually reconstructing the entire string in memory.

Instead of expanding all encoded sequences, the program uses recursion and memoization to calculate how many characters the decompressed result would contain. It also uses BigInt to support results that may exceed the limits of standard integer types.

## Each structure has a specific responsibility:
* **dic:** Maps each encoded character to its corresponding encoded sequence.
* **memo:**	Stores the decompressed length of characters that have already been processed.
* **keys:**	Stores all characters that appear as dictionary keys.
* **appearsInValue:**	Stores all characters that appear inside dictionary values.

For example, given:
```
a bc
b xy
c z
```

The dictionary would contain:
```
a -> bc
b -> xy
c -> z
```

# Solution
## Identifying the Root

After reading the input, the program searches for the root character. The root is a dictionary key that never appears inside another dictionary value.

In other words, it is a character that has a definition but is never referenced by another definition.

## Recursive Decompression

The central part of the algorithm is the descompress() method.

This method calculates the decompressed length of a given string without generating the actual decompressed content.

It works through the following steps:
1. Initialize result to zero.
2. Iterate over every character in the input string.
3. Check whether the character exists as a key in the dictionary using dic.count(ch).
4. If the character exists in the dictionary, it represents an encoded sequence that needs to be expanded.
5. Before expanding it, check whether its decompressed length has already been calculated using memo.count(ch).
6. If the result is available in the memoization map, reuse it instead of performing the recursive calculation again.
7. Otherwise, recursively calculate the decompressed length of the corresponding dictionary value and store the result in memo.
8. If the character does not exist in the dictionary, it represents a literal character, so increment the result by one.

Finally, the method returns the total decompressed length.

# Algorithm Analysis

## Recursion
Recursion allows the algorithm to process nested encoded sequences without explicitly reconstructing the entire decompressed string.

Each dictionary entry can reference other entries, creating multiple levels of expansion. The recursive method follows these references until it reaches characters that do not have dictionary definitions.

## Memoization
Memoization is an important optimization in this implementation.

Without memoization, the same dictionary entry could be expanded multiple times whenever it appears in different sequences.

The memo map avoids this repetition by storing previously calculated decompressed lengths.

For example, if the character b appears several times, its decompressed length only needs to be calculated once. Subsequent occurrences reuse the stored value.

This is particularly useful when dictionary entries are shared by multiple other entries.

## Complexity Considerations
Let:
- \(n\) represent the total number of characters across all dictionary values.
- \(V\) represent the number of dictionary entries.
With memoization, each dictionary entry is expanded at most once, assuming the dictionary represents an acyclic dependency structure.

Under these assumptions, the algorithm takes approximately:
- Time complexity: \(O(n + V)\) dictionary-processing operations.
- Space complexity: \(O(V)\) for memoization, excluding the dictionary itself and the recursion stack.
The actual execution time also depends on the cost of BigInt arithmetic, which increases as the calculated numbers become larger.

# Results

The following table presents the results obtained from the decompression algorithm for four different input files. The experiment evaluates the execution time, the total number of characters in the decompressed output, and the root character identified in each dictionary.

| Case                | Duration (µs)	 | Decompressed Characters | Root |
| ------------------- | ---------------- | ------ | ------ |
| x1.txt | 14 | 47 |a |
| x6.txt | 159 | 4083286957 |j |
| x8.txt | 141 | 90535253 |q |
| x10.txt | 237 | 38547615053 |i |

**Duration:** Represents the time required by identify the root and descompress() method to calculate the decompressed length, measured in microseconds.

**Decompressed Characters:** Indicates the total number of characters that would exist after fully decompressing the root sequence. The algorithm calculates this value without actually constructing the resulting string.

**Root:** Represents the initial character identified by the program. It is the dictionary key that does not appear in any dictionary value.

# How to execute

Command to compile:
> g++ mainlong.cpp -o o.exe

Command to execute:
> o.exe <filename>