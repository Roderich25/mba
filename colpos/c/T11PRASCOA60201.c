// COA-602 Tarea 11 Ejercicio 1
// Fecha de creacion: 01-April-2020
/********************************************************************************************************
* Dada una matriz A de números enteros de tamaño m(hileras) x n(columnas); 6<= m,n<=12;
* Identifique si la suma de los máximos de hileras pares es mayor a la suma de máximos de columnas nones.
*********************************************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#define M 6
#define N 12

int maximo(const int arreglo[], int n);
void lee_dimension(int *ptrN, int *ptrM);
void genera_matriz(int matriz[][N], int m, int n);
void max_hil_col(const int matriz[][N], int m, int n);
void imprime_matriz(int matriz[][N], int m, int n);

int main()
{
    int n, m;
    int matriz[M][N] = {0};
    lee_dimension(&n, &m);
    genera_matriz(matriz, m, n);
    imprime_matriz(matriz, m, n);
    max_hil_col(matriz, m, n);

    return 0;
}

void lee_dimension(int *ptrN, int *ptrM)
{
    do
    {
        printf("Ingresar dimensión de hileras, entre  1 y 6:\t");
        scanf("%d", ptrM);
    } while (*ptrM<1 | *ptrM> 6);

    do
    {
        printf("Ingresar dimensión de columnas, entre  1 y 12:\t");
        scanf("%d", ptrN);
    } while (*ptrN<1 | *ptrN> 12);
}

int maximo(const int arreglo[], int n)
{
    int i, max;
    max = 0;
    for (i = 0; i < n; i++)
        if (arreglo[i] > max)
            max = arreglo[i];
    return max;
}

void genera_matriz(int matriz[][N], int m, int n)
{
    int i, j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            matriz[i][j] = rand() % 100;
        }
    }
}

void max_hil_col(const int matriz[][N], int m, int n)
{
    int i, j, hileras, columnas;
    int transpuesta[n][m];

    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            transpuesta[j][i] = matriz[i][j];

    hileras = 0;
    for (i = 0; i < m; i++)
        if ((i + 1) % 2 == 0)
            hileras += maximo(matriz[i], n);

    columnas = 0;
    for (j = 0; j < n; j++)
        if ((j + 1) % 2 == 1)
            columnas += maximo(transpuesta[j], m);

    printf("\n\tLa suma de máximos de hileras pares es: %5d\n\tLa suma de máximos de columnas nones es: %5d\n", hileras, columnas);
    if (hileras == columnas)
    {
        printf("\tPor lo tanto, las sumas son iguales.\n");
    }
    else
    {
        if (hileras > columnas)
        {
            printf("\tPor lo tanto, la suma de máximos de hileras pares es mayor.\n");
        }
        else
        {
            printf("\tPor lo tanto, la suma de máximos de columnas nones es mayor.\n\n");
        }
    }
}

void imprime_matriz(int matriz[][N], int m, int n)
{
    int i, j;
    printf("\n\tLa matriz aleatoria de %dx%d es:\n", m, n);
    for (i = 0; i < m; i++)
    {
        printf("\t\t|");
        for (j = 0; j < n; j++)
        {
            printf("%4d", matriz[i][j]);
        }
        printf("|\n");
    }
}