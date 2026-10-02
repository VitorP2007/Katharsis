# Katharsis

### DESENVOLVIMENTO DE UM SISTEMA WEB DE AUTOMONITORAMENTO EMOCIONAL E ACOLHIMENTO ESTUDANTIL

O **Katharsis** é um projeto acadêmico que propõe uma plataforma web voltada ao bem-estar emocional de estudantes, considerando os desafios presentes na vida acadêmica, como avaliações, trabalhos, prazos, organização dos estudos e adaptação ao ambiente educacional.

A plataforma busca incentivar o autoconhecimento emocional, disponibilizar informações educativas sobre saúde mental e facilitar o acesso às informações sobre o acolhimento psicológico institucional.

## Como foi desenvolvido esse prototipo

O desenvolvimento desse prototipo serve apenas para ilustrur como o sistema será de fato, ainda sem as funcionalidades completas, seguiu uma abordagem Spec-Driven Development (SDD) com o Spec Kit, aplicando as metodologias e conceitos, orientada por especificação: os requisitos foram organizados em planejamento e tarefas, e as funcionalidades foram implementadas e validadas manualmente por etapas. O GitHub Copilot foi utilizado como ferramenta de apoio para elaborar e revisar os artefatos do projeto, auxiliar na implementação e sugerir ajustes; as decisões finais e a validação do sistema permaneceram sob responsabilidade da equipe.

## 🎯 Objetivo do projeto

Desenvolver uma aplicação web que contribua para a promoção do bem-estar emocional no ambiente acadêmico, oferecendo recursos de automonitoramento, psicoeducação e orientação sobre caminhos para buscar apoio institucional.

## ✨ Funcionalidades

- **Check-in emocional:** permite que o estudante registre sua percepção emocional no momento.
- **Conteúdos educativos:** disponibiliza informações sobre saúde mental relacionadas à rotina estudantil.
- **Organização por categorias:** facilita a navegação pelos conteúdos.
- **Página de acolhimento:** apresenta informações sobre como buscar apoio psicológico na instituição.
- **Interface responsiva:** adapta a apresentação do sistema a computadores, tablets e celulares.
- **Painel administrativo:** permite gerenciar os conteúdos educativos, conforme a implementação do projeto.

## 📚 Temas abordados

Os conteúdos da plataforma podem abordar temas como:

- Ansiedade diante de provas e avaliações;
- Estresse acadêmico e sobrecarga de atividades;
- Organização dos estudos e equilíbrio com o descanso;
- Sono e bem-estar emocional;
- Autocuidado durante períodos de maior demanda acadêmica;
- Adaptação à vida estudantil;
- Reconhecimento de momentos em que pode ser importante buscar apoio.

## 🛠️ Tecnologias utilizadas

O projeto está planejado para utilizar as seguintes tecnologias:

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Django | Desenvolvimento do sistema web |
| SQLite | Banco de dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização da interface |
| JavaScript | Interações complementares, quando necessárias |
| Bootstrap 5 | Componentes e responsividade |
| Bootstrap Icons | Ícones da interface |
| Google Fonts | Tipografia |

## 📁 Estrutura prevista do projeto

```text
mente-aberta/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── conteudos/
├── checkin/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── checkin.html
│   ├── lista_conteudos.html
│   ├── detalhe_conteudo.html
│   └── acolhimento.html
├── static/
│   └── css/
│       └── estilo.css
├── requirements.txt
└── README.md
```

*Observação: a estrutura acima é uma referência inicial e poderá ser ajustada durante o desenvolvimento.*

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

Antes de começar, instale:

- Python 3;
- Git;
- Um editor de código, como o Visual Studio Code.

### 2. Clone o repositório

```bash
git clone https://github.com/VitorP2007/Katharsis.git
```

Entre na pasta do projeto:

```bash
cd katharsis
```

### 3. Crie um ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

Caso o arquivo `requirements.txt` já esteja criado:

```bash
pip install -r requirements.txt
```

### 5. Configure o banco de dados

Execute as migrações do Django:

```bash
python manage.py migrate
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

**Importante:** os comandos pressupõem que a estrutura Django e as dependências já tenham sido configuradas no projeto.

## 🔒 Privacidade e limites da plataforma

O sistema tem caráter educativo e preventivo. Seu objetivo é apoiar a percepção emocional dos estudantes e facilitar o acesso a informações sobre acolhimento institucional.

A plataforma não realiza diagnósticos, não substitui acompanhamento psicológico ou atendimento profissional e não deve ser utilizada como ferramenta de avaliação clínica.

O desenvolvimento deve priorizar a privacidade dos usuários e evitar a coleta de dados pessoais desnecessários.

## 🎓 Contexto acadêmico

Este projeto está sendo desenvolvido com finalidade acadêmica, como proposta de uma solução tecnológica voltada ao bem-estar estudantil e ao acolhimento no ambiente educacional.

## 🚧 Status do projeto

Em desenvolvimento.

As funcionalidades e a estrutura poderão ser ajustadas durante as etapas de especificação, planejamento, implementação e validação.

## 👥 Autoria

Projeto acadêmico desenvolvido por:

- **Autor:** Vitor Pizolato da Silva
- **Instituição:** IF Baiano / Campus Guanambi
- **Curso:**  Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
- **Orientador(a):** George Gabriel

---

**Katharsis — Cuidar de você também faz parte da sua jornada acadêmica.**
