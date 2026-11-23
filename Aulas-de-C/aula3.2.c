// Aula de Operadores Aritimeicos
#include <stdio.h>

int main()
{

    int a, b, soma, subt, mult, div;

    printf("\nDigite um valor: ");
    scanf("%d", &a);
    printf("Digite outro valor: ");
    scanf("%d", &b);

    soma = a + b;
    subt = a - b;
    mult = a * b;
    div = a / b;

    printf("\nResultados:\n");
    printf("%d + %d = %d\n", a, b, soma);
    printf("%d - %d = %d\n", a, b, subt);
    printf("%d * %d = %d\n", a, b, mult);
    printf("%d / %d = %d\n", a, b, div);

    int dado = 10;
    printf("\nDado antes do incremento: %d", dado);

    dado++;
    printf("\nDepois do incremento: %d", dado);

    dado--;
    printf("\nDepois do decremento: %d", dado);

    dado += 3;
    printf("\nDepois do incremento: %d", dado);

    dado -= 2;
    printf("\nDepois do decremento: %d", dado);

    dado *= 10;
    printf("\nDepois de mutiplicar: %d", dado);

    dado /= 2;
    printf("\nDepois de dividir: %d", dado);

    return 0;
}