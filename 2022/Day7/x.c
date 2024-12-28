// created by JB 2024
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TreeNode {
  int size;
  char name[24];
  struct TreeNode *sub, *brod;
} TreeNode;

TreeNode * newTreeNode( ) {
  TreeNode *p = malloc( sizeof ( TreeNode ) );
  p->size = 0;
  p->sub = p->brod = NULL;
  strcpy( p->name, "" );
  return p;
}

TreeNode * TreeSort( TreeNode * p ) {
  if ( p == NULL ) return p;
  p->brod = TreeSort( p->brod );
  if ( p->brod && strcmp( p->name, p->brod->name ) > 0 ) {
    TreeNode * ax = p->brod;
    p->brod = p->brod->brod;
    ax->brod = TreeSort( p );
    p = ax;
  }
  p->sub = TreeSort( p->sub );
  return p;
}

int inicia( char a[], char b[] ) {
  return strncmp( a, b, strlen( b ) ) == 0;
}

TreeNode * TreeBuild(FILE *file) {
  char lin[24];

   if (fgets(lin, sizeof(lin), file) == NULL) return NULL;
  if ( inicia( lin, "$ cd .." ) ) return NULL;
  if ( inicia( lin, "$ ls" ) ) return TreeBuild(file);
  if ( inicia( lin, "dir" ) ) return TreeBuild(file);

  TreeNode * p = newTreeNode( );

  if ( inicia( lin, "$ cd " ) ) {
    sscanf( lin + 5, "%s", p->name );
    p->sub = TreeBuild(file);
  } else
    sscanf( lin, "%d %s", &p->size, p->name );

  p->brod = TreeBuild(file);
  return p;
}

void TreePrint( TreeNode * p, int dep ) {
  if ( p == NULL ) return;
  printf( "%*s%s (%d)\n", dep, " ", p->name, p->size );
  TreePrint( p->sub, dep + 4 );
  TreePrint( p->brod, dep );
}

int TreeSizes( TreeNode * p ) {
  if ( p == NULL ) return 0;
  p->size += TreeSizes( p->sub );
  return p->size + TreeSizes( p->brod );
}

// method created by Daniela Rigoli to solve Part 1 Day 7 2022
int SumAtMost(TreeNode *p, int atMost) {
  if (p == NULL) return 0;

  int sum = 0;
  if (p->sub != NULL && p->size <= atMost) {
    sum += p->size;
  }
  sum += SumAtMost(p->sub, atMost);
  sum += SumAtMost(p->brod, atMost);

  return sum;
}

// method created by Daniela Rigoli to solve Part 2 from Day 7 2022
int SmallesToDelete(TreeNode *p, int best, int used, int needed) {
  int diskSpace =70000000; 
  if (p == NULL) return best;

  int sum = 0;
  if (p->sub != NULL && p->size < best && diskSpace - (used - p->size) > needed) {
   // printf("Name: %s %d becasue best %d and will used %d and is free %d \n", p->name, p->size, best, (used - p->size),(diskSpace - (used - p->size)));
    best = p->size;
  }
  int sub = SmallesToDelete(p->sub, best, used, needed);
  int brod = SmallesToDelete(p->brod, best, used, needed);

 // printf("sub %d  brod %d\n",sub, brod );
  best = best < sub ? best : sub;
  return best < brod ? best: brod;
}


int main ( ) {
  FILE *file = fopen("input.txt", "r");
  if (file == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  TreeNode *root = TreeBuild(file);
  fclose(file);

  int size = TreeSizes(root);
  printf("Total size: %d\n\n", size);
  root = TreeSort( root );
  TreePrint(root, 0);
  
  int p1 = SumAtMost(root, 100000);
  printf("Part 1: %d\n\n", p1);

  int p2 = SmallesToDelete(root, size, size, 30000000);
  printf("Part 2: %d\n\n", p2);
  return 0;
}

