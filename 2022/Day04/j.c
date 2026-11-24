// JB

#include <stdio.h>
#include <stdlib.h>

int min(int a, int b){ return (a < b ? a : b);}
int max(int a, int b){ return (a > b ? a : b);}

void main(){
    int acc = 0, acc2 = 0;
    unsigned int a1, a2, b1, b2;
    while(4 == scanf("%d-%d,%d-%d", &a1, &a2, &b1, &b2)){
        if(a1 <= b1 && b2 <= a2) acc++;
            else
                if(b1 <= a1 && a2 <= b2 ) acc++;
            int c1 = max(a1, b1);
            int c2 = min(a2, b2);
            if(c1 <= c2) acc2++;
    }
    printf("Parte 1: %d\n", acc);
    printf("Parte 2: %d\n", acc2);
}
