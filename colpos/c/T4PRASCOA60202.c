#include <stdio.h>

int main()
{
    double a, x, y;
    double diferencia = 1;
    printf("¿Raíz cuadrada (aproximada) de?\t");
    scanf("%lf", &a);
    printf("Ingresar valor inicial:\t");
    scanf("%lf", &x);

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

    printf("\n\tLa raíz cuadrada (aproximada) de %.2lf es %.2lf\n.", a, x);
    return 0;
}
