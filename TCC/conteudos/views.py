from django.shortcuts import get_object_or_404, render

from .models import Categoria, Conteudo


def lista(request):
	termo = request.GET.get('q', '').strip()[:100]
	categoria_slug = request.GET.get('categoria', '').strip()
	categorias = Categoria.objects.order_by('nome')
	categoria_selecionada = categorias.filter(slug=categoria_slug).first()

	materiais = Conteudo.objects.filter(ativo=True).select_related('categoria')
	if termo:
		materiais = materiais.filter(titulo__icontains=termo)
	if categoria_selecionada:
		materiais = materiais.filter(categoria=categoria_selecionada)

	return render(request, 'conteudos/lista.html', {
		'materiais': materiais,
		'categorias': categorias,
		'termo': termo,
		'categoria_selecionada': categoria_selecionada,
	})


def detalhe(request, pk):
	conteudo = get_object_or_404(
		Conteudo.objects.select_related('categoria'),
		pk=pk,
		ativo=True,
	)
	return render(request, 'conteudos/detalhe.html', {'conteudo': conteudo})
