# GastoCerto 💰

## Descrição do Problema
Muitas pessoas têm dificuldade em controlar seus gastos pessoais no dia a dia, o que leva ao endividamento e à falta de planejamento financeiro. Essa realidade afeta especialmente jovens e pessoas de baixa renda.

## Proposta da Solução
O GastoCerto é uma aplicação CLI simples que permite registrar, listar, visualizar e remover gastos pessoais de forma rápida e organizada, ajudando o usuário a ter consciência dos seus gastos.

## Público-alvo
Qualquer pessoa que queira organizar suas finanças pessoais de forma simples, sem precisar de aplicativos complexos.

## Funcionalidades
- Adicionar gastos com descrição, valor e categoria
- Listar todos os gastos registrados
- Ver o total gasto
- Remover gastos

## Tecnologias Utilizadas
- Python 3.10+
- pytest (testes automatizados)
- ruff (linting)
- GitHub Actions (CI)

## Instalação
```bash
git clone https://github.com/danielzinrx/gastocerto.git
cd gastocerto
pip install -r requirements.txt
```

## Execução
```bash
python src/gastocerto.py
```

## Rodando os Testes
```bash
pytest tests/
```

## Rodando o Lint
```bash
ruff check src/
```

## Versão
1.0.0

## Autor
Daniel Carlos Delfino dos Santos

## Repositório
https://github.com/danielzinrx/gastocerto