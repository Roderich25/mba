// COA-602 Tarea 9 Ejercicio 5
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 10-Marzo-2020
/*********************************************************************************************************************************
Generalice la estrategia para ordenar tres o cinco números enteros,
que consiste en buscar mínimos sucesivamente en una lista L1 de tamaño n= 100.
Almacene los mínimos en otra lista L2 iniciando en la posición i=0.
Cada vez que encuentre un mínimo en L1, marque cada posición, para no incluir dicho valor en la siguiente búsqueda.
Imprima L1 y L2 a doble columna.
**********************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 100

void aleatoriza_lista(int lista[]);
void imprime_lista(int lista[]);

int main()
{
    int L1[SIZE] = {0}, L2[SIZE] = {0};
    printf("Hello\n");
    aleatoriza_lista(L1);
    imprime_lista(L1);
    imprime_lista(L2);
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

void imprime_lista(int lista[])
{
    int i;
    printf("\nLista:\t");
    for (i = 0; i < SIZE; i++)
    {
        printf("%4d", lista[i]);
    }
    printf("\n");
}