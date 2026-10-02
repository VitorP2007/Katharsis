# Especificacao: Katharsis

**Status:** Rascunho
**Idioma:** Portugues do Brasil

## Objetivo

Definir uma aplicacao web pequena e responsiva que apoie o bem-estar emocional durante a vida academica por meio de autopercepcao, psicoeducacao contextualizada e orientacao inicial sobre busca de apoio. O Katharsis considera desafios como estudos, avaliacoes, trabalhos, prazos, organizacao do tempo, relacoes e adaptacao, sem presumir que sejam iguais para todos. Tem finalidade informativa e preventiva e nao diagnostica, avalia clinicamente ou substitui atendimento profissional.

## Publico-alvo

Estudantes de instituicoes de ensino, especialmente do ensino superior, que desejam compreender melhor o bem-estar emocional durante sua trajetoria academica, consultar informacoes educativas ou conhecer orientacoes gerais de acolhimento.

## Funcionalidades

1. **Inicio:** apresentar o nome Katharsis, a proposta do sistema e acessos claros ao check-in, aos conteudos e ao acolhimento.
2. **Meu check-in:** permitir selecionar uma percepcao emocional atual entre Muito bem, Bem, Neutro, Preocupado e Sobrecarregado. Pode oferecer um campo opcional de observacao. O registro representa somente a percepcao do proprio estudante.
3. **Conteudos:** disponibilizar materiais educativos sobre Ansiedade, Estresse, Sono e saude mental, Saude mental nos estudos, Autocuidado e Quando procurar ajuda. Os textos aproximam os temas de provas, trabalhos, prazos, organizacao do tempo, descanso, adaptacao e relacoes na vida estudantil, sem presumir experiencias iguais ou indicar transtornos. Cada material possui titulo, resumo e texto educativo.
4. **Acolhimento:** explicar de forma geral que o estudante pode buscar apoio quando perceber dificuldades que estejam interferindo em seu cotidiano. A secao deve permitir incorporar informacoes institucionais futuramente, sem exibir nomes, contatos ou procedimentos nao fornecidos.
5. **Responsabilidade e privacidade:** informar os limites do sistema e permitir o uso no primeiro MVP sem conta ou identificacao pessoal.

## Requisitos funcionais

- **RF-01:** O sistema deve apresentar na pagina inicial o nome Katharsis e uma explicacao breve de sua finalidade informativa e preventiva.
- **RF-02:** A pagina inicial deve oferecer acesso as areas Meu check-in, Conteudos e Acolhimento.
- **RF-03:** O sistema deve permitir que o estudante selecione uma opcao de percepcao emocional: Muito bem, Bem, Neutro, Preocupado ou Sobrecarregado.
- **RF-04:** O sistema pode oferecer um campo opcional para uma observacao relacionada ao check-in. O campo nao deve ser obrigatorio.
- **RF-05:** O sistema deve deixar claro que o check-in e uma autopercepcao do momento, nao uma avaliacao clinica.
- **RF-06:** O sistema deve disponibilizar conteudos educativos para os temas Ansiedade, Estresse, Sono e saude mental, Saude mental nos estudos, Autocuidado e Busca de ajuda.
- **RF-07:** Cada conteudo deve apresentar titulo, resumo e texto educativo.
- **RF-08:** O sistema deve apresentar uma secao de acolhimento com orientacao geral sobre considerar a busca de apoio quando dificuldades estiverem interferindo no cotidiano.
- **RF-09:** A estrutura da secao de acolhimento deve permitir a inclusao futura de informacoes institucionais, sem inventar nomes de setores, profissionais, contatos, servicos ou etapas.
- **RF-10:** O sistema deve informar que nao realiza diagnostico ou avaliacao clinica e nao substitui profissionais de Psicologia ou outros servicos especializados.
- **RF-11:** O sistema nao deve exigir cadastro nem login no primeiro MVP.
- **RF-12:** Apos envio valido, o sistema deve salvar a percepcao selecionada, a observacao opcional e a data do registro sem associar esses dados a uma conta de estudante.
- **RF-13:** Apos salvar um check-in valido, o sistema deve apresentar uma confirmacao amigavel.
- **RF-14:** A area de conteudos deve listar materiais ativos com titulo, resumo, categoria e acesso a leitura.
- **RF-15:** O sistema deve permitir buscar materiais pelo titulo e filtrar por categoria, aplicando os criterios em conjunto quando ambos forem informados.
- **RF-16:** A pagina de detalhe deve apresentar titulo, categoria, data de publicacao, texto educativo e um controle para voltar a listagem.
- **RF-17:** A pagina inicial deve deixar evidente que o Katharsis apoia o bem-estar emocional durante a jornada academica e oferecer acesso a check-in, conteudos e acolhimento.

## Requisitos nao funcionais

- **RNF-01:** A interface deve funcionar em computador, tablet e celular.
- **RNF-02:** A navegacao e os textos devem ser claros, consistentes e compreensiveis para o publico estudantil.
- **RNF-03:** A apresentacao deve ser acolhedora e profissional, sem parecer excessivamente clinica.
- **RNF-04:** O sistema deve minimizar a coleta e a exposicao de dados. Nao deve solicitar nome, matricula, CPF ou outros identificadores pessoais.
- **RNF-05:** O sistema deve usar linguagem respeitosa, nao estigmatizante e sem afirmacoes que prometam resultados clinicos.
- **RNF-06:** Os conteudos devem ser organizados de modo que titulo, resumo e texto educativo sejam distinguiveis e faceis de consultar.

## Regras de negocio

