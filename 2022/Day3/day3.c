#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// JB
// https://adventofcode.com/2022/day/3
// part 2
// Function to process three lines
int main()
{
    FILE * f = stdin;
    char s1[100];
    char s2[100];
    char s3[100];
    int acc = 0;

    while ( 3 == fscanf(f, "%s %s %s", s1, s2, s3)){
        char p1[256] = {};
        char p2[256] = {};
        char p3[256] = {};

        int i, len;
        len = strlen(s1);
        for( i =0; i < len; i++) p1[s1[i]]=1;
        len = strlen(s2);
        for( i =0; i < len; i++) p2[s2[i]]=1;
        len = strlen(s3);
        for( i =0; i < len; i++) p3[s3[i]]=1;
        for(i =0; i<256; i++)
            if(p1[i] > 0 && p2[i] > 0 && p3[i] > 0){
                int a = i;
                if( a >= 'a' && a <= 'z') a = a - 'a' + 1;
                else a = a - 'A' + 27;
                acc += a;
            }
    }
    printf("\n%d\n", acc);
}
