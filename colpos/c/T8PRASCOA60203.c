// COA-602 Tarea 8 Ejercicio 3
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 5-Marzo-2020
/*********************************************************************************************************************************
Se desea sumar y restar números de más de 20 dígitos y menor o igual a 50 dígitos. Los números son proporcionados por el usuario.
Seleccionar la operación deseada e imprimir el resultado.
**********************************************************************************************************************************/
#include <stdio.h>
#include <math.h>
#define SIZE 50

void ingresar_digitos(int d[]);
void suma(int a[], int b[]);
void compara_resta(int a[], int b[]);
void resta(int n1[], int n2[], int signo);
void imprimir(int c[], int signo);

int main(void)
{
    int numero1[SIZE] = {0};
    int numero2[SIZE] = {0};
    int operacion;

    ingresar_digitos(numero1);
    ingresar_digitos(numero2);

    printf("Para sumar presione [1], para restar presione [2]:\t");
    scanf("%d", &operacion);
    if (operacion == 1)
        suma(numero1, numero2);
    if (operacion == 2)
        compara_resta(numero1, numero2);
}

void ingresar_digitos(int d[])
{
    int temp[SIZE] = {0}, i, j;
    printf("\nIngresar numero digito tras digito hasta 50 digitos, terminar con -1 si desea terminar antes:\n");
    i = 0;
    while (i < SIZE)
    {
        printf("\tDigito %d:\t", i+1);
        scanf("%d", &temp[i]);
        if (temp[i] == -1)
            break;
        i++;
    }

    for (j = 0; j < i; j++)
    {
        d[j] = temp[i - j - 1];
    }
}

void suma(int a[], int b[])
{
    int temp, i, suma = 0, c[SIZE] = {0};
    for (i = 0; i < SIZE; i++)
    {
        temp = a[i] + b[i];
        if (temp > 9)
        {
            if (i < SIZE - 1)
            {
                c[i + 1]++;
                c[i] += temp - 10;
            }
            else
            {
                c[i] += temp;
            }
        }
        else
        {
            c[i] += temp;
        }
    }
    printf("SUMA\n");
    imprimir(c, 1);
}

void compara_resta(int a[], int b[])
{
    int i, mayor = 1, signo=1;
    for (i = SIZE - 1; i >= 0; i--)
    {
        if (b[i] != a[i])
        {
            if (b[i] > a[i])
            {
                mayor = 2;
                signo = -1;
                break;
            }
            else
            {
                mayor = 1;
                break;
            }
        }
    }

    if (mayor == 1)
    {
        resta(a, b, 1);
    }
    else
    {
        resta(b, a, signo);
    }
}

void resta(int n1[], int n2[], int signo)
{
    int i, c[SIZE] = {0};
    for (i = 0; i < SIZE; i++)
    {
        if (n1[i] >= n2[i])
        {
            c[i] += n1[i] - n2[i];
        }
        else
        {
            if (i < SIZE - 1)
            {
                c[i] += (n1[i] + 10) - n2[i];
                n1[i + 1]--;
            }
            else
            {
                c[i] += n1[i] - n2[i];
                n1[i]--;
            }
        }
    }
    printf("RESTA\n");
    imprimir(c, signo);
}

void imprimir(int c[], int signo)
{
    printf("El resultado es:\t");
    int i, bandera = -1;
    if (signo < 0)
        printf("-");
    for (i = SIZE - 1; i >= 0; i--)
    {
        if (c[i] == 0)
        {
            if (bandera == 1)
            {
                printf("%d", c[i]);
            }
        }
        else
        {
            printf("%d", c[i]);
            bandera = 1;
        }
    }
    if(bandera==-1) printf("%d", 0);
    printf("\n");
}
