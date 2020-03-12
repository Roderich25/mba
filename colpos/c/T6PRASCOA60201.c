// COA-602 Tarea 6 Ejercicio 1
// Fecha de creacion: 20-Febrero-2020
/*************************************************************************************************************************************
Utilice al menos tres funciones (entrada, proceso, impresion) para resolver el problema de la raiz cuadrada por el metodo de Newton,
descrito en el problema 2 de T4 COA 602. Agregue una pregunta para volver a ejecutar el calculo de la raiz cuadrada.
*************************************************************************************************************************************/
#include <stdio.h>

double entrada(void);

double proceso(double a);

int salida(double numero, double respuesta);

double a, x;

int main()
{

    int marca;
    do
    {

        double a = entrada();

        double respuesta = proceso(a);

        marca = salida(a, respuesta);
    } while (!marca);

    return 0;
}

double entrada(void)
{
    double a;
    printf("\n�Raiz cuadrada (aproximada) de?\t");
    scanf("%lf", &a);
    return a;
}

double proceso(double a)
{
    double diferencia = 1, x = 1, y;

    while (diferencia > 0.00001)
    {
        y = (x + a / x) / 2;
        if (y - x > 0)
        {
            diferencia = y - x;
        }
        else
        {
            diferencia = x - y;
        }
        x = y;
    }
    return x;
}

int salida(double numero, double respuesta)
{
    int marca;
    printf("\n\tLa raiz cuadrada (aproximada) de %.2lf es %.2lf\n", numero, respuesta);
    printf("\n\n...Si desea continuar presione la tecla [0], si desea salir presione la tecla [1]:\t");
    scanf("%d", &marca);
    return marca;
}
