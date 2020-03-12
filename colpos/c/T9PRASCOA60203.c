// COA-602 Tarea 9 Ejercicio 3
// Fecha de creacion: 10-Marzo-2020
/*********************************************************************************************************************************
Lea una lista de salarios entre 5000 y 20000 de tamaño n < 30.
Luego, clasifique la lista en tres estratos. 5000-10000, 10000-15000 y 15000-20000. Defina intervalos abiertos por la derecha.
Para cada estrato, realice un conteo de salarios en cada estrato. Grafique un histograma con frecuencias relativas.
Calcule las medias por estrato. Elabore una función f1, para leer la dimensión de la lista;
una función f2 para leer los elementos de la lista; una función f3, para clasificar, y una función f4 para imprimir los resultados.
Las funciones debe llamarse del el main().
**********************************************************************************************************************************/
#include <stdio.h>

int f1(void);
void f2(int n, int lista[]);
void f3(int n, int lista[], int resultados[]);
void f4(int n, int resultados[]);

int main()
{
    int n = f1();
    int salarios[n];
    int resultados[3] = {0};
    f2(n, salarios);
    f3(n, salarios, resultados);
    f4(n, resultados);
    return 0;
}

int f1(void)
{
    int n, fin;
    fin = 0;
    while (!fin)
    {
        printf("Ingresar tamaño de lista de salarios:\t");
        scanf("%d", &n);
        if (n > 0)
            if (n < 30)
            {
                fin = 1;
                break;
            }
        printf("Tamaño invalido. Intente de nuevo.\n");
    }
    return n;
}

void f2(int n, int lista[])
{
    int i, temp;
    for (i = 0; i < n; i++)
    {
        printf("\tIngresar salario %2d:\t", i + 1);
        scanf("%d", &temp);
        lista[i] = temp;
    }
}

void f3(int n, int lista[], int resultados[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (lista[i] >= 5000)
            if (lista[i] < 10000)
                resultados[0]++;
        if (lista[i] >= 10000)
            if (lista[i] < 15000)
                resultados[1]++;
        if (lista[i] >= 15000)
            if (lista[i] < 20000)
                resultados[2]++;
    }
}

void f4(int n, int resultados[])
{
    int i, j;
    printf("\n");
    for (i = 0; i < 3; i++)
    {
        switch (i)
        {
        case 0:
            printf(" [5000-10000)");
            break;
        case 1:
            printf("[10000-15000)");
            break;
        case 2:
            printf("[15000-20000)");
            break;
        default:
            break;
        }
        printf("%3d:\t", resultados[i]);
        for (j = 1; j <= resultados[i]; j++)
            printf("*");
        printf("\n");
    }
    printf("\n");
}