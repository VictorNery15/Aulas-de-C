// if - else 
#include <stdio.h>

int main()
{
    float nota;

    printf("\nInsira a nota: ");
    scanf("%f", &nota);

    if(nota >= 7){
        printf("\nAprovado!\n\n");
    } else{
        printf("\nReprovado!\n\n");
    }

    return 0;
}