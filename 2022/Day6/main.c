#include <stdio.h>
#include <string.h>
#include <stdbool.h>


// return true if the input[endMarker] is in the interval from startMarker and endMarker-1
// else false
// O(markerSize)
int find(const char *window, int start, int end){
    for(int i = 0; i < end-1; i++){
        if(window[i] == window[j]){
            return i;
        }
    }
    return -1;
}

// day 6 solution O(n*markerSize)
int findMarker(const char *input, int markerSize) {
    int dataLength = strlen(input);
    int startMarker = 0;
    int endMarker = 0;
    while(endMarker - startMarker > markerSize){
        // check if the input[endMarker] is in the interval from startMarker and endMarker-1
        int find = find(&input[startMarker], startMarker, endMarker)
        if(find(&input[startMarker], startMarker, endMarker)){
            startMarker = find+1 + startMarker;
        }
        endMarker++;
    }
    
    return endMarker;
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
