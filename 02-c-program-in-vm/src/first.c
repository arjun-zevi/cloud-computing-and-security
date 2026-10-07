#include <stdio.h>

int main(void)
{
    int a;
    printf("Enter the number to find Even Or Not: ");
    scanf("%d", &a);
    if (a % 2 == 0)
        printf("The Entered number is Even\n");
    else
        printf("The Entered number is Odd\n");
    return 0;
}
