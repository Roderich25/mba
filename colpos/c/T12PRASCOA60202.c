// COA-602 Tarea 12 Ejercicio 2
// Fecha de creacion: 08-April-2020
/***********************************************************************************************
* Declare una cadena que contenga caracteres de letras y números,
* identifique las frecuencias de las letras a, e, i, o y u y el número de palabras en la cadena;
* Imprima el histograma de frecuencias y el número de palabras. 
* Utilice funciones con índice de arreglos para recorrer la cadena. 
* Luego, implemente otra función para recorrer la cadena con apuntadores.
*************************************************************************************************/
#include <stdio.h>

void historgrama_indices(char cadena[], int n);
void histograma_apuntadores(char *ptrCadena);
void llena_frecuencias(char c, int arreglo[]);

int main()
{
    char cadena[] = "Lorem ipsum dolor sit amet, libris graeco duo no, est mucius eruditi appellantur ex. Quo nisl senserit volutpat ei.";

    historgrama_indices(cadena, sizeof(cadena) / sizeof(char));
    histograma_apuntadores(cadena);

    return 0;
}

void historgrama_indices(char cadena[], int n)
{
    int frecuencia[6] = {0};
    char vocales[] = {'a', 'e', 'i', 'o', 'u', ' '};
    int i, j, k;

    for (k = 0; k < n; k++)
        llena_frecuencias(cadena[k], frecuencia);

    printf("\n\n\tHISTOGRAMA recorriendo \"cadena\" con indices:\n");
    for (i = 0; i < 5; i++)
    {
        printf("\tVocal \"%c\": #%3d\t", vocales[i], frecuencia[i]);
        for (j = 0; j < frecuencia[i]; j++)
            printf("*");
        printf("\n");
    }
    printf("\tNúmero de palabras:\t%d\n\n", frecuencia[5] + 1);
}
void histograma_apuntadores(char *ptrCadena)
{
    int frecuencia[6] = {0};
    char vocales[] = {'a', 'e', 'i', 'o', 'u', ' '};
    int i, j, n;

    while (*ptrCadena != '\0')
    {
        llena_frecuencias(*ptrCadena, frecuencia);
        ptrCadena++;
    }

    n = sizeof(vocales) / sizeof(char);
    printf("\n\n\tHISTOGRAMA recorriendo \"cadena\" con apuntador:\n");
    for (i = 0; i < n - 1; i++)
    {
        printf("\tVocal \"%c\": #%3d\t", vocales[i], frecuencia[i]);
        for (j = 0; j < frecuencia[i]; j++)
            printf("*");
        printf("\n");
    }
    printf("\tNúmero de palabras:\t%d\n\n", frecuencia[n - 1] + 1);
}

void llena_frecuencias(char c, int arreglo[])
{
    switch (c)
    {
    case 'a':
        arreglo[0]++;
        break;
    case 'e':
        arreglo[1]++;
        break;
    case 'i':
        arreglo[2]++;
        break;
    case 'o':
        arreglo[3]++;
        break;
    case 'u':
        arreglo[4]++;
        break;
    case ' ':
        arreglo[5]++;
        break;
    default:
        break;
    }
}