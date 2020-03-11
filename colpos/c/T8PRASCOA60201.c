// COA-602 Tarea 8 Ejercicio 1
// Pablo Rodrigo Avila Solis
// Fecha de creacion: 5-Marzo-2020
/*******************************************************************************************************************************
Realice una validacion de la entrada del numero de hileras (hil) y numero de columnas (col) de un patron rectangular de numeros,
(5 < hil, col < 10). Si el usuario da un valor incorrecto, repita la lectura del dato. Luego, continue con el programa y
despliegue un menu con tres opciones 1, 2 y 3, valide la opción si es incorrecta repita la lectura de la opcion.
Luego, imprima un mensaje con la opción seleccionada.
Pregunte al usuario si desea continuar o terminar la ejecución del programa. Defina funcion f1 para leer hileras o columnas.
Una función f2 para leer la opción. Y una función f3 para imprimir la opción seleccionada.
********************************************************************************************************************************/
#include <stdio.h>

void f1(void);
int f2(void);
void f3(int n);

int main(void)
{
    int n;
    f1();
    n = f2();
    f3(n);
    return 0;
}

void f1(void)
{
    int hileras, columnas, continuar = 1;
    while (continuar)
    {
        printf("\nIngresar numero de hileras menor que 5: \t");
        scanf("%d", &hileras);
        printf("\nIngresar numero de columnas menor que 10:\t");
        scanf("%d", &columnas);
        if (hileras < 5)
            if (columnas < 10)
                continuar = 0;
    }
}

int f2(void)
{
    int opcion = -1;
    while (1)
    {
        printf("\nElija la opcion:\n\t[1] Uno\n\t[2] Dos\n\t[3] Tres\n");
        scanf("\t%d", &opcion);
        while (getchar() != '\n')
            ;
        if (opcion >= 1)
            if (opcion <= 3)
                break;
    }
    return opcion;
}

void f3(int n)
{
    printf("\nLa opcion seleccionada es: %d\n\n", n);
}