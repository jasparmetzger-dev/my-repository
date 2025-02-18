//runoff.c

#include<stdio.h>
#include<stdbool.h>
#include<cs50.h>
#include<string.h>
#include<stdlib.h>

typedef struct
{
    string name;
    int votes;
    bool eliminated;
}ca;

ca cands[9];

int voter_count; //num of voters
int ca_count; //num of cands
int big = 0; //biggest number of votes on a candidate
int n = 3; //votes per voter
int preference[9][voter_count]; // 77777777777777777777
void count_f(int);

int main(int argc, string argv[])
{

        // get candidates

    if (argc > 9)
    {
        printf("Error\n");
        return 1;
    }

        //define cands

    for (int i = 0; i < argc; i++)
    {
        cands[i].name = argv[i + 1];
        cands[i].votes = 0;
        cands[i].eliminated = false;
    }
    ca_count = argc;

        //get voters

    voter_count = get_int("Number of voters: ");

        //get votes

    int preference[argc][voter_count];

    for (int i = 0; i < voter_count; i++) //for every voter
    {
        for (int j = 0; j < n; j++)    //on their n (3) amount of picks
        {
            string vote = get_string("Vote %i: ", j + 1);
            bool B = false;
            for (int k = 0; k < argc; k++)
            {
                if (strcmp(cands[k].name, vote) == 0) //if candidate == vote
                {
                    preference[k][i] = j; //the number for the preference of each candidate(k) from each voter [i] = the place the voted them on (j)
                    B = true;
                }

            }
            if (B == false) //Error if noone was voted
            {
                printf("Usage: Vote: 'Candidate'\n");
                return 2;
            }
        }
        printf("\n");
    }

        //compute votes


    int comp = argc; //define all the competitors
    count_f(comp);

    for(int i = 0; i < argc; i++)
    {
        if (cands[i].eliminated == false)
        {
            printf("Winner %i: %s with %i votes\n", i + 1, cands[i].name, big);
        }
    }
    return 0;
}



void count_f(int co)
{
    for (int p = 0; p < n; p++) //check three times
    {
        if (co == 1) //if one has the most votes, stopp
        {
            return;
        }

        for (int i = 0; i < voter_count; i++) //for all voters
        {
            for (int k = 0; k < co; k++) //check if theyre voted on try n
            {
                if (preference[k][i] == p)
                        cands[i].votes++; //add
            }

            if (cands[i].votes > big)
                big = cands[i].votes; //get int big
        }
        int randomcounter = 0;
        for (int i = 0; i < co; i++) //for every comp
        {
            if (cands[i].votes != big)
            {
                cands[i].eliminated = true; //if they arent tied for first, make room for more votes through elimination
                co--;
            }
            else
                randomcounter++; //check if everyone is tied

        }
        if (randomcounter == co) //not at top cus ranodomcounter has to reset every time
        {
            return;
        }
    }
    Printf("Error 3\n");
}
