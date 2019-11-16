from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateField(null=True)

    def __str__(self):
        return f'{self.name} Inc.'

    class Meta:
        verbose_name_plural = "Companies"


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'#{self.name}'


class Programmer(models.Model):
    name = models.CharField(max_length=60)
    birth_year = models.PositiveSmallIntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return f'{self.name}@{self.company.name}'
