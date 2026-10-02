# Plano tecnico: Katharsis

## Resumo

Aplicacao web server-rendered em Python e Django, organizada segundo MVT. SQLite armazenara categorias, conteudos educativos e registros de check-in sem vinculo a contas de estudantes. O check-in salva somente percepcao, observacao opcional e data; nao oferece historico individual nem interpretacao clinica. As paginas publicas nao terao cadastro nem login; o Django Admin ficara restrito a manutencao por administradores autorizados.

## Decisoes tecnicas

| Tema | Decisao |
| --- | --- |
| Linguagem e framework | Python com Django, usando views, models, templates e URLs do framework (MVT). |
| Banco de dados | SQLite para o MVP academico. |
| Conteudo | Categorias e conteudos persistidos no banco, mantidos pelo Django Admin e apresentados publicamente quando ativos. |
| Check-in | Model e ModelForm Django com opcoes fixas; validar no POST e salvar percepcao, observacao opcional e data sem associar estudante ou conta. |
| Acesso | Paginas publicas sem autenticacao. Autenticacao do Django Admin apenas para administradores; sem cadastro de estudantes. |
| Interface | HTML e CSS; JavaScript apenas quando necessario. Bootstrap 5, Bootstrap Icons e Google Fonts via CDN, complementados por estilos proprios. |
| Validacao | Cenários manuais documentados abaixo; nao criar testes automatizados. |

O salvamento anonimo e a observacao opcional atendem ao pedido atual e substituem a decisao anterior de manter o check-in transitorio. Nao ha historico individual, identificacao, analise, interpretacao clinica ou uso dos registros fora do salvamento. O periodo de retencao e o processo de descarte ainda nao foram definidos; essa decisao e necessaria antes da publicacao fora do ambiente academico local.

## Arquitetura e organizacao

```text
Katharsis/
├── manage.py
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── conteudos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── checkin/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── checkin/
│   ├── conteudos/
│   └── acolhimento/
└── static/
    └── css/
        └── estilo.css
```

- `projeto/urls.py` inclui as rotas das aplicacoes e a pagina inicial.
- `conteudos` contem modelos, migration dos seis materiais iniciais, consultas, views, rotas e configuracao administrativa de categorias e materiais. A listagem oferece busca por titulo e filtro combinavel por categoria.
- `checkin` contem o modelo anonimo de registro, o formulario, a view GET/POST e a rota do check-in.
- `templates/base.html` define estrutura comum, navbar, rodape, links CDN e mensagens de responsabilidade. As demais paginas estendem essa base.
- `static/css/estilo.css` define tokens CSS para cores, tipografia, espacamento, bordas e sombras, alem dos ajustes responsivos e de foco. Bootstrap complementa, mas nao determina sozinho a identidade visual.
- A area de acolhimento sera uma pagina informativa em template, sem app ou cadastro de instituicoes ate que os dados sejam fornecidos.

## Modelagem

### Categoria

- `nome`: texto curto, obrigatorio e unico.
- `slug`: identificador para URLs, unico.
- Opcionalmente, `descricao` curta para contextualizar a categoria.

### Conteudo

- `titulo`: texto curto, obrigatorio.
- `resumo`: texto, obrigatorio.
- `texto`: corpo educativo, obrigatorio.
- `categoria`: ForeignKey obrigatoria para `Categoria`, com `related_name="conteudos"` e exclusao protegida enquanto houver conteudos associados.
- `data_publicacao`: data e hora de publicacao.
- `ativo`: BooleanField, inativo por padrao; a publicacao exige ativacao deliberada apos revisao editorial.

A listagem publica consulta somente conteudos ativos e permite busca por titulo e filtro por categoria. O detalhe tambem deve retornar nao encontrado para um conteudo inativo, mesmo que seu identificador seja conhecido. Uma migration de dados cria os seis temas e materiais iniciais ativos. Os textos devem relacionar os temas a vida academica, sem universalizar experiencias, usar linguagem diagnostica ou representar avaliacao clinica.