- **RN-01:** As cinco opcoes do check-in sao descricoes de autopercepcao e nao podem ser convertidas em diagnostico, pontuacao clinica, nivel de risco ou classificacao de transtorno.
- **RN-02:** O check-in nao deve produzir interpretacoes automatizadas nem recomendacoes clinicas com base na opcao selecionada ou na observacao.
- **RN-03:** O uso do sistema nao exige identificacao, cadastro ou login no primeiro MVP.
- **RN-04:** O sistema nao deve solicitar dados pessoais identificaveis.
- **RN-05:** A secao de acolhimento deve limitar-se a orientacoes gerais ate que informacoes institucionais verificadas sejam fornecidas.
- **RN-06:** Todo conteudo deve reforcar, quando pertinente, o carater informativo e preventivo do sistema e que ele nao substitui atendimento profissional.
- **RN-07:** A observacao do check-in, se oferecida, e opcional e nao deve ser usada para avaliacao clinica.
- **RN-08:** Um check-in pode conter somente a percepcao selecionada, uma observacao opcional e a data do registro; nao deve conter identificadores pessoais ou vinculo a conta de estudante.
- **RN-09:** Os registros nao devem ser apresentados como historico individual nem usados para diagnostico, pontuacao, classificacao, alerta ou conclusao sobre a saude mental.

## Historias de usuario e criterios de aceitacao

### HU-01: Conhecer a proposta

Como estudante, quero entender rapidamente a finalidade do Katharsis e acessar suas areas principais para escolher o que preciso consultar.

**Criterios de aceitacao:**

- Dada a pagina inicial, quando ela e exibida, entao apresenta o nome Katharsis e comunica que cuidar de si tambem faz parte da jornada academica.
- Dada a pagina inicial, quando o estudante procura uma funcionalidade, entao encontra acesso ao check-in, aos conteudos e ao acolhimento.
- A comunicacao nao deve sugerir diagnostico ou tratamento.

### HU-02: Registrar uma percepcao

Como estudante, quero selecionar como percebo meu momento emocional para fazer uma pausa de autopercepcao.

**Criterios de aceitacao:**

- Dada a area Meu check-in, quando as opcoes sao exibidas, entao estao disponiveis Muito bem, Bem, Neutro, Preocupado e Sobrecarregado.
- Quando o estudante seleciona uma opcao, o sistema a trata apenas como autopercepcao, sem pontuacao, rotulo clinico, diagnostico ou avaliacao.
- Se houver campo de observacao, ele e opcional e pode ficar vazio.
- A tela informa que o check-in nao e uma avaliacao clinica.

### HU-03: Consultar psicoeducacao

Como estudante, quero encontrar informacoes educativas sobre temas de saude mental relevantes para meus estudos e cotidiano.

**Criterios de aceitacao:**

- Dada a area Conteudos, quando a lista e exibida, entao inclui Ansiedade, Estresse, Sono e saude mental, Saude mental nos estudos, Autocuidado e Busca de ajuda.
- Cada card apresenta titulo, resumo, categoria e a acao Ler conteudo.
- Os exemplos e textos relacionam os temas a situacoes academicas sem afirmar que todos os estudantes as vivenciam.
- O estudante pode buscar por titulo, filtrar por categoria e combinar os dois criterios.
- A pagina de detalhe apresenta titulo, categoria, data de publicacao, texto educativo e controle para voltar a listagem.
- Os textos sao informativos e nao apresentam diagnosticos individuais nem prometem resultados clinicos.

### HU-04: Entender quando buscar apoio

Como estudante, quero consultar orientacoes gerais sobre acolhimento para considerar buscar apoio quando estiver enfrentando dificuldades.

**Criterios de aceitacao:**

- Dada a area Acolhimento, quando consultada, entao explica que pode ser pertinente buscar apoio se dificuldades estiverem interferindo no cotidiano.
- A area nao apresenta nomes, contatos, servicos ou etapas institucionais que nao tenham sido fornecidos.
- A estrutura permite adicionar informacoes institucionais verificadas futuramente.

### HU-05: Usar o sistema sem identificacao

Como estudante, quero consultar as areas principais sem criar uma conta ou fornecer dados de identificacao.

**Criterios de aceitacao:**

- O primeiro MVP nao exige cadastro nem login para acessar o inicio, o check-in, os conteudos ou o acolhimento.
- O sistema nao solicita nome, matricula, CPF ou outros identificadores pessoais.

## Limites de escopo

O primeiro MVP inclui somente as areas Inicio, Meu check-in, Conteudos e Acolhimento, com os requisitos descritos nesta especificacao.

Estao fora do escopo:

- Rede social, publicacao ou compartilhamento entre estudantes.
- Chat ou comunicacao com profissionais.
- Inteligencia artificial para analise psicologica.
- Diagnostico, triagem, avaliacao clinica ou classificacao de transtornos.
- Questionarios clinicos ou pontuacao de risco.
- Agendamento de atendimentos.
- Prontuario ou historico clinico.
- Cadastro ou catalogo de profissionais.
- Notificacoes complexas.
- Cadastro, login ou coleta de dados identificaveis no primeiro MVP.
- Publicacao de contatos, servicos ou fluxos institucionais ainda nao fornecidos.
- Decisoes sobre tecnologias, arquitetura, persistencia de dados ou mecanismos de armazenamento, que nao sao definidas por esta especificacao.

Os check-ins podem ser salvos sem vinculo a identificadores de estudantes. O primeiro MVP nao apresenta historico individual. O periodo de retencao e o processo de descarte dos registros ainda precisam ser definidos antes de uma publicacao fora do ambiente academico local.
