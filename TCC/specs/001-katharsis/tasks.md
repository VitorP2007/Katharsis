# Tarefas de implementacao: Katharsis

As tarefas seguem a Specification e o Plan. Cada item e pequeno e tem uma verificacao objetiva. Todas iniciam pendentes; marcar como concluida somente depois de executar a validacao indicada.

## Decisoes de escopo

- O pedido atual substitui a decisao anterior de check-in transitorio: registros sao salvos no SQLite sem vinculo a estudante, com observacao opcional limitada a 500 caracteres. Nao criar conta, identificacao ou historico publico.
- A retencao e o descarte dos registros ainda precisam de uma decisao antes da publicacao fora do ambiente academico local.
- A busca por titulo e o filtro por categoria agora constam na Specification e no Plan. Os criterios GET podem ser combinados.
- Os seis materiais iniciais relacionam psicoeducacao a experiencias possiveis da vida academica, sem presumir que todos passam pelas mesmas situacoes nem usar linguagem diagnostica ou avaliacao clinica; dados institucionais nao fornecidos continuam fora do escopo.

## FASE 1 — ESTRUTURA

- [x] T001 Criar ambiente do projeto Django e arquivo de dependencias. **Validacao:** Django instalado no ambiente e comando de versao executa sem erro.
- [x] T002 Criar o projeto Django `projeto` e as aplicacoes `conteudos` e `checkin`. **Validacao:** `manage.py` reconhece ambas as aplicacoes.
- [x] T003 Registrar as aplicacoes e configurar settings essenciais do projeto. **Validacao:** verificacao de configuracao do Django nao aponta erro.
- [x] T004 Configurar descoberta de templates compartilhados e por aplicacao. **Validacao:** a pagina inicial renderiza um template em `templates/`.
- [x] T005 Configurar arquivos estaticos e a pasta `static/`. **Validacao:** `css/estilo.css` e encontrado pelo mecanismo static do Django.
- [x] T006 Configurar SQLite como banco de desenvolvimento. **Validacao:** conexao ao banco e migrations internas iniciais funcionam.
- [x] T007 Configurar a URL raiz, o acesso administrativo e a inclusao das URLconfs dos apps. **Validacao:** `/` renderiza a home e as URLconfs vazias estao incluidas para evolucao futura.
- [x] T008 Criar o template-base minimo e configurar Bootstrap 5, Bootstrap Icons e Google Fonts via CDN. **Validacao:** recursos carregam no navegador e fontes de fallback estao definidas.

## FASE 2 — MODELOS

- [x] T009 Criar o modelo `Categoria` com nome unico e identificador de URL. **Validacao:** modelo aparece no app `conteudos` e passa na verificacao do Django.
- [x] T010 Criar o modelo `Conteudo` com titulo, resumo, texto, categoria, data de publicacao e estado ativo. **Validacao:** campos correspondem ao Plan e `ativo` inicia desativado.
- [x] T011 Configurar ForeignKey de `Conteudo` para `Categoria` com `related_name="conteudos"` e exclusao protegida. **Validacao:** relacionamento permite consultar conteudos pela categoria e impede apagar categoria em uso.
- [x] T012 Gerar migration inicial do app `conteudos`. **Validacao:** arquivo de migration descreve os dois modelos e a relacao.
- [x] T013 Aplicar migrations no SQLite. **Validacao:** migracoes pendentes do projeto sao aplicadas sem erro.
- [x] T014 Configurar `Categoria` no Django Admin. **Validacao:** administrador consegue criar, editar e listar categorias.
- [x] T015 Configurar `Conteudo` no Django Admin com busca, filtros e campos editoriais. **Validacao:** administrador consegue editar todos os campos previstos e localizar conteudos.
- [x] T016 Inserir as seis categorias tematicas iniciais. **Validacao:** Ansiedade, Estresse, Sono e saude mental, Saude mental nos estudos, Autocuidado e Busca de ajuda aparecem no Admin.
- [x] T017 Inserir os seis conteudos educativos iniciais contextualizados para a vida academica. **Validacao:** cada tema possui titulo, resumo, texto, categoria e aparece na listagem publica sem generalizar a experiencia estudantil.

## FASE 3 — INTERFACE BASE

