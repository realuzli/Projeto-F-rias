# Diário de Treino 🏋️

Projeto feito em Python, via terminal, pra registrar treinos, exercícios e acompanhar o progresso ao longo do tempo.

## Por que esse projeto?

Gosto de treinar e gosto de programar, então decidi unir as duas coisas. Em vez de anotar os treinos no celular ou no papel, resolvi criar meu próprio sistema pra guardar esses dados — e de quebra, praticar lógica de programação em cima de algo que eu realmente uso no dia a dia.

## Funcionalidades

- **Exercícios:** adicionar, listar, alterar e remover exercícios, organizados por tipo/divisão de treino (ex: Upper, Lower, Push, Pull).
- **Treinos:** adicionar um treino do dia (com carga, repetições, RPE e observação por série), listar o histórico, alterar um registro já feito e remover um treino específico.
- **Persistência de dados:** os dados ficam salvos em arquivos JSON (catálogo de exercícios e histórico de treinos) e também são exportados em CSV, pra facilitar abrir numa planilha e analisar depois.
- **Carregamento automático:** ao abrir o programa, ele já carrega os dados salvos anteriormente; ao sair, salva tudo automaticamente — sem precisar escolher isso manualmente no menu.

## Estrutura do projeto

- `main.py` → menu principal, ponto de entrada do programa.
- `exercicio.py` → funções relacionadas ao cadastro de exercícios.
- `treino.py` → funções relacionadas ao registro dos treinos realizados.
- `arquivo.py` → leitura e escrita dos dados (JSON e CSV).
- `utils.py` → funções auxiliares (limpar tela, pausar execução).

## Como rodar

```bash
python main.py
```

## Próximos passos

Esse projeto ainda tem bastante espaço pra evoluir. Algumas ideias pro futuro:
- Interface gráfica (em vez de tudo pelo terminal).
- Sugestão automática de divisões de treino e exercícios com base no histórico do usuário.
- Cálculo de progresso/evolução de carga e RPE ao longo do tempo.