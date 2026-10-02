from django.db import models
from django.utils import timezone


class Categoria(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=120, unique=True)
	descricao = models.TextField(blank=True)

	class Meta:
		ordering = ('nome',)
		verbose_name = 'categoria'
		verbose_name_plural = 'categorias'

	def __str__(self):
		return self.nome


class Conteudo(models.Model):
	titulo = models.CharField(max_length=200)
	resumo = models.TextField()
	texto = models.TextField()
	categoria = models.ForeignKey(
		Categoria,
		on_delete=models.PROTECT,
		related_name='conteudos',
	)
	data_publicacao = models.DateTimeField(default=timezone.now)
	ativo = models.BooleanField(default=False)

	class Meta:
		ordering = ('titulo',)
		verbose_name = 'conteúdo'
		verbose_name_plural = 'conteúdos'

	def __str__(self):
		return self.titulo
