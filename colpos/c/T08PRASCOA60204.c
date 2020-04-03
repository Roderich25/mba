// COA-602 Tarea 8 Ejercicio 4
// Fecha de creacion: 5-Marzo-2020
/****************************************************************************************************************************
Defina un arreglo de enteros de tamano maximo 100. Luego lea una lista de calificaciones entre 1 y 10.
Que termina con una marca de fin de datos (-1).
Guarde los datos en el arreglo creado, mientras el número de datos leídos no rebase 100,
o bien, cuando se lea la marca de fin de datos.
Luego, calcule si hay datos > 3, el promedio de calificaciones de los tres primeros mas altos.
Declare al menos una funcion.
*****************************************************************************************************************************/
#include <stdio.h>
#define SIZE 100

int ingresar_calificaciones(int calificaciones[]);

void calcular_promedio_de_3(int calificaciones[], int n);

int main(void)
{
    int suma = 0, i, n;
    int calificaciones[SIZE] = {0};
    n = ingresar_calificaciones(calificaciones);

    if (n > 3)
    {
        calcular_promedio_de_3(calificaciones, n);
    }
    else
    {
        printf("\n\tSe necesitan ingresar mas de 3 calificaciones.\n");
    }

    return 0;
}

int ingresar_calificaciones(int calificaciones[])
{
    int fin = 0, i = 0, temp;
    while (!fin)
    {
        printf("Ingresar calificacion entre 1 y 10:\t");
        scanf("%d", &temp);
        if (temp == -1)
        {
            fin = 1;
        }
        else
        {
            calificaciones[i++] = temp;
        }
        if (i >= SIZE)
            fin = 1;
    }
    return i;
}

void calcular_promedio_de_3(int calificaciones[], int n)
{
    int i, j, temp, suma3 = 0;
    for (i = 0; i < 3; i++)
    {
        for (j = n - 1; j > 0; j--)
        {
            if (calificaciones[j] > calificaciones[j - 1])
            {
                temp = calificaciones[j - 1];
                calificaciones[j - 1] = calificaciones[j];
                calificaciones[j] = temp;
            }
        }
        suma3 += calificaciones[i];
    }

    printf("El promedio de los tres mas altos es:\t%.2lf\n", suma3 / 3.0);
}