// COA-602 Tarea 6 Ejercicio 4
// Fecha de creacion: 20-Febrero-2020
/***************************************************************************************************************************************
Modifique el programa para jugar con dos dados visto en clase, para jugar contra la maquina. Lea el nombre del usuario, elija el turno
de inicio (Maquina o Usuario). Defina un numero de unidades de pago inicial para el usuario, el numero maximo de partidas.
Defina las reglas para pagar cuando el usuario gana o pierde.
El juego termina cuando el usuario pierde todo su monto inicial o despues de un numero maximo de partidas. 
Imprima los resultados intermedios del juego, y el balance final del usuario. Defina al menos dos o tres funciones.
****************************************************************************************************************************************/

/************************************************************************************************************
 * Reglas del juego:
 * En el turno impar el usuario/maquina recibe el monto igual a la suma de los dados de su oponente,
 * en el turno par el usuario/maquina paga el monto de la suma de los dados a su oponente.
 * Ambos empiezan con $24 y el juego termina despues de 7 turnos o cuando alguno de los dos jugadores
 * tenga menos de $12 y en su siguiente turno le toque pagar porque esto le impedira pagarle a su oponente.
*************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int tira_dado(void);
int decide_turno(char *usuario);
void imprime_turnos(int a, int b);

int main()
{
    srand(time(NULL));
    char nombre[25];
    int contador_usuario = 1, contador_maquina = 1, max = 7, turno, suma, dado1, dado2;
    double monto_usuario = 24, monto_maquina = 24;

    printf("Ingresar su nombre:\t");
    scanf("%s", nombre);

    //Decide Turno
    turno = decide_turno(nombre);

    //Dados
    while ((contador_usuario + contador_maquina) <= 2 * max + 1)
    {
        imprime_turnos(contador_maquina, contador_usuario);
        dado1 = tira_dado();
        dado2 = tira_dado();
        suma = dado1 + dado2;
        if (turno > 0)
        {
            printf("Suma de dados %s: %d + %d = %d\n", nombre, dado1, dado2, suma);
            if (contador_usuario % 2)
            {
                monto_usuario += suma;
                monto_maquina -= suma;
                printf("\t%s recibe $%.2lf de maquina.\n", nombre, (double)suma);
            }
            else
            {
                monto_usuario -= suma;
                monto_maquina += suma;
                printf("\t%s paga $%.2lf a maquina.\n", nombre, (double)suma);
            }
            contador_usuario++;
        }
        else
        {
            printf("Suma de dados maquina: %d + %d = %d\n", dado1, dado2, suma);
            if (contador_maquina % 2)
            {
                monto_usuario -= suma;
                monto_maquina += suma;
                printf("\tMaquina recibe $%.2lf de %s.\n", (double)suma, nombre);
            }
            else
            {
                monto_usuario += suma;
                monto_maquina -= suma;
                printf("\tMaquina paga $%.2lf a %s.\n", (double)suma, nombre);
            }
            contador_maquina++;
        }

        if (!(contador_usuario % 2))
            if (monto_usuario < 12)
                max = 0;
        if (!(contador_maquina % 2))
            if (monto_maquina < 12)
                max = 0;
        turno *= -1;
    }
    printf("\nBalance Final\t%s: $%.2lf\tMaquina: $%.2lf\n\n", nombre, monto_usuario, monto_maquina);

    return 0;
}

int tira_dado(void)
{
    return 1 + rand() % 6;
}

int decide_turno(char *usuario)
{
    if (rand() % 2)
    {
        printf("\nEmpieza %s.\n", usuario);
        return 1;
    }
    else
    {
        printf("\nEmpieza la maquina.\n");
        return -1;
    }
}

void imprime_turnos(int a, int b)
{
    double c = a + b;
    if (!(fmod(c, 2)))
        printf("\nTurno %d:\n", (a + b) / 2);
}
