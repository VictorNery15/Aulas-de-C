// do while
#include<stdio.h>

int main(){
    int a = 1;

    do{
        printf("| %d |", a);
        a++;
    }while (a < 11);

    int n = 1;

    do{
        if(n<0 || n>11) {
            printf("!!ERRO!!\nPadrao irregular detectado!!\nTente novamente!");
        }
        printf("\nDigite sua nota: ");
        scanf("%d", &n);
        printf("\n");
    
    }while(n<0 || n>11);

    return 0;
}