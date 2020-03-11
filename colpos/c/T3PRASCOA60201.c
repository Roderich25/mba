#include <stdio.h>

int main()
{
	int n, anterior, actual, numero_incorrecto;
	char tipo;
	int orden = 0;
	int contador = 1;
	int posicion = -1;

	printf("Ingrese en tamaño de la lista: ");
	scanf("%d", &n);

	if (n <= 15)
	{
		if (n >= 5)
		{
			printf("Ingrese tipo de ordenamiento, A para ascendete o D para descendente: ");
			scanf("%s", &tipo);
			if (tipo == 'A')
			{
				orden = 1;
			}
			else
			{
				if (tipo == 'D')
				{
					orden = -1;
				}
			}
			if (orden != 0)
			{
				printf("Ingrese el primer valor: ");
				scanf("%d", &anterior);
				while (contador < n)
				{
					printf("Ingrese el siguiente valor: ");
					scanf("%d", &actual);
					if (orden > 0)
					{
						if (anterior > actual)
						{
							if (posicion == -1)
							{
								posicion = contador + 1;
								numero_incorrecto = actual;
							}
						}
					}
					else
					{
						if (anterior < actual)
						{
							if (posicion == -1)
							{
								posicion = contador + 1;
								numero_incorrecto = actual;
							}
						}
					}
					contador++;
					anterior = actual;
				}
				if (posicion == -1)
				{
					printf("\tOrdenamiento correcto!\n");
				}
				else
				{
					printf("\tEl número %d es incorrecto en la posición %d.\n", numero_incorrecto, posicion);
				}
			}
			else
			{
				printf("Orden requerido inválido!\n");
			}
		}
		else
		{
			printf("Tamaño de lista no válido. Muy pequeño!\n");
		}
	}
	else
	{
		printf("Tamaño de lista no válido. Muy grande!\n");
	}
	return 0;
}
