from django.db import models

# Create your models here.

class Despesas(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    data = models.DateField()

    def __str__(self):
        return f"{self.data}: {self.valor} - {self.descricao}"

    class Meta:
        verbose_name = "Despesas"
        verbose_name_plural = "Despesas"

class Receitas(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    data = models.DateField()

    def __str__(self):
        return f"{self.data}: {self.valor} - {self.descricao}"

    class Meta:
        verbose_name = "Receitas"
        verbose_name_plural = "Receitas"