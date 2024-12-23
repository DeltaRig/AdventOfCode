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

int main ( ) {
  FILE *file = fopen("input.txt", "r");
  if (file == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  TreeNode *root = TreeBuild(file);
  fclose(file);

  int size = TreeSizes(root);
  printf("Total size: %d\n", size);
  TreePrint(root, 0);
  
  return 0;
}
