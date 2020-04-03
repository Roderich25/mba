#include <stdio.h>

int main()
{
    // Entrada
    double monto_final;
    printf("Ingresar monto final objetivo:\t");
    scanf("%lf", &monto_final);
    int n;
    printf("Ingresar el número de años requerido:\t");
    scanf("%d", &n);
    
	//Proceso
    int contador = 0;
    double monto_inicial = monto_final/ 2;
    double diferencia = monto_inicial;
    double tasa = 0.5;
    double y_aprox;

    while(diferencia > (monto_final * 0.01))
    {
        contador++;
        y_aprox = monto_inicial;

        int i = 1;
        for (i = 1; i <= n * 12; i++)
        {
            y_aprox = y_aprox * (1 + tasa / 100);
        }

        if (monto_final - y_aprox > 0)
        {
            diferencia = monto_final - y_aprox;
            monto_inicial = monto_inicial * (1 + 0.001);
        }
        else
        {
            diferencia = y_aprox - monto_final;
            monto_inicial = monto_inicial * (1 - 0.001);
        }

    }
	
	//Salida
    printf("\nTotal de iteraciones: %d\n", contador);
    printf("El monto inicial aproximado para un objetivo de $%.2lf en %d años a una tasa mensual de %.2lf%% es de: $%.2lf\n", monto_final, n, tasa, monto_inicial);
    return 0;
}
