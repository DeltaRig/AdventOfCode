#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Returns the index of a duplicate in the window, or -1 if don't find
int finder(const char *window, int start, int end) {
    for (int i = start; i < end; i++) {
        if (window[i] == window[end]) {
            return i;
        }
    }
    return -1;
}

int findMarker(const char *input, int markerSize) {
    int dataLength = strlen(input);
    int startMarker = 0;
    int endMarker = 0;
    int find = -1;

    while (endMarker < dataLength) {
        // Check if the current character creates a duplicate in the window
        find = finder(input, startMarker, endMarker);
        if (find >= 0) {
            // Adjust the startMarker to skip past the duplicate
            startMarker = find + 1;
        }
        endMarker++;
        if ((endMarker - startMarker) == markerSize) {
            return endMarker;
        }
    }
    return -1;
}

int main() {
    // Open the input file
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    char input[10000]; // Buffer to store the input
    if (fgets(input, sizeof(input), file) == NULL) {
        printf("Error reading the file!\n");
        fclose(file);
        return 1;
    }
    fclose(file); // Close the file after reading

    // Remove newline character if present
    input[strcspn(input, "\n")] = '\0';

    // Part 1: Find the first start-of-packet marker (4 distinct characters)
    int marker = findMarker(input, 4);
    if (marker != -1) {
        printf("Part 1: First start-of-packet marker after character %d\n", marker);
    } else {
        printf("Part 1: Start-of-packet marker not found\n");
    }

    // Part 2: Find the first start-of-message marker (14 distinct characters)
    marker = findMarker(input, 14);
    if (marker != -1) {
        printf("Part 2: First start-of-message marker after character %d\n", marker);
    } else {
        printf("Part 2: Start-of-message marker not found\n");
    }

    return 0;
}