Toda alteracao de schema gera migration Django versionada. As migrations criam os modelos de conteudo e de check-in. Nenhum dado institucional sera semeado sem fonte confirmada.

### RegistroCheckIn

- `percepcao`: uma das cinco opcoes fixas da especificacao.
- `observacao`: texto opcional limitado a 500 caracteres.
- `criado_em`: data e hora de criacao automatica.
- Nao possui ForeignKey para estudante, usuario ou sessao.

Os registros ficam no SQLite sem interface publica para consultar historico. A politica de retencao e descarte permanece pendente.

## Rotas e comportamento das paginas

| Rota sugerida | Pagina / comportamento |
| --- | --- |
| `/` | Inicio com apresentacao do Katharsis e acessos ao check-in, conteudos e acolhimento. |
| `/checkin/` | GET apresenta as cinco opcoes e observacao opcional; POST valida, salva sem identificacao e redireciona para confirmacao. |
| `/conteudos/?q=<titulo>&categoria=<slug>` | Lista de conteudos ativos com busca por titulo e filtro opcional por categoria. Os parametros podem ser combinados. |
| `/conteudos/<int:pk>/` | Detalhe de um conteudo ativo, com titulo, categoria, data, texto e acao para voltar a listagem. |
| `/acolhimento/` | Orientacao geral sobre considerar apoio quando dificuldades interferem no cotidiano. |
| `/admin/` | Django Admin para administradores autenticados, com gestao de Categoria e Conteudo. |

O formulario de check-in usa protecao CSRF do Django, valida os valores no servidor e limita a observacao a 500 caracteres. A confirmacao deve dizer que o registro foi salvo e reforcar que e apenas autopercepcao. A view nao interpreta os valores nem os envia para analytics ou servicos externos. Nao havera pagina de historico.

## Administracao de conteudo

Configurar o Django Admin para:

- listar categorias e conteudos com colunas uteis, filtros por categoria e estado ativo e busca por titulo;
- editar titulo, resumo, texto, categoria, data de publicacao e estado ativo;
- mostrar a categoria nos formularios de conteudo;
- exigir autenticacao administrativa normal do Django, sem expor autenticacao ou criacao de conta ao publico estudantil.

A publicacao inicial requer inserir e revisar manualmente os textos educativos. Contatos, servicos, nomes de profissionais e fluxos institucionais nao devem ser cadastrados ate serem oficialmente fornecidos.

## Interface e acessibilidade

- Navbar responsiva com links textuais para Inicio, Meu check-in, Conteudos e Acolhimento; indicador claro da pagina atual.
- Paginas estendem `base.html`, com um unico titulo principal `h1` e hierarquia semantica subsequente.
- As opcoes do check-in devem ser controles de formulario nativos, associados a labels e operaveis por teclado; nao depender apenas de cor ou icone para comunicar selecao.
- Botoes e links devem ter nomes claros, ordem de foco previsivel e foco visivel. Icones decorativos sao ocultados de leitores de tela; icones com significado recebem nome acessivel.
- Imagens informativas recebem texto alternativo; imagens decorativas usam alternativa vazia.
- Verificar contraste de texto e componentes, tamanho legivel, zoom e reflow em larguras de celular, tablet e computador.
- Bootstrap 5, Bootstrap Icons e Google Fonts sao carregados via CDN conforme solicitado. Usar versoes estaveis fixadas, atributos de integridade quando suportados e fontes de fallback. As requisicoes a CDNs podem expor metadados de conexao aos respectivos provedores; nao adicionar trackers ou scripts de analise.

## Seguranca e privacidade

