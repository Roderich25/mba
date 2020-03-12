// COA-602 Tarea 7 Ejercicio 2
// Fecha de creacion: 24-Febrero-2020
/**********************************************************************************************************************************
Plantee una solución iterativa para calcular los termino de la sucesión de Fibonacci, lea el n-esimo termino deseado. Utilice
variables entero “long” para los terminos de la sucesion. Genere, un cuadro comparativo con la solucion recursiva de Fibonacci,
para valores de 0 a n.
Una vez el cuadro generado, pregunte al usuario si desea continuar con el calculo del termino n-esimo de la sucesión de Fibonacci.
***********************************************************************************************************************************/
#include <stdio.h>

long int fibonacci_iterativo(int x);

long int fibonacci_recursivo(int x);

void cuadro_comparativo(int n);

int main()
{
    int fin, n;
    do
    {
        printf("Ingresar un numero para calcular Fibonacci:\t");
        scanf("%d", &n);

        cuadro_comparativo(n);

        printf("Si desea continuar calculando Fibonacci presione [0], si desea salir presione [1]:\t");
        scanf("%d", &fin);
    } while (!fin);

    return 0;
}

long int fibonacci_iterativo(int x)
{
    long int n;
    if (x == 0 || x == 1)
    {
        return x;
    }
    else
    {
        long int n_2 = 0;
        long int n_1 = 1;
        int i;
        for (i = 2; i <= x; i++)
        {
            n = n_1 + n_2;

            n_2 = n_1;
            n_1 = n;
        }
        return n;
    }
}

long int fibonacci_recursivo(int x)
{
    if (x == 0 || x == 1)
    {
        return x;
    }
    else
    {
        return fibonacci_recursivo(x - 1) + fibonacci_recursivo(x - 2);
    }
}

void cuadro_comparativo(int n)
{
    int i;
    printf("\tFibonacci de:\t\tIterativo:\t\tRecursivo:\n");
    for (i = 0; i <= n; i++)
    {
        printf("\t%9d\t\t%20ld\t\t%20ld\n", i, fibonacci_iterativo(i), fibonacci_recursivo(i));
    }
}
