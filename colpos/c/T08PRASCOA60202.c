// COA-602 Tarea 8 Ejercicio 2
// Fecha de creacion: 5-Marzo-2020
/****************************************************************************************************************************
Genere una lista de tamaño n, de numeros enteros en el rango 1-20, en forma aleatoria n<=100.
Luego, cuente las frecuencias de numeros pares y números nones.
Luego, imprima el histograma de las frecuencias, declare al menos una función.
*****************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 20

int genera_aleatorio(int max);

int main(void)
{
    srand(time(NULL));

    int i, j, n, pos;
    int frec[SIZE + 1] = {0};
    n = genera_aleatorio(100);

    for (i = 1; i <= n; i++)
    {
        pos = genera_aleatorio(SIZE);
        frec[pos]++;
    }

    printf("\nTotal de numeros aleatorios generados:\t%d\n\n", n);

    printf("%s%13s%17s\n", "Elemento", "Frecuencia", "Histograma");
    for (i = 1; i <= SIZE; i++)
    {
        printf("%7d%13d        ", i, frec[i]);

        for (j = 1; j <= frec[i]; j++)
        {
            printf("%c", '*');
        }
        printf("\n");
    }

    return 0;
}

int genera_aleatorio(int max)
{
    return rand() % max + 1;
}