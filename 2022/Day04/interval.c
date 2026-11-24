// Daniela Rigoli - Aug 24 2024
// https://adventofcode.com/2022/day/4
// part 2
// In how many assignment pairs does one range fully contain the other?
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// part 1
// return 1 if interval 1 fully contains or contained interval 2
int fullyContains(int start1, int end1, int start2, int end2) //multiplica recebe N1,N2 e retorna um int
{
    if(start1 <= start2 && end1 >= end2)
        return 1;
    else if(start2 <= start1 && end2 >= end1)
        return 1;
    else {
        return 0;
    }
}

// part 2
// return 1 when have overlap
int overlap(int start1, int end1, int start2, int end2)
{
    if(fullyContains(start1, end1, start2, end2))
        return 1;
    else if(end2 == start1 || end1 == start2)
        return 1;
    else if((start1 < start2 && end1 > start2) || (start2 < start1 && end2 > start1))
        return 1;
    else {
        return 0;
    }
}

int main()
{
    FILE * f = stdin;
    char token[100]; 
    int p1 = 0;
    int p2 = 0;
    
    int start1, end1, start2, end2;
    while ( 4 == scanf(f,"%d-%d,%d-%d", &start1, &end1, &start2, &end2)){
        p1 += fullyContains(start1, end1, start2, end2);
        p2 += overlap(start1, end1, start2, end2);
    }
    printf("\nIn how many assignment pairs does one range fully contain the other? %d\n", p1);
    printf("\nIn how many assignment pairs do the ranges overlap? %d\n", p2);
}
