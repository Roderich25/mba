/* Tarea 10 Ejercicio 3 */
/* Fecha de creacion: 18 de marzo de 2020*/
/***********************************************************************************************************************************
 * Elabore un programa para realizar operaciones con matrices cuadradas de números enteros, con las siguientes funciones f1,
 * para leer cada matriz, f2 para efectuar la suma o resta de dos matrices A y B. f3 para multiplicar un escalar r por una matriz A 
 * y f4 para imprimir las matrices leídas y la matriz resultante. f1, f2 y f3 deben llamarse desde el main(). 
 * Defina un tamaño máximo NMAX de 10, y lea el orden n <= NMAX
 * *********************************************************************************************************************************/
#include <stdio.h>
#define NMAX 10

void f1(int MAT[][NMAX], int n);
void f2(char c, int A[][NMAX], int B[][NMAX], int C[][NMAX], int n);
void f3(int A[][NMAX], int B[][NMAX], int C[][NMAX], int n);
void f4(char c, int A[][NMAX], int B[][NMAX], int C[][NMAX], int n);

int main()
{
    int n;
    char operacion;
    int A[NMAX][NMAX] = {{0}};
    int B[NMAX][NMAX] = {{0}};
    int C[NMAX][NMAX] = {{0}};

    printf("\t'Operaciones con matrices'\n\tSi desea sumar presione [s], si desea restar [r], o [m] para multiplicar por un escalar:\n\t>");
    scanf("%c", &operacion);

    if(operacion=='m'){
        printf("\nIngresar escalar:\t");
        scanf("%d", &A[0][0]);
        printf("\nIngresar tamaño de la matriz cuadrada:\t");
        scanf("%d", &n);
        f1(B, n);
        f3(A, B, C, n);
        f4(operacion, A, B, C, n);
    }else{
        printf("\nIngresar tamaño de matrices cuadradas:\t");
        scanf("%d", &n);
        f1(A, n);
        f1(B, n);
        f2(operacion, A, B, C, n);
        f4(operacion, A, B, C, n);
    }

    
    return 0;
}

void f1(int MAT[][NMAX], int n)
{
    static int matriz_n = 1;
    int i, j;
    printf("\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("\tEntero de fila %d, columna %d de la matriz %d:\t", i + 1, j + 1, matriz_n);
            scanf("%d", &MAT[i][j]);
        }
    }

    matriz_n++;
}

void f2(char c, int A[][NMAX], int B[][NMAX], int C[][NMAX], int n)
{
    int i, j;

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (c == 's')
            {
                C[i][j] = A[i][j] + B[i][j];
            }
            if (c == 'r')
            {
                C[i][j] = A[i][j] - B[i][j];
            }
        }
    }
}

void f3(int A[][NMAX], int B[][NMAX], int C[][NMAX], int n)
{
    int i, j;

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            C[i][j] = A[0][0] * B[i][j];
        }
    }
}

void f4(char c, int A[][NMAX], int B[][NMAX], int C[][NMAX], int n)
{
    int i, j;

    if (c == 'm')
    {
        //
        for (i = 0; i < n; i++)
        {
            if (i == 0)
            {
                printf("\n\t%3d\t*\t|", A[0][0]);
            }
            else
            {
                printf("\n\t   \t \t|");
            }

            for (j = 0; j < n; j++)
            {
                printf("%4d  ", B[i][j]);
            }
            printf("|\t\t");

            if (i == 0)
            {
                printf("R=|");
            }
            else
            {
                printf("  |");
            }
            for (j = 0; j < n; j++)
            {
                printf("%4d  ", C[i][j]);
            }
            printf("|");
        }
        printf("\n\n");
        //
    }
    else
    {
        for (i = 0; i < n; i++)
        {
            printf("\n\t");

            if (i == 0)
            {
                printf("A|");
            }
            else
            {
                printf(" |");
            }

            for (j = 0; j < n; j++)
            {
                printf("%4d  ", A[i][j]);
            }
            printf("|\t\t");

            if (i == 0)
            {
                printf("B|");
            }
            else
            {
                printf(" |");
            }

            for (j = 0; j < n; j++)
            {
                printf("%4d  ", B[i][j]);
            }
            printf("|\t\t");

            if (i == 0)
            {
                printf("R=|");
            }
            else
            {
                printf("  |");
            }
            for (j = 0; j < n; j++)
            {
                printf("%4d  ", C[i][j]);
            }
            printf("|");
        }
        printf("\n\n");
    }
}