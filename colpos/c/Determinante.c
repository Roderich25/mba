#include <stdio.h>
#define NMAX 4

void muestra_matriz(int mat[][NMAX], int m);
int cofactor_matriz(int mat[][NMAX], int m);
void matriz_reducida(int mat[][NMAX], int temp[][NMAX], int m);
int det2x2(int mat[][NMAX]);
int determinante(int mat[][NMAX], int n);

int main()
{
    int mat[NMAX][NMAX] = {2, 4, 1, -3, 7, 2, 2, -2, 3, 3, 2, 2, 0, 5, 1, 0};
    muestra_matriz(mat, NMAX);
    printf("\nDeterminante: %3d\n", determinante(mat, NMAX));
    return 0;
}

int cofactor_matriz(int mat[][NMAX], int m)
{
    return mat[m][0];
}

void matriz_reducida(int mat[][NMAX], int temp[][NMAX], int m)
{
    int i, j, k = 0;
    int local[NMAX][NMAX] = {0};

    for (i = 0; i < NMAX; i++)
    {
        if (i == m)
            k++;
        for (j = 1; j < NMAX; j++)
        {
            if (k < NMAX)
            {
                local[i][j - 1] = mat[k][j];
            }
        }
        k++;
    }
    for (i = 0; i < NMAX; i++)
    {
        for (j = 0; j < NMAX; j++)
        {
            temp[i][j] = local[i][j];
        }
    }
}

int det2x2(int mat[][NMAX])
{
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0]);
}

void muestra_matriz(int mat[][NMAX], int m)
{
    int i, j;
    for (i = 0; i < m; i++)
    {
        printf("|");
        for (j = 0; j < m; j++)
        {
            printf("%3d", mat[i][j]);
        }
        printf("|\n");
    }
}

int determinante(int mat[][NMAX], int n)
{
    int i, signo, det;
    int temp[NMAX][NMAX] = {0};
    if (n == 2)
    {
        return det2x2(mat);
    }
    else
    {
        signo = -1;
        det = 0;
        for (i = 0; i < n; i++)
        {
            signo *= -1;
            matriz_reducida(mat, temp, i);
            det += signo * cofactor_matriz(mat, i) * determinante(temp, n - 1);
        }
        return det;
    }
}