from django.contrib import admin

from .models import Categoria, Conteudo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'slug')
	prepopulated_fields = {'slug': ('nome',)}
	search_fields = ('nome',)


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'categoria', 'data_publicacao', 'ativo')
	list_filter = ('categoria', 'ativo')
	list_select_related = ('categoria',)
	search_fields = ('titulo', 'resumo')
	date_hierarchy = 'data_publicacao'
