#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;
    while (1)
    {
        printf("Change owed: ");
        if (scanf("%d", &cents) != 1)
        {
            while (getchar() != '\n')
                ;
            continue;
        }

        if (cents >= 0)
        {
            break;
        }
    }

    int coins = 0;

    coins += cents / 25;
    cents %= 25;

    coins += cents / 10;
    cents %= 10;

    coins += cents / 5;
    cents %= 5;

    coins += cents;

    printf("%d\n", coins);
    return 0;
}
