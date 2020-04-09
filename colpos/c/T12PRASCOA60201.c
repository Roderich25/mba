// COA-602 Tarea 12 Ejercicio 1
// Fecha de creacion: 08-April-2020
/*************************************************************************************************************
* Elabore un programa para estimar los parámetros de un modelo de regresión lineal simple.
*    i) Lea el número de observaciones nobs (menor o igual a 100). Luego, lea los pares de valores x,y.
*   ii) Utilice las funciones elaboradas en el problema 3 de T11.
*  iii) Construya el sistema lineal A X = C. donde A (XTX) es una matriz cuadrada simétrica de orden pxp (2x2);
        X es un vector de dimensión px2; esto es 2x1; y C (XTY)es un vector de orden 2x1.
*   iv) Resuelva el sistema lineal A X = C, utilizando una solución algebraica (por igualación, sustitución etc)
        para conocer los valores del vector X. Consultar en internet cualquier método algebraico para resolver
        un sistema de dos ecuaciones lineales con 2 incógnitas
*    v) Imprima los datos leídos, las matrices X, XT, XTX=A, XTY = C, y el vector solución.
*   vi) Obtenga un conjunto de datos de cualquier libro de estadística o de internet. Indique la fuente.
*  vii) En el main, únicamente deben estar los llamados a funciones y declaraciones de variables.
* viii) Defina tamaños máximos Maxhileras y Maxcolumnas de matrices y vectores.

**************************************************************************************************************/
#include <stdio.h>
#define MAXHIL 100
#define MAXCOL 2

int ingresar_datos(double datos[][MAXCOL]);
void genera_X(double datos[][MAXCOL], double X[][MAXCOL], int n);
void genera_Y(double datos[][MAXCOL], double Y[], int n);
void genera_XT(double X[][MAXCOL], double XT[][MAXHIL], int n);
void genera_XTX(double XTX[][MAXCOL], double XT[][MAXHIL], double X[][MAXCOL], int n);
void genera_XTY(double XTY[], double XT[][MAXHIL], double Y[], int n);
void genera_solucion(double Beta[], double XTX[][MAXCOL], double XTY[]);

int main()
{
    double datos[MAXHIL][MAXCOL] = {0.0};
    double X[MAXHIL][MAXCOL] = {0.0};
    double XT[MAXCOL][MAXHIL] = {0.0};
    double Y[MAXHIL] = {0.0};
    double XTX[MAXCOL][MAXCOL] = {0.0};
    double XTY[MAXCOL] = {0.0};
    double Beta[MAXCOL] = {0.0};
    /* COMPROBACIÓN DEL PROGRAMA
    * https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/cars.html
    * Si tomamos las primeras 10 observaciones del conjunto de datos "cars"
    *  x (speed)    y (dist)
    *   4             2
    *   4            10
    *   7             4
    *   7            22
    *   8            16
    *   9            10
    *  10            18
    *  10            26
    *  10            34
    *  11            17
    * en R corremos el siguiente comando
    * >lm(dist~speed, data=cars[1:10,])
    * con los siguientes resultados:
    * 
    * Coefficients:
    * (Intercept)        speed  
    *      -4.529        2.554
    * 
    * que comparados por los obtenidos con este programa son:
    *  B_0: -4.53
    *  B_1:  2.55
    * por lo tanto, son aproximadamente iguales. 
    */
    int n = ingresar_datos(datos);
    genera_X(datos, X, n);
    genera_Y(datos, Y, n);
    genera_XT(X, XT, n);
    genera_XTX(XTX, XT, X, n);
    genera_XTY(XTY, XT, Y, n);
    genera_solucion(Beta, XTX, XTY);

    return 0;
}

int ingresar_datos(double datos[][MAXCOL])
{
    int i, n;
    double x, y;
    do
    {
        printf("Ingresar tamaño de n, positivo menor o igual a 100:\t");
        scanf("%d", &n);
    } while (n<1 | n> 100);
    for (i = 0; i < n; i++)
    {
        printf("Ingresar par de datos #%d, ( x, y ) separados por un espacio:\t", i + 1);
        scanf("%lf %lf", &x, &y);
        datos[i][0] = x;
        datos[i][1] = y;
    }

    printf("\nDatos:\n\t%5c\t%5c\n", 'x', 'y');
    for (i = 0; i < n; i++)
        printf("\t%5.2lf\t%5.2lf\n", datos[i][0], datos[i][0]);
    return n;
}

void genera_X(double datos[][MAXCOL], double X[][MAXCOL], int n)
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

void genera_Y(double datos[][MAXCOL], double Y[], int n)
{
    int i;
    printf("\nVector Y:\n");
    for (i = 0; i < n; i++)
    {
        Y[i] = datos[i][1];
        printf("\t|%6.2lf|\n", Y[i]);
    }
}

void genera_XT(double X[][MAXCOL], double XT[][MAXHIL], int n)
{
    int i, j;
    printf("\nMatriz XT:\n");
    for (i = 0; i < MAXCOL; i++)
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

void genera_XTX(double XTX[][MAXCOL], double XT[][MAXHIL], double X[][MAXCOL], int n)
{
    int i, j, k;

    for (i = 0; i < MAXCOL; i++)
        for (k = 0; k < n; k++)
            for (j = 0; j < MAXCOL; j++)
                XTX[i][j] += XT[i][k] * X[k][j];

    printf("\nMatriz A=XTX:\n");
    for (i = 0; i < MAXCOL; i++)
    {
        printf("\t|");
        for (j = 0; j < MAXCOL; j++)
            printf("%6.2lf", XTX[i][j]);
        printf("|\n");
    }
}

void genera_XTY(double XTY[], double XT[][MAXHIL], double Y[], int n)
{
    int i, j, k;

    for (i = 0; i < MAXCOL; i++)
        for (k = 0; k < n; k++)
            for (j = 0; j < 1; j++)
                XTY[i] += XT[i][k] * Y[k];

    printf("\nMatriz C=XTY:\n");
    for (i = 0; i < MAXCOL; i++)
        printf("\t|%6.2lf|\n", XTY[i]);
}

void genera_solucion(double Beta[], double XTX[][MAXCOL], double XTY[])
{
    Beta[1] = (XTY[1] - ((XTX[1][0] * XTY[0]) / XTX[0][0])) / (XTX[1][1] - ((XTX[1][0] * XTX[0][1]) / XTX[0][0]));
    Beta[0] = (XTY[0] / XTX[0][0]) - (XTX[0][1] / XTX[0][0]) * Beta[1];

    printf("Solución:\n\t| B_0: %5.2lf |\n\t| B_1: %5.2lf |\n", Beta[0], Beta[1]);
}