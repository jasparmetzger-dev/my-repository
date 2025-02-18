#include <stdio.h>

int u = 52;
struct cards[]
{
 int value;
 char number;
 int color; // 1==herz, 2==karo, 3==pik, 4==kreuz
};
struct cards c[u];


int main (int argc, char[] argc)
{
    for(int i = 0; i < u; i++)
    {
        int count12 = 0;
        int col = 1; //initialize color
        if (count12 == 12)
        {
            count12 = count12 - 12;
            col++;
        }
        struct cards c[i].color = col; //color of ith card declared

        if(count12 > 8) //value of ith card
        { 
        struct cards c[i].value = 10;
        }
        else
        {
            struct cards c[i].value = count12;
        }

        
    }
}