// break e continue
#include<stdio.h>

int main(){

    int i, m;

    printf("\nDigite um numero: ");
    scanf("%d", &i);

    m = i*10;

    for (i = 1; i; i++)
    {

        if(i > m){
            break; // o break encerra o loop
        }

        if (i % 2 == 0){
            continue; // o continue renicia o loop sem executar oque esta apos o mesmo
        }

        printf("%d ", i);
        
    }
    
    return 0;
}