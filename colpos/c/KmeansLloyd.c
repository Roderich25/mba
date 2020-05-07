/*******************************************************************************************************************************
 *  Implementación en C del algoritmo K-means                                                                                  *
 *  Entradas:                                                                                                                  *
 *    + nombre del archivo en formato csv, dentro del mismo folder                                                             * 
 *    + número de variables en el archivo                                                                                      *
 *    + número de clusters requeridos                                                                                          *
 *                                                                                                                             *
 *  Proceso:                                                                                                                   *
 *    + Se realiza el clustering de K-means usando el algoritmo de Lloyd.                                                      *
 *                                                                                                                             *          
 *  Salida:                                                                                                                    *
 *    + Impresión en pantalla de un diccionario estilo Python, de la forma {observación:etiqueta,...}                          *
 *                                                                                                                             *
 *******************************************************************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define VARIABLES 12      // Máximo de variables en el archivo csv
#define OBSERVACIONES 200 // Máximo número de observaciones en el archivo
#define ITERACIONES 100   // Máximo número de iteraciones para tratar de minimizar la función objetivo

void bienvenida(void);
void obs_aleatorias(double dat[][VARIABLES], double medias[][VARIABLES], int vars, int obs, int k);
void centroides(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k);
double genera_clusters(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k);
void k_means(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k, int imprimir);
double distancia(double arr1[], double arr2[], int n);
void imprime_clusters(int clusters[], int obs);
void lee_archivo(double dat[][VARIABLES], int *ptrVars, int *ptrObs, int *ptrK);

int main(void)
{
    srand(time(NULL));
    int k, obs, vars, t;
    int marca = 1;
    double medias[OBSERVACIONES][VARIABLES];
    int clusters[OBSERVACIONES];
    double datos[OBSERVACIONES][VARIABLES];
    printf("******************************************************************************************\n");
    printf("*                             Algoritmo K-means                                          *\n");
    printf("*                                                                                        *\n");
    printf("* Entrada nombre del archivo csv sin comillas, por ejemplo: iris.csv                     *\n");
    printf("* Número de variables en el archivo, ejemplo: 4                                          *\n");
    printf("* Número de clusters requeridos, ejemplo: 3                                              *\n");
    printf("*                                                                                        *\n");
    printf("******************************************************************************************\n\n");
    while (marca)
    {
        lee_archivo(datos, &vars, &obs, &k);
        if (k <= obs && obs > 0)
        {
            k_means(datos, medias, clusters, vars, obs, k, 1);
            for (t = 1; t < k; t++)
                k_means(datos, medias, clusters, vars, obs, t, 0);
        }
        else
        {
            printf("Número de clústers debe ser un número positivo menor o igual al número de observaciones.\n\n");
        }

        printf("\t¿Calcular de nuevo K-means con otro archivo? Presione '1' para SI o '0' para NO.\n\t> ");
        scanf("%d", &marca);
    }

    return 0;
}

/*
* La función obs_aleatorias encuentra k observaciones aleatorias ordenadas sin repertir del conjunto de datos
* para inicializar el algoritmo y las almacena en el vector de medias que se pasa por referencia.
*/
void obs_aleatorias(double dat[][VARIABLES], double medias[][VARIABLES], int vars, int obs, int k)
{
    int contador, i, j, temp, diff;
    int aleatorios[k];
    // Genera k observaciones aleatorias no-repetidas
    contador = 0;
    while (contador < k)
    {
        temp = rand() % obs;
        diff = -1;
        for (i = 0; i < contador; i++)

            if (aleatorios[i] == temp)
                diff++;

        if (diff == -1)
            aleatorios[contador++] = temp;
    }
    // Ordena k observaciones no-repetidas de forma ascendente
    for (i = 0; i < k - 1; i++)
        for (j = 0; j < k - 1; j++)
            if (aleatorios[j] > aleatorios[j + 1])
            {
                temp = aleatorios[j];
                aleatorios[j] = aleatorios[j + 1];
                aleatorios[j + 1] = temp;
            }
    // Guarda en medias valores de los puntos seleccionados
    for (i = 0; i < k; i++)
        for (j = 0; j < vars; j++)
            medias[i][j] = dat[aleatorios[i]][j];
}

