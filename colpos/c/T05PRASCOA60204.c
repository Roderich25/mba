// COA-602 Tarea 5 Ejercicio 4
/******************************************************************************************************
Lea dos numeros num1 y num2 (digito por digito) de longitud lon1 y lon2, respectivamente.
La longitud de cada numero debe estar entre 1 y 5 digitos.
Luego pregunte si desea la suma o la resta de los numeros leidos.
Efectue la operacion solicitada e imprima los numeros leidos y el resultado.
(digito por digito) aplique el algoritmo aritmetico de primaria para realizar la suma.
Por ejemplo:
num1 de longitud lon1 = 3, leer d1, d2, d3: 2 3 4
num2 de longitud lon2 = 2, leer e1, e2: 9 8
Resultado  234
         +  98 
         _____
           332
******************************************************************************************************/
#include <stdio.h>
int main()
{
    int d1 = 0, d2 = 0, d3 = 0, d4 = 0, d5 = 0;
    int e1 = 0, e2 = 0, e3 = 0, e4 = 0, e5 = 0;
    int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
    int signo = 1, bandera = -1, marca = -1;
    int lon1, lon2, operacion, temp;
    // Primer número
    printf("Ingresar longitud del primer numero (entre 1 y 5):\t");
    scanf("%d", &lon1);
    printf("Ingresar primer numero digito por digito, separados por un espacio:\t");
    if (lon1 == 5)
        scanf("%d %d %d %d %d", &d5, &d4, &d3, &d2, &d1);
    if (lon1 == 4)
        scanf("%d %d %d %d", &d4, &d3, &d2, &d1);
    if (lon1 == 3)
        scanf("%d %d %d", &d3, &d2, &d1);
    if (lon1 == 2)
        scanf("%d %d", &d2, &d1);
    if (lon1 == 1)
        scanf("%d", &d1);
    // Segundo numero
    printf("Ingresar longitud del segundo numero (entre 1 y 5):\t");
    scanf("%d", &lon2);
    printf("Ingresar segundo numero digito por digito, separados por un espacio:\t");
    if (lon2 == 5)
        scanf("%d %d %d %d %d", &e5, &e4, &e3, &e2, &e1);
    if (lon2 == 4)
        scanf("%d %d %d %d", &e4, &e3, &e2, &e1);
    if (lon2 == 3)
        scanf("%d %d %d", &e3, &e2, &e1);
    if (lon2 == 2)
        scanf("%d %d", &e2, &e1);
    if (lon2 == 1)
        scanf("%d", &e1);
    //¿Pregunar si se desea sumar o restar?
    printf("\nSi desea Sumar presione [1], si desea Restar presione [2]:\t");
    scanf("%d", &operacion);
    printf("\n");

    if (operacion == 1)
    {
        printf("\t %d%d%d%d%d\n", d5, d4, d3, d2, d1);
        printf("\t+%d%d%d%d%d\n", e5, e4, e3, e2, e1);
        f1 = e1 + d1;
        if (f1 > 9)
        {
            f2++;
            f1 -= 10;
        }
        f2 += e2 + d2;
        if (f2 > 9)
        {
            f3++;
            f2 -= 10;
        }
        f3 += e3 + d3;
        if (f3 > 9)
        {
            f4++;
            f3 -= 10;
        }
        f4 += e4 + d4;
        if (f4 > 9)
        {
            f5++;
            f4 -= 10;
        }
        f5 += e5 + d5;
    }
    else
    {
        if (operacion == 2)
        {
            printf("\t %d%d%d%d%d\n", d5, d4, d3, d2, d1);
            printf("\t-%d%d%d%d%d\n", e5, e4, e3, e2, e1);
            if (d5 != e5)
            {
                if (bandera == -1)
                {
                    if (d5 < e5)
                    {
                        bandera = 0;
                        signo = -1;
                    }
                    else
                    {
                        bandera = 0;
                    }
                }
            }
            if (d4 != e4)
            {
                if (bandera == -1)
                {
                    if (d4 < e4)
                    {
                        bandera = 0;
                        signo = -1;
                    }
                    else
                    {
                        bandera = 0;
                    }
                }
            }
            if (d3 != e3)
            {
                if (bandera == -1)
                {
                    if (d3 < e3)
                    {
                        bandera = 0;
                        signo = -1;
                    }
                    else
                    {
                        bandera = 0;
                    }
                }
            }
            if (d2 != e2)
            {
                if (bandera == -1)
                {
                    if (d2 < e2)
                    {
                        bandera = 0;
                        signo = -1;
                    }
                    else
                    {
                        bandera = 0;
                    }
                }
            }
            if (d1 != e1)
            {
                if (bandera == -1)
                {
                    if (d1 < e1)
                    {
                        bandera = 0;
                        signo = -1;
                    }
                    else
                    {
                        bandera = 0;
                    }
                }
            }
            //
            if (signo == -1)
            {
                temp = e5;
                e5 = d5;
                d5 = temp;
                temp = e4;
                e4 = d4;
                d4 = temp;
                temp = e3;
                e3 = d3;
                d3 = temp;
                temp = e2;
                e2 = d2;
                d2 = temp;
                temp = e1;
                e1 = d1;
                d1 = temp;
            }
            //
            if (d1 >= e1)
            {
                f1 += d1 - e1;
            }
            else
            {
                f1 += (10 + d1) - e1;
                f2--;
            }

            if (d2 >= e2)
            {
                f2 += d2 - e2;
            }
            else
            {
                f2 += (10 + d2) - e2;
                f3--;
            }

            if (d3 >= e3)
            {
                f3 += d3 - e3;
            }
            else
            {
                f3 += (10 + d3) - e3;
                f4--;
            }

            if (d4 >= e4)
            {
                f4 += d4 - e4;
            }
            else
            {
                f4 += (10 + d4) - e4;
                f5--;
            }

            if (d5 >= e5)
            {
                f5 += d5 - e5;
            }
            else
            {
                f5 += d5 - e5;
                f5--;
            }
        }
        else
        {
            printf("Operacion no valida.\n");
        }
    }
    printf("\t______\n", e5, e4, e3, e2, e1);
    if (operacion <= 2)
    {
        if (operacion >= 1)
        {
            if (signo >= 1)
            {
                printf("\t+");
            }
            else
            {
                printf("\t-");
            }
        }
    }

    if (f5 == 0)
        if (marca == -1)
        {
            printf(" ");
        }
        else
        {
            printf("%d", f5);
        }
    else
    {
        printf("%d", f5);
        marca = 0;
    }

    if (f4 == 0)
        if (marca == -1)
        {
            printf(" ");
        }
        else
        {
            printf("%d", f4);
        }
    else
    {
        printf("%d", f4);
        marca = 0;
    }

    if (f3 == 0)
        if (marca == -1)
        {
            printf(" ");
        }
        else
        {
            printf("%d", f3);
        }
    else
    {
        printf("%d", f3);
        marca = 0;
    }

    if (f2 == 0)
        if (marca == -1)
        {
            printf(" ");
        }
        else
        {
            printf("%d", f2);
        }
    else
    {
        printf("%d", f2);
        marca = 0;
    }
    if (operacion == 1)
    {
        printf("%d\n", f1);
    }
    else
    {
        if (operacion == 2)
        {
            printf("%d\n", f1);
        }
    }
    printf("\n");
}
