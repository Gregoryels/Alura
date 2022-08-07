from django.contrib import admin
from orcamentos.models import Despesas, Receitas
# Register your models here.

class Despesas_Admin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fiels = ('data', 'descricao')
    list_per_page = 20

admin.site.register(Despesas, Despesas_Admin)


class Receitas_Admin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fiels = ('data', 'descricao')
    list_per_page = 20


admin.site.register(Receitas, Receitas_Admin)