/*
* La función centroides, determina a que centroide pertenece cada observación de acuerdo al arreglo de medias
* pasado por referencia y calcula los nuevos centroides calculados que se guardan nuevamente en el arreglo de medias. 
*/
void centroides(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k)
{
    int i, j, cluster;
    double dist, max;
    int contador[OBSERVACIONES] = {0};
    double acumulador[OBSERVACIONES][VARIABLES] = {0.0};
    // Determina a que clúster pertenece cada observacion (de acuerdo a su distancia)
    for (i = 0; i < obs; i++)
    {
        max = 9999999; // Se usa max para comparar y buscar mínimos
        for (j = 0; j < k; j++)
        {
            dist = distancia(medias[j], dat[i], vars);
            if (dist < max)
            {
                max = dist;
                cluster = j;
            }
            clusters[i] = cluster;
        }
    }
    // Medias de cada clúster
    for (i = 0; i < obs; i++)
    {
        contador[clusters[i]]++;
        for (j = 0; j < vars; j++)
            acumulador[clusters[i]][j] += dat[i][j];
    }
    for (i = 0; i < k; i++)
        for (j = 0; j < vars; j++)
            medias[i][j] = acumulador[i][j] / contador[i];
}

/*
* La función distancia devuelve un valor double que contiene la distancia euclidiana entre dos arreglos. 
*/
double distancia(double arr1[], double arr2[], int n)
{
    // Calcula distancia euclidiana entre dos arreglos
    int i;
    double suma;
    suma = 0;
    for (i = 0; i < n; i++)
        suma += pow(arr1[i] - arr2[i], 2);
    return sqrt(suma);
}

/*
* La función imprime_cluster se llama al final del algoritmo para imprimir en pantalla los resultados del algoritmo.
*/
void imprime_clusters(int clusters[], int obs)
{
    int i;
    printf("\nClústers: { observación: clúster, }\n\n{\n ");
    for (i = 0; i < obs; i++)
    {
        printf("\t%3d:%3d,", i + 1, clusters[i] + 1);
        if ((i + 1) % 10 == 0)
            printf("\n");
    }
    printf("}\n\n");
}

/*
* genera_clusters hace uso de las funciones obs_aleatorias y centroides, se encarga de verificar la convergencia para un
* conjunto de observaciones aleatorias y al final devuelve un double con la suma de cuadrados de los clusters encontrados.
*/
double genera_clusters(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k)
{
    int i, j, iter;
    double anteriores[OBSERVACIONES][VARIABLES] = {0.0}, var[OBSERVACIONES] = {0.0};
    double diff, acum;
    obs_aleatorias(dat, medias, vars, obs, k);
    diff = 1.0;
    iter = 0;
    // Checa convergencia de nuevos centroides bajo un epsilon o un máximo de 300 iteraciones para evitar caer en un ciclo infinito
    while (diff >= 0.001 || iter > 300)
    {
        diff = 0.0;
        centroides(dat, medias, clusters, vars, obs, k);
        for (i = 0; i < k; i++)
            for (j = 0; j < vars; j++)
            {
                diff += medias[i][j] - anteriores[i][j];
                anteriores[i][j] = medias[i][j];
            }
        iter++;
    }
    // Suma de cuadrados entre clústers
    for (i = 0; i < obs; i++)
        for (j = 0; j < vars; j++)
            var[clusters[i]] += pow(dat[i][j] - medias[clusters[i]][j], 2);
    // Suma de cuadrados total
    acum = 0.0;
    for (i = 0; i < k; i++)
        acum += var[i];
    return acum;
}