- Armazenar somente percepcao, observacao opcional e data do check-in; nao armazenar identificadores de estudante, nome, matricula, CPF ou e-mail.
- Nao disponibilizar historico individual nem usar registros de check-in para analise ou perfil.
- Nao pedir nome, matricula, CPF, e-mail, identificador ou criacao de conta para estudantes.
- Manter CSRF ativo nos formularios POST e escapar conteudo renderizado pelos templates Django.
- Restringir o Django Admin a contas administrativas criadas para manutencao; credenciais administrativas nao fazem parte da interface publica.
- Usar configuracoes Django adequadas ao ambiente e nao deixar `DEBUG` habilitado em publicacao. Nao incluir segredos no repositorio.
- Nao usar dados do check-in para diagnostico, pontuacao, triagem, perfil ou recomendacao individual.

## Plano de implementacao

1. Criar projeto Django `projeto` e apps `conteudos` e `checkin`; configurar templates, arquivos estaticos, SQLite e URLs.
2. Implementar `Categoria` e `Conteudo`, gerar e aplicar migrations, configurar Django Admin e inserir os seis materiais educativos iniciais.
3. Criar templates compartilhados, navbar, rodape, pagina inicial e CSS com variaveis de design e comportamento responsivo.
4. Implementar listagem de conteudos ativos, busca por titulo, filtro por categoria e detalhe; contextualizar os seis materiais na vida academica com linguagem introdutoria, inclusiva e informativa.
5. Implementar check-in anonimo com validacao de opcoes, CSRF, observacao opcional, persistencia e confirmacao.
6. Implementar pagina de acolhimento com texto geral e sem contatos ou fluxo institucional nao fornecidos.
7. Executar os cenarios de validacao manual, corrigir problemas observados e registrar o resultado da revisao humana.

## Cenarios de validacao manual

1. **Inicio e navegacao:** abrir `/` e verificar nome, finalidade informativa/preventiva, acessos as quatro areas e funcionamento dos links.
2. **Check-in valido:** escolher cada uma das cinco opcoes e enviar, com e sem observacao. Confirmar persistencia dos campos permitidos, resposta de sucesso e ausencia de diagnostico, pontuacao ou recomendacao clinica.
3. **Check-in invalido:** enviar valor fora das opcoes permitidas. Confirmar rejeicao sem gravacao e sem erro interno exposto.
4. **Privacidade do check-in:** enviar uma opcao, consultar o schema SQLite e os registros. Confirmar que somente percepcao, observacao opcional e data foram salvas, sem identificador pessoal ou historico publico.
5. **Conteudos:** verificar os seis materiais iniciais, buscar por titulo, filtrar por categoria, combinar criterios e abrir um detalhe com titulo, categoria, data, texto e acao de retorno.
6. **Estado de publicacao:** marcar conteudo como inativo. Confirmar que desaparece da listagem e que seu detalhe nao fica acessivel publicamente.
7. **Estado vazio:** buscar um titulo sem correspondencia. Confirmar que a pagina apresenta uma mensagem clara e permite limpar os filtros.
8. **Acolhimento:** verificar orientacao geral e confirmar que nao ha nomes, contatos, servicos ou etapas inventados.
9. **Admin:** confirmar que administradores conseguem manter categorias e conteudos e que a interface publica nao oferece cadastro ou login de estudante.
10. **Responsividade e acessibilidade:** testar tamanhos de celular, tablet e computador, navegacao apenas por teclado, foco visivel, ampliacao de texto, contraste, labels de formulario, hierarquia de titulos e nomes acessiveis dos controles.
11. **Responsabilidade:** revisar textos de todas as paginas e materiais para confirmar finalidade informativa/preventiva, ausencia de promessa clinica e aviso de que o sistema nao substitui profissionais ou servicos especializados.

Os cenarios acima sao executados por revisao humana; nao devem ser convertidos em testes automatizados neste projeto.

## Fora do plano

Nao fazem parte deste MVP: historico individual de check-ins, contas de estudantes, rede social, chat, IA psicologica, diagnostico, questionarios clinicos, agendamento, prontuario, cadastro de profissionais, notificacoes complexas ou informacoes institucionais nao fornecidas.
