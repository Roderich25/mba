
// COA-602 Tarea 5 Ejercicio 3
// Pablo Rodrigo Avila Solis
// Fecha de modificacion: 18-Feb-2020 (Ya funciona para intervalos negativos!)

/******************************************************************************************************
Determine por aproximaciones sucesivas, la longitud L de una curva definida por una funcion
y =f(x) = x*x. definida en el intervalo [a,b] de la recta numérica. Por ejemplo, x en [0, 5].
Divida el intervalo en n partes (1, 2, 4, 8 etc.)
para cada n, utilice aproximaciones lineales en cada subintervalo para calcular L en cada iteracion i.
para i = 1, 2, 3, ..., n-1, n.
Termine cuando abs(Ln - Ln-1) < epsilon o cuando en i > nmax.
Lea los valores del intervalo, nmax (numero maximo de intentos) y epsilon.
******************************************************************************************************/
#include <stdio.h>
#include <math.h>

int main()
{
    double a0, a, b, len, sub, Ln1 = 0, Ln, epsilon;
    int n = 1, fin = 0, contador = 0, n_max;

    printf("Ingresar el intervalo para evaluar la longitud de arco de f(x)=x^2:\t");
    scanf("%lf %lf", &a0, &b);
    printf("Ingresar numero maximo de intentos:\t");
    scanf("%d", &n_max);
    printf("Ingresar el valor de epsilon:\t");
    scanf("%lf", &epsilon);
    len = b - a0;
    printf("i\tn\taprox\n");

    while (!fin)
    {
        contador++;
        int i;
        for (i = 1; i <= n; i++)
        {
            sub = len / n;
            Ln += sqrt(((a + sub) * (a + sub) - a * a) * ((a + sub) * (a + sub) - a * a) + sub * sub);
            a += sub;
        }
        printf("%d\t%d\t%lf\n", contador, n, Ln);
        n *= 2;
        a = a0;

        if (contador > n_max)
            fin = 1;
        if (Ln > Ln1)
        {
            if (Ln - Ln1 <= epsilon)
                fin = 1;
        }
        else
        {
            if (Ln1 - Ln <= epsilon)
                fin = 1;
        }
        Ln1 = Ln;
        Ln = 0;
    }
    printf("La longitud de arco aproximada es %.4lf\n", Ln1);

    return 0;
}
