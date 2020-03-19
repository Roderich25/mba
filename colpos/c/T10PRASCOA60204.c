/* Tarea 10 Ejercicio 4 */
/* Fecha de creacion: 18 de marzo de 2020*/
/******************************************************************************************************************************
 * Genere dos listas de números enteros L1 y L2 de tamaño n <= NMAX=100. L1 tendrá valores aleatorios entre 1 y 5, 
 * L2 tendrá valores aleatorios entre 0 y 100. 
 * Luego, defina una función f1 para ordenar las dos listas utilizando como clave los valores de L1. 
 * Luego, defina una función f2 para obtener los promedios de L2, por cada valor de L1. 
 * Finalmente, defina una función f3 para imprimir los promedios para cada valor diferente de L1 calculados en f2.
 * ****************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NMAX 100

void f1(int L1[], int L2[]);
void f2(int L1[], int L2[], double L3[]);
void f3(int L1[], int L2[], double L3[]);

int main()
{
    srand(time(NULL));
    int i;
    int L1[NMAX] = {0}, L2[NMAX] = {0};
    double L3[5] = {0};

    printf("\tListas:");
    for (i = 0; i < NMAX; i++)
    {
        L1[i] = rand() % 5 + 1;
        L2[i] = rand() % 101;
    }
    f1(L1, L2);
    f2(L1, L2, L3);
    f3(L1, L2, L3);
    return 0;
}

void f1(int L1[], int L2[])
{
    int mat[5][NMAX] = {-1};
    int ind[5] = {0};
    int temp, i, j, k;
    for (k = 0; k < NMAX; k++)
    {
        switch (L1[k])
        {
        case 1:
            mat[0][ind[0]] = L2[k];
            ind[0]++;
            break;
        case 2:
            mat[1][ind[1]] = L2[k];
            ind[1]++;
            break;
        case 3:
            mat[2][ind[2]] = L2[k];
            ind[2]++;
            break;
        case 4:
            mat[3][ind[3]] = L2[k];
            ind[3]++;
            break;
        case 5:
            mat[4][ind[4]] = L2[k];
            ind[4]++;
            break;
        default:
            printf("\t\"Invalid number!!!\"\n");
            break;
        }
    }

    for (i = 0; i < 5; i++)
    {
        j = 0;
        while (j < ind[i] - 1)
        {
            for (k = 0; k < ind[i] - 1; k++)
            {
                if (mat[i][k + 1] < mat[i][k])
                {
                    temp = mat[i][k];
                    mat[i][k] = mat[i][k + 1];
                    mat[i][k + 1] = temp;
                }
            }
            j++;
        }
    }

    k = 0;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < ind[i]; j++)
        {
            L1[k] = i + 1;
            L2[k] = mat[i][j];
            k++;
        }
    }
}

void f2(int L1[], int L2[], double L3[])
{
    int i;
    int L4[5] = {0};
    for (i = 0; i < NMAX; i++)
    {
        L3[L1[i] - 1] += L2[i];
        L4[L1[i] - 1] += 1;
    }

    for (i = 0; i < 5; i++)
    {
        if (L4[i] != 0)
        {
            L3[i] = (double)L3[i] / L4[i];
        }
        else
        {
            L3[i] = 0.0;
        }
    }
}

void f3(int L1[], int L2[], double L3[])
{
    int i, j;
    printf("\n");
    for (i = 0; i < 5; i++)
    {
        printf("\t%d|", i + 1);
        for (j = 0; j < NMAX; j++)
        {
            if (L1[j] - 1 == i)
            {
                printf("%4d", L2[j]);
            }
        }
        printf("\n");
    }
    printf("\n\tPromedios:\n");
    for (i = 0; i < 5; i++)
    {
        printf("\t%d =>  %5.2lf\n", i + 1, L3[i]);
    }
}