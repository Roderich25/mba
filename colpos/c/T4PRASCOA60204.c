#include <stdio.h>
#include <math.h>

int main()
{
    double x0 = 0, y0 = 0, distancia = 1;
    double x1, y1, x, y;
    int contador;
    printf("Ingresar valores consecutivos x1 y1 respectivamente:\t");
    scanf("%lf %lf", &x, &y);

    // epsilon = 0.1
    x1 = x;
    y1 = y;
    printf("#\tPosición (x1, y1)\tDistancia\n");
    contador = 0;
    while (distancia > 0.1)
    {
        contador++;
        x1 = (x1 - x0) / 2;
        y1 = (y1 - y0) / 2;
        distancia = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2));
        printf("%3d\t(%.5lf, %.5lf)\t%.5lf\n", contador, x1, y1, distancia);
    }
    printf("Para acercase a la solución con epsilon=%.3lf se necesitaron %d iteraciones.\n", 0.1, contador);

    // epsilon = 0.01
    x1 = x;
    y1 = y;
    printf("#\tPosición (x1, y1)\tDistancia\n");
    contador = 0;
    while (distancia > 0.01)
    {
        contador++;
        x1 = (x1 - x0) / 2;
        y1 = (y1 - y0) / 2;
        distancia = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2));
        printf("%3d\t(%.5lf, %.5lf)\t%.5lf\n", contador, x1, y1, distancia);
    }
    printf("Para acercase a la solución con epsilon=%.3lf se necesitaron %d iteraciones.\n", 0.01, contador);
    
    // epsilon = 0.001
    x1 = x;
    y1 = y;
    printf("#\tPosición (x1, y1)\tDistancia\n");
    contador = 0;
    while (distancia > 0.001)
    {
        contador++;
        x1 = (x1 - x0) / 2;
        y1 = (y1 - y0) / 2;
        distancia = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2));
        printf("%3d\t(%.5lf, %.5lf)\t%.5lf\n", contador, x1, y1, distancia);
    }
    printf("Para acercase a la solución con epsilon=%.3lf se necesitaron %d iteraciones.\n", 0.001, contador);

    return 0;
}
