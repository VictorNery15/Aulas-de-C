// Arrays
#include<stdio.h>

int main(){

    int v[5] = {1, 1, 1, 1, 1};
    int i;
    float m;

    printf("\nDigite 5 valores.\n");

    for (i=0; i<5; i++)
    {
        printf("%d: ", i+1);
        scanf("%d", &v[i]);

        m += v[i];
    }

    printf("\nValores inseridos:\n");
    for (i = 0; i < 5; i++)
    {
        printf("%d ", v[i]);
    }
    

    printf("\n\nMedia: %.1f\n\n", m/5);

    return 0;

}



/*
int main(){

    int v[5];
    float m;

        printf("\nDigite 5 valores.\n1: ");
        scanf("%d", &v[0]);
        
        printf("2: ");
        scanf("%d", &v[1]);

        printf("3: ");
        scanf("%d", &v[2]);

        printf("4: ");
        scanf("%d", &v[3]);

        printf("5: ");
        scanf("%d", &v[4]);

        m = (v[0] + v[1] + v[2] + v[3] + v[4]) / 5;

        printf("Media: %.2f\n\n", m);

    return 0;
}
*/