- [x] T018 Completar `templates/base.html` com estrutura HTML semantica e blocos de conteudo. **Validacao:** pagina inicial estende a base sem duplicar a estrutura comum.
- [x] T019 Criar navbar responsiva com links para Inicio, Meu check-in, Conteudos e Acolhimento. **Validacao:** links levam as secoes correspondentes em desktop e celular.
- [x] T020 Criar rodape compartilhado com aviso informativo e de nao substituicao profissional. **Validacao:** aviso aparece nas paginas publicas.
- [x] T021 Definir tokens CSS para cores, tipografia, espacamento, bordas e sombras. **Validacao:** variaveis estao em `static/css/estilo.css` e sao usadas pelos componentes.
- [x] T022 Criar a identidade visual propria em `static/css/estilo.css`. **Validacao:** estilo complementar ao Bootstrap e aplicado na pagina inicial.
- [x] T023 Ajustar a base para larguras de celular, tablet e computador. **Validacao:** navbar e conteudo nao apresentam rolagem horizontal indevida nas larguras testadas.

## FASE 4 — PAGINA INICIAL

- [x] T024 Criar a view e o template da pagina inicial. **Validacao:** `/` apresenta resposta renderizada usando `base.html`.
- [x] T025 Criar a secao principal (hero) com nome Katharsis e mensagem sobre bem-estar na jornada academica. **Validacao:** texto nao presume vivencias iguais nem promete diagnostico, tratamento ou resultado clinico.
- [x] T026 Criar a chamada visual para Meu check-in. **Validacao:** acao leva a secao de autopercepcao na home; formulario fica para fase futura.
- [x] T027 Criar acesso visual a Conteudos na pagina inicial. **Validacao:** acao leva a secao introdutoria de conteudos; listagem fica para fase futura.
- [x] T028 Criar acesso visual a Acolhimento na pagina inicial. **Validacao:** acao leva a secao introdutoria de acolhimento; pagina completa fica para fase futura.
- [x] T029 Criar secao introdutoria sobre finalidade informativa e preventiva e limites do sistema. **Validacao:** secao informa que o sistema nao realiza diagnostico nem substitui atendimento profissional.

## FASE 5 — CHECK-IN

- [x] T030 Criar modelo anonimo `RegistroCheckIn` e migration. **Validacao:** tabela salva percepcao, observacao opcional e data sem vinculo a estudante.
- [x] T031 Criar formulario com as cinco opcoes fixas. **Validacao:** exatamente Muito bem, Bem, Neutro, Preocupado e Sobrecarregado sao exibidas e selecionaveis por teclado.
- [x] T032 Validar no servidor que a opcao enviada pertence a lista permitida. **Validacao:** valor permitido e aceito e valor arbitrario e rejeitado sem erro interno.
- [x] T033 Adicionar campo opcional de observacao com limite de 500 caracteres. **Validacao:** formulario aceita observacao vazia e rejeita texto acima do limite.
- [x] T034 Salvar cada envio valido sem identificacao pessoal. **Validacao:** registro aparece no SQLite com percepcao, observacao e data, sem conta ou identificador de estudante.
- [x] T035 Apresentar confirmacao amigavel apos salvamento usando redirecionamento. **Validacao:** mensagem aparece apos POST valido e recarregar a pagina nao duplica o envio.
- [x] T036 Garantir que o fluxo nao gere diagnostico, pontuacao, classificacao, alerta ou conclusao clinica. **Validacao:** texto e comportamento limitam o registro a autopercepcao.

## FASE 6 — CONTEUDOS

- [x] T037 Criar view e template para listar somente conteudos ativos. **Validacao:** conteudos inativos nao aparecem na resposta publica.
- [x] T038 Criar cards de conteudo com titulo, resumo, categoria e botao Ler conteudo. **Validacao:** cada card apresenta os campos e o link correto.
- [x] T039 Adicionar busca por titulo. **Validacao:** termo correspondente reduz a lista e termo sem correspondencia mostra estado vazio compreensivel.
- [x] T040 Adicionar filtro de conteudos por categoria combinavel com a busca. **Validacao:** selecionar categoria mostra somente conteudos ativos associados a ela.
- [x] T041 Criar view e template de detalhe de conteudo ativo. **Validacao:** detalhe apresenta titulo, categoria, data, texto e botao voltar.
- [x] T042 Restringir acesso publico a detalhes inativos ou inexistentes. **Validacao:** ambos retornam pagina de nao encontrado sem revelar o conteudo.
- [x] T043 Adicionar estado vazio para listagem sem conteudos, busca sem resultado ou filtro sem correspondencia. **Validacao:** pagina permanece utilizavel e explica que nenhum conteudo foi encontrado.

## FASE 7 — ACOLHIMENTO

- [x] T044 Criar view e template da pagina de acolhimento. **Validacao:** `/acolhimento/` abre dentro da base compartilhada.
- [x] T045 Escrever secao geral sobre quando considerar procurar apoio. **Validacao:** texto menciona dificuldades que interferem no cotidiano, sem diagnosticar.
- [x] T046 Criar estrutura visual extensivel para informacoes institucionais futuras. **Validacao:** estrutura pode receber dados posteriormente e nao exibe dados ficticios ou bloco de contato vazio.
- [x] T047 Revisar a pagina para remover nomes, contatos, servicos ou etapas institucionais nao fornecidos. **Validacao:** pagina contem apenas orientacao geral confirmada.

