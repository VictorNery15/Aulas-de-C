// Aula de Variaveis e Atribuição
#include <stdio.h>
#define texto "Entrada e saida de dados."

int main()
{
    printf("\n%s\n\n", texto);

    int idade = 0;
    float peso = 0.0;
    char nome[50] = "";

    printf("Digite uma idade: ");
    scanf("%d", &idade);

    printf("Digite um peso: ");
    scanf("%f", &peso);

    printf("Digite um nome: ");
    scanf("%s", nome);

    printf("\nDados informados:\n\n");

    printf("Idade informada: %d\n", idade);
    printf("Peso informadado: %.2f\n", peso);
    printf("Nome informado: %s\n", nome);

}