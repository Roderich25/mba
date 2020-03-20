// Examen 2 Ejercicio 1
// Fecha de creacion: 19 de marzo de 2020
/************************************************************************************************************************
 * Genere en forma sistemática dos listas de arreglos unidimensionales L1, L2 de tamaño n <=NMAX= 50.
 * (Lea con una función f1 el valor de n). Considere los siguientes criterios, la lista L1 tendrá valores tres veces
 * el valor de su posición más 10. y L2 tendrá para cada posición, valores binarios, 0 si su índice es par y 
 * 1 si su índice es non. Imprimir a doble columna las listas generadas, mediante una función f2. 
 ************************************************************************************************************************/
#include <stdio.h>

int f1(void);
void llena_listas(int L1[], int L2[], int n);
void f2(int L1[], int L2[], int n);

int main()
{
    int n;
    n = f1();
    int L1[n], L2[n];
    llena_listas(L1, L2, n);
    f2(L1, L2, n);

    return 0;
}

int f1(void)
{
    int n = -1;
    while (n == -1)
    {
        printf("Ingresar tamaño de lista de tamaño maximo 50:\t");
        scanf("%d", &n);
        if (n > 50)
            n = -1;
        if (n <= 0)
            n = -1;
    }
    return n;
}

void llena_listas(int L1[], int L2[], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        L1[i] = i * 3 + 10;
        if (i % 2 == 0)
        {
            L2[i] = 0;
        }
        else
        {
            L2[i] = 1;
        }
    }
}

void f2(int L1[], int L2[], int n)
{
    int i;
    printf("\t i\t|\t L1\t|\tL2\n");
    for (i = 0; i < n; i++)
    {
        printf("\t%2d\t|\t%3d\t|\t%2d\n", i, L1[i], L2[i]);
    }
    printf("\n");
}