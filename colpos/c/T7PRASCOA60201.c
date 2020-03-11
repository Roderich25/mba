// COA-602 Tarea 7 Ejercicio 1
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 24-Febrero-2020
/****************************************************************************************************************************
Plantee una solución iterativa para calcular el factorial de un numero n. Utilice variables de double precision.
Lea el numero n, y luego, genere un cuadro comparativo con la solucion recursiva del factorial de n, para valores de 1 a n.
Una vez el cuadro generado, pregunte al usuario si desea continuar con el calculo del factorial de un numero.
*****************************************************************************************************************************/
#include <stdio.h>

long int factorial_iterativo(int x);

long int factorial_recursivo(int x);

void cuadro_comparativo(int n);

int main()
{
    int fin, n;
    do
    {
        printf("Ingresar un numero para calcular el factorial:\t");
        scanf("%d", &n);

        cuadro_comparativo(n);

        printf("Si desea continuar calculando factorial presione [0], si desea salir presione [1]:\t");
        scanf("%d", &fin);
    } while (!fin);
    return 0;
}

long int factorial_iterativo(int x)
{
    int i;
    long int n = 1;
    for (i = 1; i <= x; i++)
    {
        n = n * i;
    }

    return n;
}

long int factorial_recursivo(int x)
{
    if (x == 1)
    {
        return x;
    }
    else
    {
        return x * factorial_recursivo(x - 1);
    }
}

void cuadro_comparativo(int n)
{
    int i;
    printf("\tFactorial de:\t\tIterativo:\t\tRecursivo:\n");
    for (i = 1; i <= n; i++)
    {
        printf("\t%9d\t\t%20ld\t\t%20ld\n", i, factorial_iterativo(i), factorial_recursivo(i));
    }
}
