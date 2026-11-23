//Operadores lógicos e condições complexas
#include <stdio.h>

int main()
{
    float nota;

    printf("\nDigite sua nota: ");
    scanf("%f", &nota);

    if(nota >= 7.0)
    {
        printf("\nAprovado!!\n\n");
    }

    // if (4.0 >= nota < 7) = err
    // if (nota >= 4.0 && nota < 7.0) = roda
    else if (nota >= 4.0 && nota < 7.0)
    {
        printf("\nTem direito a exame.\n\n");
    }

    else
    {
        printf("\nReprovado.\n\n");
    }

    return 0;
}