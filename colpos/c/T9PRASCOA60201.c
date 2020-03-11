// COA-602 Tarea 9 Ejercicio 1
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 10-Marzo-2020
/*********************************************************************************************************************************
Genere una lista de números enteros de tamaño n, en forma aleatoria, n<=1000. Los números pueden variar entre 0 y 50 pueden estar 
repetidos más de una vez, en forma contigua. Ordene la lista de mayor a menor.
Dado un número x, identifique si existe en la lista; si existe indique si es único o está repetido;
si está repetido indique cuántas veces y la posición del último valor repetido.
Compare los métodos de búsqueda lineal y búsqueda binaria en términos del número de operaciones para identificar x
**********************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int tamano_lista(void);
void genera_lista(int n, int lista[]);
void ordena_lista(int n, int lista[]);
void busqueda_lineal(int x, int n, int lista[]);
void busqueda_binaria(int x, int n, int lista[]);
void imprime_lista(int n, int lista[]);

int main(void)
{
    srand(time(NULL));

    int i, n, x;
    n = tamano_lista();
    printf("\n\tTamaño de lista:\t%d\n", n);

    int lista[n];
    genera_lista(n, lista);
    ordena_lista(n, lista);

    printf("\tIntroducir entero a buscar en lista:\t");
    scanf("%d", &x);

    busqueda_lineal(x, n, lista);
    busqueda_binaria(x, n, lista);
    imprime_lista(n, lista);
    return 0;
}

int tamano_lista(void)
{
    return rand() % 1000 + 1;
}

void genera_lista(int n, int lista[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        lista[i] = rand() % 50 + 1;
    }
}

void ordena_lista(int n, int lista[])
{
    int i, j, menor, temp;
    for (j = 0; j < n - 1; j++)
    {
        for (i = 0; i < n - 1; i++)
        {
            menor = lista[i];
            if (lista[i + 1] > lista[i])
            {
                temp = lista[i + 1];
                lista[i + 1] = lista[i];
                lista[i] = temp;
            }
        }
    }
}

void imprime_lista(int n, int lista[])
{
    int i;
    printf("\n\n\tLista:\t");
    for (i = 0; i < n; i++)
    {
        printf("%3d", lista[i]);
    }
    printf("\n\n");
}

void busqueda_lineal(int x, int n, int lista[])
{
    int i, contador;
    printf("\n\tBusqueda lineal de:\t%d\n", x);
    i = 0;
    contador = 0;
    while (lista[i] >= x)
    {
        if (lista[i] == x)
            contador++;
        i++;
        if (i >= n)
            break;
    }
    if (contador > 0)
    {
        printf("\t\tDespues de %3d iteraciones se encontro \"%d\" un total de %d veces, la posicion del ultimo valor de \"%d\" es %d.\n", i + 1, x, contador, x, i - 1);
    }
    else
    {
        printf("\t\tDespues de %3d iteraciones NO se encontro %d.\n", i + 1, x);
    }
}

void busqueda_binaria(int x, int n, int lista[])
{
    int i, repetidos, izq, der, centro, encontrado, contador;
    printf("\n\tBusqueda binaria de:\t%d\n", x);
    contador = 1;
    encontrado = -1;
    izq = -1;
    der = n;
    while (der - izq > 1)
    {
        centro = (izq + der) / 2;
        if (lista[centro] == x)
        {
            encontrado = centro;
            break;
        }
        else
        {
            if (lista[centro] > x)
            {
                izq = centro;
            }
            else
            {
                der = centro;
            }
        }
        contador++;
    }

    if (encontrado != -1)
    {
        repetidos = 1;
        i = 1;
        while (encontrado - i >= 0)
        {
            if (lista[encontrado - i] == x)
            {
                repetidos++;
                i++;
            }
            else
            {
                break;
            }
        }
        i = 1;
        while (encontrado + i < n)
        {
            if (lista[encontrado + i] == x)
            {
                repetidos++;
                i++;
            }
            else
            {
                break;
            }
        }
    }

    if (encontrado != -1)
    {
        printf("\t\tDespues de %3d iteraciones se encontro \"%d\" un total de %d veces, la posicion del ultimo valor de \"%d\" es %d.\n", contador, x, repetidos, x, encontrado + i - 1);
    }
    else
    {
        printf("\t\tDespues de %3d iteraciones NO se encontro %d.\n", contador, x);
    }
}