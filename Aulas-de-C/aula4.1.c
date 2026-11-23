// Comando if e Operadores relacionais
/*
7 > 3 = true
3 < 7 = true
7 >= 7 = true
6 <= 6 = true
2 == 2 = true
5 != 1 = true
*/
#include <stdio.h>

int main()
{

    float nota;

    printf("\nDigite sua nota: ");
    scanf("%f", &nota);

    if (nota >= 7.0)
    {
        printf("\nParabens!!\nVoce foi aprovado(a)!\n\n");
    }

    else
    {
        printf("\nVoce foi reprovado(a).\nMelhore sua nota.\n\n");
    }

    return 0;
}