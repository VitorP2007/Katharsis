from django.db import migrations


CONTEUDOS = {
    'Ansiedade': {
        'resumo': 'Reflexões sobre preocupações com provas e avaliações, sem presumir uma experiência única.',
        'texto': (
            'Provas, apresentações e avaliações podem trazer expectativa e preocupação para '
            'alguns estudantes. Para outras pessoas, essas situações podem ter outro peso ou '
            'não ser uma fonte de preocupação.\n\n'
            'Perceber o que está ocupando seus pensamentos e como a rotina acadêmica está '
            'organizada pode ajudar a reconhecer necessidades, sem transformar uma reação '
            'comum em diagnóstico.\n\n'
            'Se preocupações estiverem interferindo nos estudos, no descanso ou em outras '
            'atividades, conversar com alguém de confiança ou procurar apoio pode ser uma possibilidade.'
        ),
    },
    'Estresse': {
        'resumo': 'Uma leitura sobre trabalhos, prazos e acúmulo de atividades na vida estudantil.',
        'texto': (
            'Trabalhos, prazos próximos e acúmulo de atividades podem ser percebidos como '
            'exigências. A quantidade de demandas, os recursos disponíveis e a forma de cada '
            'pessoa lidar com elas variam.\n\n'
            'Observar compromissos, tempo disponível e pausas possíveis pode ajudar a '
            'compreender a própria rotina. Organização não elimina todas as dificuldades e '
            'não é medida de valor pessoal.\n\n'
            'Se as demandas estiverem interferindo no cotidiano acadêmico ou em outras áreas, '
            'uma conversa de apoio pode ajudar a pensar nos próximos passos.'
        ),
    },
    'Sono e saúde mental': {
        'resumo': 'Como descanso e horários de estudo podem se relacionar com o bem-estar.',
        'texto': (
            'Horários de aula, períodos de estudo, deslocamentos e responsabilidades podem '
            'influenciar os horários de descanso. A relação entre sono e bem-estar também '
            'varia conforme a rotina e as condições de cada pessoa.\n\n'
            'Não existe uma rotina perfeita que sirva para todos. Observar como estudo e '
            'descanso se encaixam no cotidiano pode ser um ponto de partida para reconhecer '
            'necessidades, sem transformar diferenças de rotina em falha pessoal.\n\n'
            'Se questões relacionadas ao sono persistirem e afetarem o cotidiano, buscar '
            'orientação profissional pode ser uma possibilidade.'
        ),
    },
    'Saúde mental nos estudos': {
        'resumo': 'Reflexões sobre avaliações, organização do tempo, relações e adaptação à vida acadêmica.',
        'texto': (
            'A vida acadêmica pode envolver avaliações, trabalhos, prazos, organização do '
            'tempo, relações interpessoais e adaptação à instituição. Essas experiências não '
            'são iguais para todos e podem mudar ao longo da trajetória estudantil.\n\n'
            'Perceber quais aspectos estão presentes no próprio momento pode ajudar a '
            'identificar necessidades e recursos disponíveis. Estratégias que funcionam para '
            'uma pessoa ou período podem não servir para outra situação.\n\n'
            'Quando dificuldades relacionadas aos estudos ou a outras áreas interferem no '
            'cotidiano, conversar com alguém de confiança ou buscar orientação pode ser considerado.'
        ),
    },
    'Autocuidado': {
        'resumo': 'Possibilidades de cuidado durante períodos de maior exigência acadêmica, sem fórmulas únicas.',
        'texto': (
            'Em períodos com mais avaliações, trabalhos ou prazos, pode ser útil perceber '
            'quais necessidades estão sendo deixadas de lado e quais pausas são possíveis. '
            'As condições e possibilidades de cada estudante são diferentes.\n\n'
            'Descanso, atividades significativas, organização do tempo, limites e conversas '
            'com pessoas de confiança podem fazer parte do cuidado. Essas possibilidades '
            'não são uma lista obrigatória nem uma medida de desempenho.\n\n'
            'Autocuidado não substitui apoio profissional quando dificuldades estão afetando '
            'o cotidiano e não precisa seguir uma fórmula única.'
        ),
    },
    'Quando procurar ajuda': {
        'resumo': 'Como considerar apoio quando dificuldades acadêmicas ou pessoais interferem no cotidiano.',
        'texto': (
            'Pode ser válido considerar apoio quando provas, trabalhos, prazos, adaptação ou '
            'outras dificuldades estão interferindo nos estudos, nas relações, no descanso ou '
            'em atividades do cotidiano. Não é necessário encontrar um rótulo para pedir orientação.\n\n'
            'Cada instituição possui recursos e procedimentos próprios. Esta plataforma não '
            'informa contatos ou etapas institucionais que não tenham sido oficialmente '
            'disponibilizados. Quando essas informações existirem, consulte fontes oficiais.'
        ),
    },
}


def atualizar_conteudos(apps, schema_editor):
    Conteudo = apps.get_model('conteudos', 'Conteudo')
    banco = schema_editor.connection.alias

    for titulo, campos in CONTEUDOS.items():
        Conteudo.objects.using(banco).filter(titulo=titulo).update(**campos)


class Migration(migrations.Migration):
    dependencies = [
        ('conteudos', '0002_seed_psicoeducacao'),
    ]

    operations = [
        migrations.RunPython(atualizar_conteudos, migrations.RunPython.noop),
    ]
