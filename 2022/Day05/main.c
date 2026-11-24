#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACKS 10
#define MAX_CRATES_PER_STACK 100
#define MAX_LINE_LENGTH 100

// Structure to represent a stack of crates
typedef struct {
    char crates[MAX_CRATES_PER_STACK];
    int top;
} Stack;
void push(Stack *stack, char crate) {
    stack->crates[++stack->top] = crate;
}
char pop(Stack *stack) {
    return stack->crates[stack->top--];
}

void moveCrates(Stack *from, Stack *to, int num) {
    char temp[MAX_CRATES_PER_STACK];
    for (int i = 0; i < num; i++) {
        temp[i] = pop(from);
    }
    for (int i = num - 1; i >= 0; i--) {
        push(to, temp[i]);
    }
}
void printTopCrates(Stack stacks[], int numStacks) {
    for (int i = 0; i < numStacks; i++) {
        if (stacks[i].top >= 0) {
            printf("%c", stacks[i].crates[stacks[i].top]);
        } else {
            printf(" ");
        }
    }
    printf("\n");
}

void parseInitialStacks(Stack stacks[], char lines[][MAX_LINE_LENGTH], int numStacks, int numLines) {
    for (int i = numLines - 1; i >= 0; i--) {
        int stackIndex = 0;
        for (int j = 1; j < strlen(lines[i]); j += 4) {
            if (lines[i][j] != ' ') {
                push(&stacks[stackIndex], lines[i][j]);
            }
            stackIndex++;
        }
    }
}

int main() {
    Stack stacks[MAX_STACKS];
    for (int i = 0; i < MAX_STACKS; i++) {
        stacks[i].top = -1;
    }
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    char line[MAX_LINE_LENGTH];
    char stackLines[10][MAX_LINE_LENGTH];
    int lineCount = 0;
    int stackLineCount = 0;

    while (fgets(line, sizeof(line), file)) {
        if (strchr(line, '[') != NULL) {
            strcpy(stackLines[stackLineCount++], line);
        }
    }
    int numStacks = (strlen(stackLines[stackLineCount - 1]) + 1) / 4; // Get number of stacks from the last line
    parseInitialStacks(stacks, stackLines, numStacks, stackLineCount);
    fseek(file, 0, SEEK_SET);
    while (fgets(line, sizeof(line), file)) {
        if (strncmp(line, "move", 4) == 0) {
            break;
        }
    }
    do {
        int numCrates, fromStack, toStack;
        sscanf(line, "move %d from %d to %d", &numCrates, &fromStack, &toStack);
        moveCrates(&stacks[fromStack - 1], &stacks[toStack - 1], numCrates);
    } while (fgets(line, sizeof(line), file));
    fclose(file);
    printTopCrates(stacks, numStacks);
    return 0;
}
