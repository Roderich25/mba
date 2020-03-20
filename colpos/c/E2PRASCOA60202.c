/* Examen 2 Ejercicio 2 */
/* Fecha de creacion: 19 de marzo de 2020*/
/************************************************************************************************************************
 * Defina una función f_fibonacci, para calcular en forma iterativa el algoritmo de Fibonacci.
 * Lea el término deseado n de la sucesión e imprima únicamente todos los términos pares hasta el término n.
 ************************************************************************************************************************/
#include <stdio.h>

void f_fibonacci(int n);

int main()
{
    int n;
    printf("Ingresar n para calcular pares de Fibonacci:\t");
    scanf("%d", &n);
    f_fibonacci(n);

    return 0;
}

void f_fibonacci(int n)
{
    int i, n_1, n_2, fibo;

    n_1 = 1;
    n_2 = 0;
    for (i = 2; i <= n; i++)
    {

        fibo = n_1 + n_2;
        if (i % 2 == 0)
            printf("\tFibonacci de %d es:\t%d\n", i, fibo);

        n_2 = n_1;
        n_1 = fibo;
    }
}