/*
* k_means lleva a cabo, con el uso de funciones auxiliares, el algoritmo de Lloyd e imprime los clusters requeridos.
*/
void k_means(double dat[][VARIABLES], double medias[][VARIABLES], int clusters[], int vars, int obs, int k, int imprimir)
{
    int i, clusters_final[obs];
    double suma_de_cuadrados, nueva_suma_de_cuadrados;
    suma_de_cuadrados = genera_clusters(dat, medias, clusters, vars, obs, k);
    for (i = 0; i < obs; i++)
        clusters_final[i] = clusters[i];
    // Busca suma de cuadrados mínima en cada iteración
    while (i < ITERACIONES)
    {
        nueva_suma_de_cuadrados = genera_clusters(dat, medias, clusters, vars, obs, k);
        if (nueva_suma_de_cuadrados < suma_de_cuadrados)
        {
            for (i = 0; i < obs; i++)
                clusters_final[i] = clusters[i];
            suma_de_cuadrados = nueva_suma_de_cuadrados;
        }
        i++;
    }

    if (imprimir)
    {
        printf("\nSuma de Cuadrados Total (entre clústers):\t%.4lf\n", suma_de_cuadrados);
        imprime_clusters(clusters_final, obs);
    }
    else
    {
        printf("Suma de Cuadrados con %d clusters es:\t%15.4lf\n", k, suma_de_cuadrados);
    }
}

/*
* Esta función lee un archivo en formato CSV, de hasta 12 variables cuantitativas.
* Recibe como parámetros:
*       + un arreglo de dos dimensiones,
*       + un apuntador que contiene la dirección en memoria del número de variables,
*       + un apuntador donde se guardaran el número de observaciones en el archivo,
*       + y un apuntador con la dirección en memoria del número de clusters deseados.
*/
void lee_archivo(double dat[][VARIABLES], int *ptrVars, int *ptrObs, int *ptrK)
{
    FILE *ptrFile;
    int i = 0;
    int confirma1 = 0, confirma2 = 0, confirma3 = 0;
    char archivo[256];
    while (!confirma1)
    {
        printf("\t* Nombre del archivo csv (separado por comas):\t");
        scanf("%s", archivo);
        printf("\tEl nombre del archivo es \"%s\", si es correcto presione '1' en caso contrario presione '0'.\n\t> ", archivo);
        scanf("%d", &confirma1);
    }
    while (!confirma2)
    {
        printf("\t* Ingresar número de variables en el archivo:\t");
        scanf("%d", ptrVars);
        printf("\tEl número de variables en el archivo es \"%d\", si es correcto presione '1' en caso contrario presione '0'.\n\t> ", *ptrVars);
        scanf("%d", &confirma2);
    }
    while (!confirma3)
    {
        printf("\t* Ingresar número de clústers deseados:\t");
        scanf("%d", ptrK);
        printf("\tEl número de clusters requeridos es \"%d\", si es correcto presione '1' en caso contrario presione '0'.\n\t> ", *ptrK);
        scanf("%d", &confirma3);
    }
    printf("\n");
    if ((ptrFile = fopen(archivo, "r")) == NULL)
    {
        printf("El archivo no puede abrirse."); // Si hay un error con el archivo, manda este mensaje
    }
    else
    {
        while (!feof(ptrFile))
        {
            switch (*ptrVars)
            {
            case 1:
                fscanf(ptrFile, "%lf", &dat[i][0]);
                break;
            case 2:
                fscanf(ptrFile, "%lf,%lf", &dat[i][0], &dat[i][1]);
                break;
            case 3:
                fscanf(ptrFile, "%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2]);
                break;
            case 4:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3]);
                break;
            case 5:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4]);
                break;
            case 6:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5]);
                break;
            case 7:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6]);
                break;
            case 8:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6], &dat[i][7]);
                break;
            case 9:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6], &dat[i][7], &dat[i][8]);
                break;
            case 10:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6], &dat[i][7], &dat[i][8], &dat[i][9]);
                break;
            case 11:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6], &dat[i][7], &dat[i][8], &dat[i][9], &dat[i][10]);
                break;
            case 12:
                fscanf(ptrFile, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf", &dat[i][0], &dat[i][1], &dat[i][2], &dat[i][3], &dat[i][4], &dat[i][5], &dat[i][6], &dat[i][7], &dat[i][8], &dat[i][9], &dat[i][10], &dat[i][10]);
                break;
            default:
                break;
            }
            i++;
        }
    }
    printf("Observaciones: %d\n", i);
    printf("Número de Clusters: %d\n", *ptrK);
    *ptrObs = i; // El número de observaciones se infiere del archivo y se guarda en su respectivo apuntador.
}