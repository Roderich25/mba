/* Tarea 10 Ejercicio 1 */
/* Fecha de creacion: 18 de marzo de 2020*/
/***********************************************************************************************************
 * Modifique el programa que ordena un conjunto de números enteros, para que ordene un conjunto de palabras
 * escritas en minúsculas con caracteres del alfabeto inglés.
 * Para que ordene de mayor a menor e imprima a doble columna la lista original y la lista ordenada.
 * Utilice funciones f1, para leer la lista de tamaño n. f2, para ordenar la lista L1 de palabras en una
 * nueva lista L2, y f3, para imprimir las listas L1 y L2 a doble columna.
 * *********************************************************************************************************/
#include <stdio.h>
#define SIZE 100

void f1(char palabras[][SIZE], int n);
void f2(char palabras[][SIZE], char ordenadas[][SIZE], int n);
void f3(char palabras[][SIZE], char ordenadas[][SIZE], int n);
int mayor_en_lista(char palabras[][SIZE], int n);

int main()
{
    int n;
    printf("Ingresar tamaño de la lista:\t");
    scanf("%d", &n);
    char L1[n][SIZE];
    char L2[n][SIZE];
    f1(L1, n);
    f2(L1, L2, n);
    f3(L1, L2, n);

    return 0;
}

void f1(char palabras[][SIZE], int n)
{
    int i, j;
    for (i = 0; i < n; i++)
    {
        while ((getchar()) != '\n')
            ;
        printf("Palabra %d:\t", i + 1);
        scanf("%[^\n]", palabras[i]);
    }
}

void f2(char palabras[][SIZE], char ordenadas[][SIZE], int n)
{
    int i, j, m;
    char temporal[n][SIZE];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < SIZE; j++)
        {
            temporal[i][j] = palabras[i][j];
        }
    }

    for (i = 0; i < n; i++)
    {
        m = mayor_en_lista(temporal, n);

        for (j = 0; j < SIZE; j++)
        {
            ordenadas[i][j] = temporal[m][j];
            temporal[m][j] = ' ';
        }
    }
}

void f3(char palabras[][SIZE], char ordenadas[][SIZE], int n)
{
    int i, j;
    printf("\n\t  n\tL1\t\tL2\n");
    for (i = 0; i < n; i++)
    {
        printf("\t%3d\t", i + 1);
        j = 0;
        while (palabras[i][j] != '\0')
        {
            printf("%c", palabras[i][j]);
            j++;
        }
        printf("\t\t");
        j = 0;
        while (ordenadas[i][j] != '\0')
        {
            printf("%c", ordenadas[i][j]);
            j++;
        }
        printf("\n");
    }
}

int mayor_en_lista(char palabras[][SIZE], int n)
{
    int i, j, mayor = 0;
    for (i = 1; i < n; i++)
    {
        int marca = -1;
        for (j = 0; j < 100; j++)
        {
            if (palabras[mayor][j] == palabras[i][j])
            {
                marca = -1;
            }
            else
            {
                if ((int)palabras[mayor][j] > (int)palabras[i][j])
                {
                    mayor = mayor;
                    marca = 1;
                }
                else
                {
                    mayor = i;
                    marca = 1;
                }
            }
            if (marca != -1)
                j = 100;
        }
    }
    return mayor;
}