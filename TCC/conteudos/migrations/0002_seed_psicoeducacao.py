from django.db import migrations
from django.utils import timezone


MATERIAIS = (
    {
        'nome_categoria': 'Ansiedade',
        'slug_categoria': 'ansiedade',
        'descricao_categoria': 'Informações educativas sobre ansiedade e cotidiano.',
        'titulo': 'Ansiedade',
        'resumo': 'Informações gerais para contextualizar a ansiedade e sua relação com o cotidiano.',
        'texto': (
            'A ansiedade é uma experiência humana que pode surgir diante de incertezas, '
            'mudanças ou expectativas. Cada pessoa pode percebê-la de uma maneira diferente; '
            'uma mesma situação pode ser vivida de formas distintas em momentos diferentes.\n\n'
            'Observar o contexto, as emoções e as necessidades envolvidas pode ser um ponto '
            'de partida para compreender a própria experiência. Não existe uma resposta única '
            'que sirva para todas as pessoas.\n\n'
            'Se dificuldades estiverem interferindo no cotidiano, conversar com alguém de '
            'confiança ou buscar apoio profissional pode ser uma possibilidade.'
        ),
    },
    {
        'nome_categoria': 'Estresse',
        'slug_categoria': 'estresse',
        'descricao_categoria': 'Informações educativas sobre estresse e demandas do dia a dia.',
        'titulo': 'Estresse',
        'resumo': 'Uma introdução ao estresse, às demandas do dia a dia e à percepção dos próprios limites.',
        'texto': (
            'Prazos, mudanças e responsabilidades podem ser percebidos como exigências. '
            'A forma de lidar com essas situações varia de pessoa para pessoa e também pode '
            'mudar conforme o contexto.\n\n'
            'Perceber quais demandas estão ocupando espaço e quais recursos estão disponíveis '
            'pode ajudar a pensar nos próximos passos. Pausas e conversas de apoio são '
            'possibilidades gerais, não regras que funcionam da mesma forma para todo mundo.'
        ),
    },
    {
        'nome_categoria': 'Sono e saúde mental',
        'slug_categoria': 'sono-saude-mental',
        'descricao_categoria': 'Informações educativas sobre sono, rotina e bem-estar.',
        'titulo': 'Sono e saúde mental',
        'resumo': 'Uma leitura sobre descanso, rotina e bem-estar no cotidiano.',
        'texto': (
            'O sono faz parte da rotina e pode se relacionar com disposição, atenção e '
            'bem-estar. Horários, ambiente, responsabilidades e outros aspectos da vida '
            'podem influenciar a experiência de descanso.\n\n'
            'Não existe uma rotina perfeita que sirva para todas as pessoas. Se questões '
            'relacionadas ao sono persistirem e afetarem o cotidiano, uma conversa com um '
            'profissional de saúde pode ajudar a pensar em alternativas adequadas a cada realidade.'
        ),
    },
    {
        'nome_categoria': 'Saúde mental nos estudos',
        'slug_categoria': 'saude-mental-nos-estudos',
        'descricao_categoria': 'Informações educativas sobre bem-estar na vida acadêmica.',
        'titulo': 'Saúde mental nos estudos',
        'resumo': 'Reflexões sobre vida acadêmica, bem-estar e atenção às próprias necessidades.',
        'texto': (
            'A vida acadêmica pode envolver prazos, avaliações, mudanças e expectativas. '
            'Essas demandas fazem parte de contextos diferentes e podem afetar a forma como '
            'cada estudante organiza o cotidiano.\n\n'
            'Reconhecer limites, dividir tarefas quando possível e conversar com pessoas de '
            'confiança são algumas possibilidades gerais. Cada instituição tem recursos '
            'próprios; procure informações institucionais verificadas quando estiverem disponíveis.'
        ),
    },
    {
        'nome_categoria': 'Autocuidado',
        'slug_categoria': 'autocuidado',
        'descricao_categoria': 'Informações educativas sobre cuidado e necessidades cotidianas.',
        'titulo': 'Autocuidado',
        'resumo': 'Ideias de cuidado possíveis e adequadas a diferentes realidades, sem fórmulas únicas.',
        'texto': (
            'Autocuidado não precisa ser uma lista de tarefas nem uma meta de desempenho. '
            'Pode envolver perceber necessidades e considerar escolhas possíveis dentro das '
            'condições de cada momento.\n\n'
            'Descanso, atividades significativas, organização do tempo, limites e conversas '
            'com pessoas de confiança podem fazer parte do cuidado. Nem todas as possibilidades '
            'estão ao alcance de todas as pessoas, e isso não é uma falha individual.'
        ),
    },
    {
        'nome_categoria': 'Quando procurar ajuda',
        'slug_categoria': 'quando-procurar-ajuda',
        'descricao_categoria': 'Informações educativas sobre considerar a busca de apoio.',
        'titulo': 'Quando procurar ajuda',
        'resumo': 'Reflexões sobre perceber quando dificuldades interferem no cotidiano e considerar apoio.',
        'texto': (
            'Pode ser válido considerar apoio quando dificuldades estão tornando atividades '
            'do cotidiano mais difíceis, quando a situação se prolonga ou quando conversar '
            'com alguém parece importante. Não é necessário encontrar um rótulo para pedir '
            'orientação.\n\n'
            'Uma pessoa de confiança, um profissional ou um serviço institucional confirmado '
            'podem ser caminhos a considerar. As informações de contato e os procedimentos '
            'dependem de cada instituição e devem ser consultados em fontes oficiais.'
        ),
    },
)


def criar_materiais(apps, schema_editor):
    Categoria = apps.get_model('conteudos', 'Categoria')
    Conteudo = apps.get_model('conteudos', 'Conteudo')
    banco = schema_editor.connection.alias

    for material in MATERIAIS:
        categoria, _ = Categoria.objects.using(banco).get_or_create(
            slug=material['slug_categoria'],
            defaults={
                'nome': material['nome_categoria'],
                'descricao': material['descricao_categoria'],
            },
        )
        Conteudo.objects.using(banco).get_or_create(
            titulo=material['titulo'],
            defaults={
                'resumo': material['resumo'],
                'texto': material['texto'],
                'categoria_id': categoria.pk,
                'data_publicacao': timezone.now(),
                'ativo': True,
            },
        )


def remover_materiais(apps, schema_editor):
    Categoria = apps.get_model('conteudos', 'Categoria')
    Conteudo = apps.get_model('conteudos', 'Conteudo')
    banco = schema_editor.connection.alias
    slugs = [material['slug_categoria'] for material in MATERIAIS]
    titulos = [material['titulo'] for material in MATERIAIS]

    Conteudo.objects.using(banco).filter(titulo__in=titulos).delete()
    for categoria in Categoria.objects.using(banco).filter(slug__in=slugs):
        if not Conteudo.objects.using(banco).filter(categoria_id=categoria.pk).exists():
            categoria.delete(using=banco)


class Migration(migrations.Migration):
    dependencies = [
        ('conteudos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_materiais, remover_materiais),
    ]
