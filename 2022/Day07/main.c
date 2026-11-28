// Daniela Rigoli
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


// add recursivity
int solution(const char *input) {
    line[strcspn(line, "\n")] = '\0'; // Remove newline character

    if (strncmp(line, "$ cd ", 5) == 0) {
        // Change directory command
        StackEntry *parent = peek(&stack);

        char *dirName = line + 5;
        if (strcmp(dirName, "/") == 0) {
            // Go to root: clear stack and push root
            while (stack.top >= 0) pop(&stack);
            push(&stack, "/");
        } else if (strcmp(dirName, "..") == 0) {
            // Go up one level: pop the current directory
            StackEntry dir = pop(&stack);
            if (dir.size <= 100000) {
                totalSumP1 += dir.size; // Add to total if size ≤ 100,000
            } 

            if (parent != NULL) {
                // Add size to the parent directory (if exists)
                parent->size += dir.size;
            }

            // Save the size of the directory
            printf("Name: %s, size: %d \n", dir.name, dir.size);
            directorySizes[dirCount++] = dir.size;

        } else {
            // Go into a subdirectory: push it onto the stack
            push(&stack, dirName);
        }
    } else if (strncmp(line, "$ ls", 4) == 0) {
        // List directory contents, do nothing
    } else if (strncmp(line, "dir ", 4) == 0) {
        // Directory entry, do nothing
    } else {
        // File entry
        int size;
        char fileName[MAX_NAME_LEN];
        sscanf(line, "%d %s", &size, fileName);

        // Add file size to the current directory
        StackEntry *current = peek(&stack);
        if (current != NULL) {
            current->size += size;
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

    int result = solution(input);
    

    return 0;
}
