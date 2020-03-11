// COA-602 Tarea 5 Ejercicio 1
// Pablo Rodrigo Avila Solis
/******************************************************************************************************************
Elabore un programa que despliegue un menuÅ de opciones para imprimir cada uno de los cuatro patrones de simbolos @.
Lea el numero de hileras y columnas (maximo 15), luego elija el patron, e imprima el patron deseado.
Pregunte al usuario si desea continuar con la impresion de patrones, de otra forma,
termine la ejecucion del programa. Por ejemplo, para m=3 y n=3, las posibles opciones son:
@@@  @@@  @      @
@@    @@  @@    @@
@      @  @@@  @@@
******************************************************************************************************************/
#include <stdio.h>
int main()
{
    int marca, suma, dimension;
    int hileras;
    int columnas;
    int i, j, fin = 0;

    do
    {

        printf("Ingresar numero de hileras y columnas, separadas por un espacio:\t");
        scanf("%d %d", &hileras, &columnas);
        if (hileras <= 15)
        {
            if (columnas <= 15)
            {

                printf("\t#1   #2   #3   #4 \n");
                printf("\t@@@  @@@  @      @\n");
                printf("\t@@    @@  @@    @@\n");
                printf("\t@      @  @@@  @@@\n");
                printf("Elegir tipo de patron deseado, de 1 a 4:\t");
                scanf("%d", &marca);
                printf("\n");
                for (i = 1; i <= hileras; i++)
                {
                    printf("\t");
                    for (j = 1; j <= columnas; j++)
                    {
                        switch (marca)
                        {
                        case 1:
                            if (hileras > columnas)
                            {
                                dimension = hileras + 1;
                            }
                            else
                            {
                                dimension = columnas + 1;
                            }

                            if (i + j <= dimension)
                                printf("@");
                            break;

                        case 2:
                            if (hileras > columnas)
                            {
                                dimension = -hileras + columnas;
                            }
                            else
                            {
                                dimension = 0;
                            }

                            if (j - i >= dimension)
                            {
                                printf("@");
                            }
                            else
                            {
                                printf(" ");
                            }
                            break;

                        case 3:
                            if (hileras > columnas)
                            {
                                dimension = 1;
                            }
                            else
                            {
                                dimension = columnas - hileras + 1;
                            }

                            if (j - i < dimension)
                                printf("@");
                            break;

                        case 4:
                            if (hileras > columnas)
                            {
                                dimension = columnas + 1;
                            }
                            else
                            {
                                dimension = hileras + 1;
                            }

                            if (i + j < dimension)
                            {
                                printf(" ");
                            }
                            else
                            {
                                printf("@");
                            }
                            break;

                        default:
                            printf("Numero de patron incorrecto!");
                            i = hileras;
                            j = columnas;
                            break;
                        }
                    }
                    printf("\n");
                }
                printf("\n");
            }
            else
            {
                printf("Numero de columnas debe ser menor o igual que 15.\n");
            }
        }
        else
        {
            printf("Numero de hileras debe ser menor o igual que 15.\n");
        }
        printf("Si desea continuar con el programa presione [1], para salir presione cualquier tecla.\n");
        scanf("%d", &fin);
        if (fin == 1)
        {
            fin = 0;
        }
        else
        {
            fin = 1;
        }
    } while (!fin);
}
