// COA-602 Tarea 9 Ejercicio 4
// Fecha de creacion: 10-Marzo-2020
/*********************************************************************************************************************************
Lea una cadena de caracteres de letras y números,
identifique las frecuencias de las letras a, e, o, y el número de palabras en la cadena.
Imprima el histograma de frecuencias y el número de palabras.
**********************************************************************************************************************************/
#include <stdio.h>

int main(void)
{
    int i, j, marca = 1;
    char cadena[1000] = {};
    char letra[4] = {' ', 'a', 'e', 'o'};
    int conteo[4] = {0};

    printf("Introducir una cadena de caracteres de maximo 1000 carcateres:\n>");
    scanf("%[^\n]", cadena);
    i = 0;
    while (cadena[i] != '\0')
    {
        for (j = 0; j < 4; j++)
            if (cadena[i] == letra[j])
                conteo[j]++;
        i++;
    }

    if (i == conteo[0]++)
        marca = -1;

    if (marca != -1)
    {
        printf("\n\tTotal de palabras:\t%d\n", conteo[0]);
        printf("\n\tHistograma\n");
        for (i = 1; i < 4; i++)
        {
            printf("\t'%c' %3d: ", letra[i], conteo[i]);
            for (j = 1; j <= conteo[i]; j++)
                printf("*");
            printf("\n");
        }
        printf("\n");
    }
    else
    {
        printf("\tNO se ingreso una cadena valida.\n");
    }
    return 0;
}