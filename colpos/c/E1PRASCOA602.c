// COA-602 Examen 1
// Fecha de creacion: 20-Febrero-2020
/*****************************************************************************************************************************************************************
Suponga que una pelota se suelta a una altura inicial, alt_0, después de un nummero de rebotes, n_rebotes, cae por debajo de una altura limite alt_limite.
En cada rebote la pelota pierde altura, si el número de rebote es par, la pelota pierde 5% de su altura anterior, de otra forma, pierde 3% de su altura anterior.
Lea alt_limite, y n_rebotes deseados; luego, determine por aproximaciones, a que altura inicial debe soltarse la pelota, para caer por debajo de alt_limite.
Imprima alt_0, y para cada rebote i-esimo, la altura de la pelota; y al final, el numero de intentos realizados.
******************************************************************************************************************************************************************/
#include <stdio.h>

int main()
{
    double alt_limite, alt_aprox, alt_0;
    int n_rebotes, fin = 0, cual, contador;
    printf("Ingresar altura limite:\t");
    scanf("%lf", &alt_limite);
    printf("Ingresar numero de rebotes:\t");
    scanf("%d", &n_rebotes);

    alt_aprox = alt_limite + 0.1;
    while (!fin)
    {
        contador++;
        alt_0 = alt_aprox;
        cual = -1;
        int i;
        printf("Intento\tRebote\tAltura actual\tMarca\tAltura Aproximacion\n");
        for (i = 1; i <= n_rebotes; i++)
        {
            if (i % 2 == 0)
            {
                alt_0 = alt_0 * (1 - 0.05);
            }
            else
            {
                alt_0 = alt_0 * (1 - 0.03);
            }
            if (cual == -1)
                if (alt_0 <= alt_limite)
                    cual = i;
            printf("%d\t%d\t%lf\t%d\t%lf\n", contador, i, alt_0, cual, alt_aprox);
        }
        printf("\n");

        if (cual == n_rebotes)
        {
            fin = 1;
        }
        else
        {
            alt_aprox += 0.1;
        }
    }
    printf("La altura inicial necesaria es: %lf\n", alt_aprox);
    printf("Aproximacion lograda despues de %d intentos de altura inicial.\n\n", contador);

    return 0;
}
