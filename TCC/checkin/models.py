from django.db import models


class RegistroCheckIn(models.Model):
	class Percepcao(models.TextChoices):
		MUITO_BEM = 'muito_bem', 'Muito bem'
		BEM = 'bem', 'Bem'
		NEUTRO = 'neutro', 'Neutro'
		PREOCUPADO = 'preocupado', 'Preocupado'
		SOBRECARREGADO = 'sobrecarregado', 'Sobrecarregado'

	percepcao = models.CharField(max_length=20, choices=Percepcao.choices)
	observacao = models.CharField(max_length=500, blank=True)
	criado_em = models.DateTimeField(auto_now_add=True)
