// COA-602 Tarea 11 Ejercicio 3
// Fecha de creacion: 01-April-2020
/*************************************************************************************************************
* Cree un programa para generar las matrices X, Y, XT, XTX, XTY del problema de regresión lineal e imprímalas.
* Utilice funciones. Lea n, p, vars, y los n pares de datos x,y. para n>=3 y n <=20.
**************************************************************************************************************/
#include <stdio.h>
#define NMAX 20

int ingresar_datos(double datos[][2]);
void genera_X(double datos[][2], double X[][2], int n);
void genera_Y(double datos[][2], double Y[], int n);
void genera_XT(double X[][2], double XT[][NMAX], int n);
void imprime_XTX(double XT[][NMAX], double X[][2], int n);
void imprime_XTY(double XT[][NMAX], double Y[], int n);

int main()
{
    double datos[NMAX][2] = {0.0};
    double X[NMAX][2] = {0.0};
    double XT[2][NMAX] = {0.0};
    double Y[NMAX] = {0.0};

    int n = ingresar_datos(datos);
    genera_X(datos, X, n);
    genera_Y(datos, Y, n);
    genera_XT(X, XT, n);
    imprime_XTX(XT, X, n);
    imprime_XTY(XT, Y, n);
    return 0;
}

int ingresar_datos(double datos[][2])
{
    int i, n;
    double x, y;
    do
    {
        printf("Ingresar tamaño de n, entre 3 y 20:\t");
        scanf("%d", &n);
    } while (n<3 | n> 20);
    for (i = 0; i < n; i++)
    {
        printf("Ingresar par de datos #%d, ( x, y ):\t", i + 1);
        scanf("%lf %lf", &x, &y);
        datos[i][0] = x;
        datos[i][1] = y;
    }
    return n;
}

void genera_X(double datos[][2], double X[][2], int n)
{
    int i;
    printf("\nMatriz X:\n");
    for (i = 0; i < n; i++)
    {
        X[i][0] = 1;
        X[i][1] = datos[i][0];
        printf("\t|%6.2lf %6.2lf|\n", X[i][0], X[i][1]);
    }
}

void genera_Y(double datos[][2], double Y[], int n)
{
    int i;
    printf("\nVector Y:\n");
    for (i = 0; i < n; i++)
    {
        Y[i] = datos[i][1];
        printf("\t|%6.2lf|\n", Y[i]);
    }
}

void genera_XT(double X[][2], double XT[][NMAX], int n)
{
    int i, j;
    printf("\nMatriz XT:\n");
    for (i = 0; i < 2; i++)
    {
        printf("\t|");
        for (j = 0; j < n; j++)
        {
            XT[i][j] = X[j][i];
            printf("%6.2lf", XT[i][j]);
        }
        printf("|\n");
    }
}

void imprime_XTX(double XT[][NMAX], double X[][2], int n)
{
    int i, j, k;
    double XTX[2][2] = {0.0};

    for (i = 0; i < 2; i++)
        for (k = 0; k < n; k++)
            for (j = 0; j < 2; j++)
                XTX[i][j] += XT[i][k] * X[k][j];

    printf("\nMatriz A=XTX:\n");
    for (i = 0; i < 2; i++)
    {
        printf("\t|");
        for (j = 0; j < 2; j++)
            printf("%6.2lf", XTX[i][j]);
        printf("|\n");
    }
}

void imprime_XTY(double XT[][NMAX], double Y[], int n)
{
    int i, j, k;
    double XTY[2] = {0.0};

    for (i = 0; i < 2; i++)
        for (k = 0; k < n; k++)
            for (j = 0; j < 1; j++)
                XTY[i] += XT[i][k] * Y[k];

    printf("\nMatriz C=XTY:\n");
    for (i = 0; i < 2; i++)
        printf("\t|%6.2lf|\n", XTY[i]);
}