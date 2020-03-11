// COA-602 Tarea 7 Ejercicio 3
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 24-Febrero-2020
/*************************************************************************************************************************************
Calcule el valor aproximado de la funcion logaritmo natural, utilice una aproximacion en serie. Lea el numero x y la epsilon deseada.
Defina una funcion. Luego imprima su solucion y la solucion con la funcion log() de C.
**************************************************************************************************************************************/
#include <stdio.h>
#include <math.h>

double logaritmo_natural(double a, int n);

int main()
{
    // Entrada
    double a, epsilon;
    int i = 1;
    printf("Ingresar numero para calcular logaritmo natural:\t");
    scanf("%lf", &a);
    printf("Ingresar epsilon:\t");
    scanf("%lf", &epsilon);

    // Proceso
    while (fabs(logaritmo_natural(a, i) - log(a)) >= epsilon)
    {
        i++;
    }

    // Salida
    printf("Log propia\tLog de C\n");
    printf("%lf\t%lf\n", logaritmo_natural(a, i), log(a));
    
    return 0;
}

double logaritmo_natural(double a, int n)
{
    if (a <= 0)
    {
        if (a == 0)
        {
            return -INFINITY;
        }
        else
        {
            return NAN;
        }
    }
    else
    {
        int i;
        double x = 0;
        for (i = 1; i <= n; i++)
        {
            if (a <= 0.5)
            {
                x += pow(-1, i + 1) * pow((a - 1), i) / i;
            }
            else
            {
                x += pow((a - 1) / a, i) / i;
            }
        }
        return x;
    }
}
