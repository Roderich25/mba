// COA-602 Tarea 7 Ejercicio 5
// Fecha de creacion: 24-Febrero-2020
/**************************************************************************************************************************
Lea una lista de tripletas a, b, c de enteros positivos [1,10] que terminan con una marca de fin de datos (0, 0, 0),
cada tripleta corresponde a un individuo evaluado. Identifique el porcentaje de individuos y el promedio aritmetico de los
individuos, que tienen una evaluacion en a ∈ [7,9], en b ∈ [8,10], o en c ∈ [7,9].
Si no hay individuos que cumplan con los requisitos indicarlo.
(ojo. No utilizar los operadores lógicos AND u OR), únicamente los operadores relacionales o unarios.
***************************************************************************************************************************/
#include <stdio.h>

int checa_condicion(int a, int b, int c);

void resultados(int contador, int total, int suma);

int main()
{
    int a, b, c, fin, contador_condicion, contador_total, suma_condicion;
    fin = 0;
    contador_total = -1;
    contador_condicion = 0;
    suma_condicion = 0;

    while (!fin)
    {
        int marca;
        printf("Ingresar tripleta de numeros enteros entre 1 y 10 separada por comas:\t");
        scanf("%d, %d, %d", &a, &b, &c);

        marca = checa_condicion(a, b, c);

        if (marca > 0)
        {
            contador_condicion++;
            suma_condicion += marca;
        }

        if (a == 0)
            if (b == 0)
                if (c == 0)
                    fin = 1;

        contador_total++;
    }

    resultados(contador_condicion, contador_total, suma_condicion);

    return 0;
}

int checa_condicion(int a, int b, int c)
{
    int marca = 0;
    if (a >= 7)
        if (a <= 9)
            marca++;

    if (b >= 8)
        if (b <= 10)
            marca++;

    if (c >= 7)
        if (c <= 9)
            marca++;

    if (marca == 3)
    {
        return a + b + c;
    }
    else
    {
        return 0;
    }
}

void resultados(int contador, int total, int suma)
{
    if (contador > 0)
    {
        printf("\n\tPorcentaje\tPromedio\n");
        printf("\t%.2lf %%\t\t%.2lf\n\n", (double)100 * contador / total, (double)suma / (3 * contador));
    }
    else
    {
        printf("\nNo hay tripletas que cumplan con las condicones requeridas.\n\n");
    }
}
