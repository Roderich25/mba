#include <stdio.h>

int main()
{
	int numero;
	int contador_unicos = 1;
	int suma_unicos = 0;
	int descartados = 0;
	int unico01 = 0;
	int unico02 = 0;
	int unico03 = 0;
	int unico04 = 0;
	int unico05 = 0;
	int unico06 = 0;
	int unico07 = 0;
	int unico08 = 0;
	int unico09 = 0;
	int unico10 = 0;
	int contador_unico01 = 0;
	int contador_unico02 = 0;
	int contador_unico03 = 0;
	int contador_unico04 = 0;
	int contador_unico05 = 0;
	int contador_unico06 = 0;
	int contador_unico07 = 0;
	int contador_unico08 = 0;
	int contador_unico09 = 0;
	int contador_unico10 = 0;

	while (contador_unicos <= 10)
	{
		printf("Ingresar entero positivo o -99 para terminar: ");
		scanf("%d", &numero);
		if (numero == -99)
		{
			contador_unicos = 99;
		}
		else
		{
			if (numero > 0)
			{
				if (numero == unico01)
				{
					contador_unico01 = contador_unico01 + 1;
				}
				else if (numero == unico02)
				{
					contador_unico02 = contador_unico02 + 1;
				}
				else if (numero == unico03)
				{
					contador_unico03 = contador_unico03 + 1;
				}
				else if (numero == unico04)
				{
					contador_unico04 = contador_unico04 + 1;
				}
				else if (numero == unico05)
				{
					contador_unico05 = contador_unico05 + 1;
				}
				else if (numero == unico06)
				{
					contador_unico06 = contador_unico06 + 1;
				}
				else if (numero == unico07)
				{
					contador_unico07 = contador_unico07 + 1;
				}
				else if (numero == unico08)
				{
					contador_unico08 = contador_unico08 + 1;
				}
				else if (numero == unico09)
				{
					contador_unico09 = contador_unico09 + 1;
				}
				else if (numero == unico10)
				{
					contador_unico10 = contador_unico10 + 1;
				}
				else if (contador_unicos == 1)
				{
					unico01 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 2)
				{
					unico02 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 3)
				{
					unico03 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 4)
				{
					unico04 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 5)
				{
					unico05 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 6)
				{
					unico06 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 7)
				{
					unico07 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 8)
				{
					unico08 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 9)
				{
					unico09 = numero;
					contador_unicos = contador_unicos + 1;
				}
				else if (contador_unicos == 10)
				{
					unico10 = numero;
					contador_unicos = contador_unicos + 1;
				}
			}

			else
			{
				printf("Número inválido, intente de nuevo.\n");
			}
		}
	}

	//Salida
	if (contador_unico01 < 1)
	{
		suma_unicos = suma_unicos + unico01;
	}
	else
	{
		descartados = contador_unico01 + descartados + 1;
	}

	if (contador_unico02 < 1)
	{
		suma_unicos = suma_unicos + unico02;
	}
	else
	{
		descartados = contador_unico02 + descartados + 1;
	}

	if (contador_unico03 < 1)
	{
		suma_unicos = suma_unicos + unico03;
	}
	else
	{
		descartados = contador_unico03 + descartados + 1;
	}

	if (contador_unico04 < 1)
	{
		suma_unicos = suma_unicos + unico04;
	}
	else
	{
		descartados = contador_unico04 + descartados + 1;
	}

	if (contador_unico05 < 1)
	{
		suma_unicos = suma_unicos + unico05;
	}
	else
	{
		descartados = contador_unico05 + descartados + 1;
	}

	if (contador_unico06 < 1)
	{
		suma_unicos = suma_unicos + unico06;
	}
	else
	{
		descartados = contador_unico06 + descartados + 1;
	}

	if (contador_unico07 < 1)
	{
		suma_unicos = suma_unicos + unico07;
	}
	else
	{
		descartados = contador_unico07 + descartados + 1;
	}

	if (contador_unico08 < 1)
	{
		suma_unicos = suma_unicos + unico08;
	}
	else
	{
		descartados = contador_unico08 + descartados + 1;
	}

	if (contador_unico09 < 1)
	{
		suma_unicos = suma_unicos + unico09;
	}
	else
	{
		descartados = contador_unico09 + descartados + 1;
	}

	if (contador_unico10 < 1)
	{
		suma_unicos = suma_unicos + unico10;
	}
	else
	{
		descartados = contador_unico10 + descartados + 1;
	}
	printf("Suma de números únicos: %d\n", suma_unicos);
	printf("Conteo de números descartados: %d\n", descartados);

	return 0;
}
