/* Tarea 10 Ejercicio 2 */
/* Fecha de creacion: 19 de marzo de 2020*/
/******************************************************************************************************************************
 * Modifique el programa que calcula promedios y estadísticos a partir del arreglo bidimensional de calificaciones-estudiantes 
 * visto en clase. Agregue una función f1 para calcular la transpuesta de la matriz de calificaciones. 
 * Luego, calcule los promedios de exámenes utilizando la función promedio definida en el programa.
 * ****************************************************************************************************************************/
#include <stdio.h>
#define ESTUDIANTES 3
#define EXAMENES 4

int minimo(const int calificaciones[][EXAMENES], int alumnos, int examenes);
int maximo(const int calificaciones[][EXAMENES], int alumnos, int examenes);
double promedio(const int estableceCalif[], int examenes);
void despliegaArreglo(const int calificaciones[][EXAMENES], int alumnos, int examenes);
void f1(const int matriz[][EXAMENES], int transpuesta[][ESTUDIANTES], int alumnos, int examenes);

int main()
{
    int estudiante, examen;
    int calificacionesExamenes[EXAMENES][ESTUDIANTES];
    const int calificacionesEstudiantes[ESTUDIANTES][EXAMENES] =
        {{77, 68, 86, 73},
         {96, 87, 89, 78},
         {70, 90, 86, 81}};

    despliegaArreglo(calificacionesEstudiantes, ESTUDIANTES, EXAMENES);

    printf("\n\n\tCalificacion mas baja: %d\n\tCalificacion mas alta: %d\n\n",
           minimo(calificacionesEstudiantes, ESTUDIANTES, EXAMENES),
           maximo(calificacionesEstudiantes, ESTUDIANTES, EXAMENES));

    for (estudiante = 0; estudiante < ESTUDIANTES; estudiante++)
    {
        printf("\tEl promedio de calificacion del estudiante %d es %.2f\n",
               estudiante + 1, promedio(calificacionesEstudiantes[estudiante], EXAMENES));
    }

    printf("\n");
    f1(calificacionesEstudiantes, calificacionesExamenes, ESTUDIANTES, EXAMENES);
    for (examen = 0; examen < EXAMENES; examen++)
    {
        printf("\tEl promedio de calificacion del examen %d es %.2f\n",
               examen + 1, promedio(calificacionesExamenes[examen], ESTUDIANTES));
    }
    printf("\n");
}

void f1(const int matriz[][EXAMENES], int transpuesta[][ESTUDIANTES], int alumnos, int examenes)
{
    int i, j;
    for (i = 0; i < examenes; i++)
    {
        for (j = 0; j < alumnos; j++)
        {
            transpuesta[i][j] = matriz[j][i];
        }
    }
}

int minimo(const int calificaciones[][EXAMENES], int alumnos, int examenes)
{
    int i;
    int j;
    int califBaja = 100;

    for (i = 0; i < alumnos; i++)
    {
        for (j = 0; j < examenes; j++)
        {

            if (calificaciones[i][j] < califBaja)
            {
                califBaja = calificaciones[i][j];
            }
        }
    }
    return califBaja;
}

int maximo(const int calificaciones[][EXAMENES], int alumnos, int examenes)
{
    int i;
    int j;
    int califAlta = 0;

    for (i = 0; i < alumnos; i++)
    {

        for (j = 0; j < examenes; j++)
        {

            if (calificaciones[i][j] > califAlta)
            {
                califAlta = calificaciones[i][j];
            }
        }
    }
    return califAlta;
}

double promedio(const int conjuntoDeCalificaciones[], int examenes)
{
    int i;
    int total = 0;

    for (i = 0; i < examenes; i++)
    {
        total += conjuntoDeCalificaciones[i];
    }

    return (double)total / examenes;
}

void despliegaArreglo(const int calificaciones[][EXAMENES], int alumnos, int examenes)
{
    int i;
    int j;

    printf("\n\t\t\t\tExamen\t[1]\t[2]\t[3]\t[4]");
    for (i = 0; i < alumnos; i++)
    {
        printf("\nCalificaciones Estudiante[%d]:\t", i + 1);
        for (j = 0; j < examenes; j++)
        {
            printf("\t%3d", calificaciones[i][j]);
        }
    }
}

double promedio_examenes(const int estableceCalif[], int estudiantes)
{
    return 0.0;
}