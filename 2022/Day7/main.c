#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 100
#define MAX_CHILDREN 100

// Structure for a directory or file
typedef struct Node {
    char name[MAX_NAME_LEN];
    int size; // File size or 0 if it's a directory
    struct Node *parent;
    struct Node *children[MAX_CHILDREN];
    int childCount;
} Node;

// Create a new node (directory or file)
Node *createNode(const char *name, int size, Node *parent) {
    Node *node = (Node *)malloc(sizeof(Node));
    strcpy(node->name, name);
    node->size = size;
    node->parent = parent;
    node->childCount = 0;
    return node;
}

// Add a child to a directory
void addChild(Node *parent, Node *child) {
    parent->children[parent->childCount++] = child;
}

// Parse the input and build the filesystem
Node *parseInput(FILE *file) {
    char line[256];
    Node *root = createNode("/", 0, NULL);
    Node *current = root;

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0'; // Remove newline character

        if (strncmp(line, "$ cd ", 5) == 0) {
            // Change directory command
            char *dirName = line + 5;
            if (strcmp(dirName, "/") == 0) {
                current = root; // Go to root
            } else if (strcmp(dirName, "..") == 0) {
                current = current->parent; // Go up one level
            } else {
                // Find or create the directory
                for (int i = 0; i < current->childCount; i++) {
                    if (strcmp(current->children[i]->name, dirName) == 0) {
                        current = current->children[i];
                        break;
                    }
                }
            }
        } else if (strncmp(line, "$ ls", 4) == 0) {
            // List directory contents, do nothing
        } else if (strncmp(line, "dir ", 4) == 0) {
            // Directory entry
            char *dirName = line + 4;
            Node *dir = createNode(dirName, 0, current);
            addChild(current, dir);
        } else {
            // File entry
            int size;
            char fileName[MAX_NAME_LEN];
            sscanf(line, "%d %s", &size, fileName);
            Node *file = createNode(fileName, size, current);
            addChild(current, file);
        }
    }

    return root;
}

// Recursively calculate the total size of a directory
int calculateSize(Node *node, int *totalSum) {
    if (node->size > 0) {
        return node->size; // File size
    }

    int totalSize = 0;
    for (int i = 0; i < node->childCount; i++) {
        totalSize += calculateSize(node->children[i], totalSum);
    }

    if (totalSize <= 100000) {
        *totalSum += totalSize; // Add to total sum if size ≤ 100000
    }

    return totalSize;
}


int main() {
    // Open the input file
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Parse the input and build the filesystem tree
    Node *root = parseInput(file);
    fclose(file);

    // Calculate the total sizes of directories
    int totalSum = 0;
    calculateSize(root, &totalSum);

    // Print the result
    printf("Sum of total sizes of directories ≤ 100,000: %d\n", totalSum);

    return 0;
}
