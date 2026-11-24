#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool allUnique(const char *window, int length) {
    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) {
            if (window[i] == window[j]) {
                return false;
            }
        }
    }
    return true;
}

// day 6 solution O()
int findMarker(const char *input, int markerSize) {
    int dataLength = strlen(input);
    for (int i = 0; i <= dataLength - markerSize; i++) {
        if (allUnique(&input[i], markerSize)) {
            return i + markerSize;
        }
    }
    return -1; // Not found
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
