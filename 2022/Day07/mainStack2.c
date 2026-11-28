#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 100
#define MAX_STACK_SIZE 100
//                       12559192
#define TOTAL_DISK_SPACE 70000000
#define REQUIRED_UNUSED_SPACE 30000000

// Stack entry for a directory
typedef struct {
    char name[MAX_NAME_LEN];
    int size; // Cumulative size of the directory
} StackEntry;

// Stack structure
typedef struct {
    StackEntry entries[MAX_STACK_SIZE];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack *stack) {
    stack->top = -1;
}

// Push an entry onto the stack
void push(Stack *stack, const char *name) {
    if (stack->top >= MAX_STACK_SIZE - 1) {
        printf("Stack overflow!\n");
        exit(1);
    }
    stack->top++;
    strcpy(stack->entries[stack->top].name, name);
    stack->entries[stack->top].size = 0;
}

// Pop an entry from the stack
StackEntry pop(Stack *stack) {
    if (stack->top < 0) {
        printf("Stack underflow!\n");
        exit(1);
    }
    return stack->entries[stack->top--];
}

// Peek at the top entry of the stack
StackEntry *peek(Stack *stack) {
    if (stack->top < 0) {
        return NULL;
    }
    return &stack->entries[stack->top];
}

int main() {
    // Open the input file
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    char line[256];
    Stack stack;
    initStack(&stack);
    push(&stack, "/"); // Start at the root directory

    int totalSumP1 = 0;
    int totalUsedSpace = 0;

    // Array to track directory sizes for part two
    int directorySizes[MAX_STACK_SIZE];
    int dirCount = 0;

    while (fgets(line, sizeof(line), file)) {
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
    }

    fclose(file);

    // Process any remaining directories in the stack
    while (stack.top >= 0) {
        StackEntry dir = pop(&stack);

        // Save the size of the directory
        printf("Name: %s, size: %d \n", dir.name, dir.size);
        directorySizes[dirCount++] = dir.size;

        // Add size to the parent directory (if exists)
        StackEntry *parent = peek(&stack);
        if (parent != NULL) {
            parent->size += dir.size;
        }

        // Track the total used space
        if (stack.top < 0) {
            totalUsedSpace = dir.size; // Root directory size
        }
    }

    // Calculate the space needed
    int unusedSpace = TOTAL_DISK_SPACE - totalUsedSpace;
    int spaceToFree = REQUIRED_UNUSED_SPACE - unusedSpace;

    // Find the smallest directory that can be deleted (part 2)
    int smallestDirSize = TOTAL_DISK_SPACE;
    for (int i = 0; i < dirCount; i++) {
        if (directorySizes[i] >= spaceToFree && directorySizes[i] < smallestDirSize) {
            smallestDirSize = directorySizes[i];
        }
    }

    // Print the result part 1
    printf("Sum of total sizes of directories ≤ 100,000: %d\n", totalSumP1);
    
    // Part 2
    printf("Total used space: %d\n", totalUsedSpace);
    printf("Total unusedSpace: %d\n", unusedSpace);

    printf("Total space to free: %d\n", spaceToFree);


    printf("Smallest directory size to delete: %d\n", smallestDirSize);

    return 0;
}
