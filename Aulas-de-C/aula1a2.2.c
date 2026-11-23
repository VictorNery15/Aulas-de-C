#include <stdio.h>

int main()
{
    int idade = 0;
    int ano = 2000;
    float peso = 0.0;
    

    printf("\nDigite uma idade: ");
    scanf("%d", &idade);

    printf("Digite um ano: ");
    scanf("%d", &ano);

    printf("Digite um peso: ");
    scanf("%f", &peso);

    printf("\nIdade informada: %d.\n", idade);
    printf("Ano informado: %d.\n", ano);
    printf("Peso informado: %.2f.\n\n", peso);

}