// COA-602 Tarea 9 Ejercicio 2
// Fecha de creacion: 10-Marzo-2020
/*********************************************************************************************************************************
Genere una lista de enteros de tamaño n<20. Los números pueden estar repetidos más de una vez y en desorden.
Lea un valor x, e identifique si x existe en la lista. Imprima si x está y el índice de la posición que ocupa en la lista.
Si existe más de una vez, imprima las diferentes posiciones donde ocurre.
**********************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int tamano_lista(void);
void genera_lista(int n, int lista[]);
void busqueda(int x, int n, int lista[]);
void imprime_lista(int n, int lista[]);

int main(void)
{
    srand(time(NULL));

    int n, x;
    n = tamano_lista();
    printf("\n\tTamaño de lista:\t%d\n\n", n);

    int lista[n];
    genera_lista(n, lista);

    printf("\tIntroducir entero a buscar en lista:\t");
    scanf("%d", &x);

    busqueda(x, n, lista);
    imprime_lista(n, lista);
    return 0;
}

int tamano_lista(void)
{
    return rand() % 19 + 1;
}

void genera_lista(int n, int lista[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        lista[i] = rand() % 9 + 1;
    }
}

void busqueda(int x, int n, int lista[])
{
    int i, contador;
    printf("\n\tBusqueda de:\t%d\n", x);
    contador = 0;
    for (i = 0; i < n; i++)
    {
        if (lista[i] == x)
        {
            printf("\t\t\"%d\" encontrado en la posicion %d.\n", x, i);
            contador++;
        }
    }
    if (contador == 0)
    {
        printf("\t\tNO se encontro \"%d\".\n", x);
    }
}

void imprime_lista(int n, int lista[])
{
    int i;
    printf("\n\tLista:\t");
    for (i = 0; i < n; i++)
    {
        printf("%2d", lista[i]);
    }
    printf("\n\n");
}