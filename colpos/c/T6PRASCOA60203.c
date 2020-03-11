// COA-602 Tarea 6 Ejercicio 3
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 20-Febrero-2020
/***************************************************************************************************************************************
Determine por aproximaciones sucesivas, el area de una curva definida por una funcion y = f(x) = x*x, definida en el intervalo [a,b]
de la recta numeerica. Por ejemplo, x en [-10, 10]. Utilice la estrategia algoriitmica descrita en clase. Que basicamente consiste en
subdividir el intervalo x, en partes iguales, y calcular el aarea de rectaangulos por debajo de la curva y luego sumarlos para obtener
un area inferior, Ainf y luego, calcular el aarea de rectangulos por arriba de la curva, con los mismos subintervalos definidos, y
sumarlos para obtener un area superior Asup. Termine el calculo, cuando abs(Ainf-Asup) < epsilon (definido por el usuario).
Imprima en cada aproximacion i, Asup, Ainf, diferencia. Al final imprima el valor del Area aproximada, y el numero total de iteraciones.
Defina al menos, dos funciones.
****************************************************************************************************************************************/
#include <stdio.h>

double fun(double x);

double area(double a, double b, int n, int tipo);

double absoluto(double n1, double n2);

int main()
{
    double a, b, area_inferior, area_superior, epsilon;
    int contador, fin = 0;

    printf("Ingresar un intervalo, separado por un espacio:\t");
    scanf("%lf %lf", &a, &b);

    printf("Ingresar valor de epsilon deseado:\t");
    scanf("%lf", &epsilon);

    contador = 1;
    while (!fin)
    {

        area_inferior = area(a, b, contador, 1);
        area_superior = area(a, b, contador, 2);
        printf("%d\t%lf\t%lf\t%lf\n", contador, area_inferior, area_superior, area_superior - area_inferior);

        if (contador > 1)
            if (absoluto(area_inferior, area_superior) < epsilon)
                fin = 1;

        contador++;
    }

    printf("\tEl area aproximada es: %lf unidades cuadradas.\n\tLograda con %d iteraciones.\n", (area_inferior + area_superior) / 2, contador);
    return 0;
}

double fun(double x)
{
    return x * x;
}

double area(double a, double b, int n, int tipo)
{
    int i = 1;
    double sub = (b - a) / n, area = 0;

    for (i = 1; i <= n; i++)
    {
        if (tipo == 1)
        {
            if (a < 0)
            {
                area += sub * fun(a + sub);
            }
            else
            {
                area += sub * fun(a);
            }
        }
        if (tipo == 2)
        {
            if (a < 0)
            {
                area += sub * fun(a);
            }
            else
            {
                area += sub * fun(a + sub);
            }
        }

        a += sub;
    }

    return area;
}

double absoluto(double n1, double n2)
{
    if (n1 - n2 > 0)
    {
        return n1 - n2;
    }
    else
    {
        return n2 - n1;
    }
}
