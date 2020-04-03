// Examen 2 Ejercicio 3
// Fecha de creacion: 19 de marzo de 2020
/************************************************************************************************************************
 * Dada una lista de calificaciones diferentes (enteros [0-100]) de tamaño n <= NMAX=100. Defina una función f_busca,
 * que identifique si existe al menos una calificación que se repita al menos una vez. Si es el caso,
 * imprima la calificación repetida de otra forma indique que no hay calificaciones repetidas.
 ************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NMAX 100

int f_busca(int lista[]);

int main()
{
    srand(time(NULL));
    int i, n, calificaciones[NMAX];
    printf("\tLista:\n\t");
    for (i = 1; i <= NMAX; i++)
    {
        calificaciones[i - 1] = rand() % 101;
        printf("%4d", calificaciones[i - 1]);
        if (i % 25 == 0)
            printf("\n\t");
    }
    n = f_busca(calificaciones);
    if (n == -1)
    {
        printf("\n\tNo hay calificaciones repetidas!\n\n");
    }
    else
    {
        printf("\n\tLa calificacion %d se repite al menos una vez.\n\n", n);
    }
    return 0;
}

int f_busca(int lista[])
{
    int i, temp, marca, freq[NMAX + 1] = {0};
    for (i = 0; i < NMAX; i++)
    {
        temp = lista[i];
        freq[temp]++;
    }
    marca = -1;
    for (i = 0; i <= NMAX; i++)
    {
        if (freq[i] > 1)
        {
            marca = i;
            i = 101;
        }
    }
    return marca;
}