## FASE 8 — ACESSIBILIDADE E RESPONSIVIDADE

- [x] T048 Revisar contraste de texto, fundos, estados e controles. **Validacao:** combinacoes usadas permanecem legiveis e selecao nao depende apenas de cor.
- [x] T049 Revisar navegacao por teclado e ordem de foco. **Validacao:** links, formulario, filtros e botoes sao alcançaveis e operaveis sem mouse.
- [x] T050 Revisar foco visivel em links e controles. **Validacao:** foco tem indicador perceptivel em todos os componentes interativos.
- [x] T051 Revisar leitura e reflow em celular. **Validacao:** texto e controles cabem sem sobreposicao ou rolagem horizontal nas larguras testadas.
- [x] T052 Revisar tamanho e hierarquia dos textos. **Validacao:** titulos seguem hierarquia semantica e corpo permanece legivel com zoom.
- [x] T053 Revisar botoes, links e icones. **Validacao:** acoes tem rotulos claros e icones informativos possuem nome acessivel.
- [x] T054 Revisar alternativas textuais de imagens. **Validacao:** imagens informativas tem texto alternativo e decorativas nao geram ruido para leitor de tela.

## FASE 9 — TESTES MANUAIS

Executar cada cenario manualmente em navegador. Nao criar testes automatizados.

- [x] T055 **Abertura do sistema** — **Cenario:** estudante acessa o sistema pela primeira vez. **Acao:** abrir `/`. **Resultado esperado:** inicio carrega com Katharsis, finalidade informativa e sem erro visivel.
- [x] T056 **Navegacao** — **Cenario:** estudante percorre as areas principais. **Acao:** usar navbar e chamadas da pagina inicial. **Resultado esperado:** Inicio, Meu check-in, Conteudos e Acolhimento abrem suas rotas corretamente.
- [x] T057 **Check-in** — **Cenario:** estudante registra uma percepcao. **Acao:** enviar individualmente cada uma das cinco opcoes. **Resultado esperado:** cada opcao valida e recebe confirmacao neutra, sem diagnostico, pontuacao ou recomendacao.
- [x] T058 **Salvamento e privacidade** — **Cenario:** estudante envia check-in. **Acao:** submeter uma opcao com e sem observacao e inspecionar o SQLite. **Resultado esperado:** percepcao, observacao opcional e data sao salvas sem nome, conta ou identificador pessoal, e nao ha historico publico.
- [x] T059 **Conteudos** — **Cenario:** estudante consulta a lista. **Acao:** abrir `/conteudos/`. **Resultado esperado:** os seis materiais ativos aparecem com titulo, resumo, categoria e acesso a leitura.
- [x] T060 **Busca** — **Cenario:** estudante procura um material. **Acao:** buscar titulo existente e inexistente. **Resultado esperado:** lista corresponde ao titulo ou mostra estado vazio.
- [x] T061 **Filtro** — **Cenario:** estudante quer consultar uma categoria. **Acao:** aplicar um filtro e combina-lo com uma busca. **Resultado esperado:** lista contem somente os itens ativos correspondentes.
- [x] T062 **Leitura** — **Cenario:** estudante abre um material. **Acao:** acessar detalhe a partir de um card. **Resultado esperado:** detalhe apresenta titulo, categoria, data, texto e botao de retorno.
- [x] T063 **Acolhimento** — **Cenario:** estudante busca orientacao inicial. **Acao:** abrir a pagina e revisar o texto. **Resultado esperado:** orientacao geral explica quando considerar apoio e nao inventa dados institucionais.
- [x] T064 **Responsividade** — **Cenario:** estudante usa dispositivos de tamanhos distintos. **Acao:** abrir paginas principais em celular, tablet e computador. **Resultado esperado:** layout, navegacao e controles permanecem utilizaveis sem sobreposicao.
- [x] T065 **Acessibilidade** — **Cenario:** estudante navega sem mouse e amplia o conteudo. **Acao:** usar teclado, zoom e leitor de tela quando disponivel. **Resultado esperado:** foco visivel, rotulos compreensiveis, ordem coerente e conteudo legivel.
- [x] T066 **Responsabilidade** — **Cenario:** estudante le as paginas e materiais. **Acao:** revisar os textos publicos. **Resultado esperado:** finalidade informativa/preventiva e limites de diagnostico e substituicao profissional estao claros.
