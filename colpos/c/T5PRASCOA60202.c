// COA-602 Tarea 5 Ejercicio 2
/**************************************************************************************************************
Lea 5 enteros positivos diferentes (n1, n2, n3, n4, n5) luego, identifique cual de ellos representa la mediana.
Utilice el concepto de marca y la estrategia para identificar maximos.
**************************************************************************************************************/
#include <stdio.h>
int main()
{

    int n1, n2, n3, n4, n5, pos1, pos2, pos3;
    int max1 = -1, max2 = -1, max3 = -1;
    printf("Ingresar 5 enteros postivos diferentes entre si:\n");
    printf("Ingresar n1:\t");
    scanf("%d", &n1);
    printf("Ingresar n2:\t");
    scanf("%d", &n2);
    printf("Ingresar n3:\t");
    scanf("%d", &n3);
    printf("Ingresar n4:\t");
    scanf("%d", &n4);
    printf("Ingresar n5:\t");
    scanf("%d", &n5);

    //Encontrar primer maximo
    max1 = n1;
    pos1 = 1;
    if (n2 > max1)
    {
        max1 = n2;
        pos1 = 2;
    }
    if (n3 > max1)
    {
        max1 = n3;
        pos1 = 3;
    }
    if (n4 > max1)
    {
        max1 = n4;
        pos1 = 4;
    }
    if (n5 > max1)
    {
        max1 = n5;
        pos1 = 5;
    }
    //Encontrar segundo maximo
    if (n1 > max2)
        if (n1 < max1)
        {
            max2 = n1;
            pos2 = 1;
        }
    if (n2 > max2)
        if (n2 < max1)
        {
            max2 = n2;
            pos2 = 2;
        }
    if (n3 > max2)
        if (n3 < max1)
        {
            max2 = n3;
            pos2 = 3;
        }
    if (n4 > max2)
        if (n4 < max1)
        {
            max2 = n4;
            pos2 = 4;
        }
    if (n5 > max2)
        if (n5 < max1)
        {
            max2 = n5;
            pos2 = 5;
        }
    //Encontrar tercer maximo == mediana
    if (n1 > max3)
        if (n1 < max2)
        {
            max3 = n1;
            pos3 = 1;
        }
    if (n2 > max3)
        if (n2 < max2)
        {
            max3 = n2;
            pos3 = 2;
        }
    if (n3 > max3)
        if (n3 < max2)
        {
            max3 = n3;
            pos3 = 3;
        }
    if (n4 > max3)
        if (n4 < max2)
        {
            max3 = n4;
            pos3 = 4;
        }
    if (n5 > max3)
        if (n5 < max2)
        {
            max3 = n5;
            pos3 = 5;
        }
    //Salida
    printf("La mediana es %d alamacenada en  n%d.\n", max3, pos3);
}
