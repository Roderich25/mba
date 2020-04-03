// COA-602 Tarea 9 Ejercicio 5
// Fecha de creacion: 11-Marzo-2020
/*********************************************************************************************************************************
Generalice la estrategia para ordenar tres o cinco números enteros,
que consiste en buscar mínimos sucesivamente en una lista L1 de tamaño n= 100.
Almacene los mínimos en otra lista L2 iniciando en la posición i=0.
Cada vez que encuentre un mínimo en L1, marque cada posición, para no incluir dicho valor en la siguiente búsqueda.
Imprima L1 y L2 a doble columna.
**********************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 100

void aleatoriza_lista(int lista[]);
void imprime_listas(int lista1[], int lista2[]);
void ordena_lista(int lista1[], int lista2[]);

int main()
{
    srand(time(NULL));
    int L1[SIZE], L2[SIZE];
    aleatoriza_lista(L1);
    ordena_lista(L1, L2);
    imprime_listas(L1, L2);
    return 0;
}

void aleatoriza_lista(int lista[])
{
    int i;
    printf("\n");
    for (i = 0; i < SIZE; i++)
    {
        lista[i] = rand() % 100;
    }
}

void imprime_listas(int lista1[], int lista2[])
{
    int i;
    printf(" n\tLista 1\t\tLista 2\n");
    for (i = 0; i < SIZE; i++)
    {
        printf("%2d\t%d\t\t%d\t\n", i, lista1[i], lista2[i]);
    }
}

void ordena_lista(int lista1[], int lista2[])
{
    int i, j, minimo, pos, lista3[SIZE];

    for (i = 0; i < SIZE; i++)
        lista3[i] = lista1[i];

    for (i = 0; i < SIZE; i++)
    {
        minimo = 999;
        for (j = 0; j < SIZE; j++)
            if (lista3[j] < minimo)
            {
                minimo = lista3[j];
                pos = j;
            }
        lista3[pos] = 999;
        lista2[i] = minimo;
    }
}