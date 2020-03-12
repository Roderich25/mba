// COA-602 Tarea 7 Ejercicio 4
// Fecha de creacion: 24-Febrero-2020
/**************************************************************************************************************************
Lea un numero entero positivo x, de maximo dos digitos. Aplicando la definicion de la funcion raíz cuadrada z = f(x) = √x.
Encuentre y tal que z^2=x, para determinar la parte entera de ( z ).
Luego, calcule la parte decimal de z, utilizando una aproximación lineal.
Imprima la solución completa de y (parte entera y parte decimal).
Luego, calcule z1 = sqrt(x) y calcule el error relativo con respecto al valor exacto, de su respuesta calculada z.
Imprima x, z, z1 yel error relativo error.
***************************************************************************************************************************/
#include <stdio.h>
#include <math.h>

int raiz_parte_entera(int x);

double raiz_parte_decimal(int x, int b);

int main()
{
    // Entrada
    int x, c;
    double d, z, z1, error_relativo;
    printf("Ingresar entero positivo de maximo dos digitos:\t");
    scanf("%d", &x);

    // Proceso
    c = raiz_parte_entera(x);
    d = raiz_parte_decimal(x, c);
    z = c + d;
    z1 = sqrt(x);
    error_relativo = (z - z1) / z1;

    // Salida
    printf("\nx\tsqrt aprox\tsqrt verdadera\terror relativo\n");
    printf("%d\t%.4lf\t\t%.4lf\t\t%.8lf\n\n", x, z, z1, error_relativo);

    return 0;
}

int raiz_parte_entera(int x)
{
    int c = 0;
    while (c * c <= x)
    {
        c++;
    }
    c--;
    return c;
}

double raiz_parte_decimal(int x, int b)
{
    return (double)(x - b * b) / (2 * b);
}
