# Projeto-Ferias

Estou aprendendo a usar o GitHub e resolvi criar esse repositório para documentar esse projeto.

O projeto tem o objetivo de servir como uma agenda de treinos de musculação, rodando localmente via terminal, em Python.

## Opções disponíveis no menu

```
[1] - Registrar um treino (criar a divisão dos treinos)
[2] - Adicionar um treino (lançar séries, cargas e repetições)
[3] - Consultar os dados de treino
[4] - Listar exercícios registrados
[0] - Sair do programa
```

## Estrutura de dados

Os dados de treino ficam organizados em um dicionário aninhado, no formato:

```python
registro_de_treino = {
    "TIPO_DE_TREINO": {
        "NOME_DO_EXERCICIO": [
            {"série": 1, "carga": 40.0, "reps": 10},
            {"série": 2, "carga": 42.5, "reps": 8}
        ]
    }
}
```

Existe também um dicionário auxiliar `exercicios_registrados`, que mapeia cada tipo de treino para a lista de nomes de exercícios cadastrados nele — usado para exibir opções ao usuário sem precisar percorrer a estrutura completa.

## Funções principais

- `limpar_tela()` — limpa o terminal.
- `pausar_execucao()` — segura a tela até o usuário apertar Enter, evitando que mensagens desapareçam antes de serem lidas.
- `registrar_treino()` — fluxo de criação da divisão de treino e dos exercícios de cada dia.
- `adicionar_treino(...)` — fluxo de lançamento de séries/carga/reps para um exercício já registrado.
- `mostrar_tipos_de_treino(...)` / `escolher_tipo_de_treino(...)` — exibem os tipos de treino cadastrados e capturam a escolha do usuário, com validação.
- `mostrar_exercicios_registrados(...)` / `escolher_exercicio(...)` — mesma lógica, aplicada aos exercícios de um tipo de treino.
- `mostrar_treinos_registrados(...)` — exibe o conteúdo completo do treino registrado.

## Status do projeto

**Em desenvolvimento.** Feito até agora:

- Fluxo completo de registrar treino → adicionar sessão → consultar dados, tudo em memória (sem persistência ainda).
- Validação de entradas numéricas no menu principal e no registro do treino.
- Estrutura de dados revisada para usar lista de dicionários por série, evitando dados paralelos dessincronizados.

Ainda pendente / próximos passos:

- Persistência dos dados em arquivo (CSV ou JSON), para não perder o progresso ao fechar o programa.
- Edição e remoção de séries, exercícios e tipos de treino.
- Consultas específicas: última carga registrada, maior/menor carga de um exercício, volume total de um treino.
- Bloqueio de nomes duplicados de tipo de treino/exercício.
- Resumo geral do treino (contagem de tipos, exercícios e séries registradas).
- Versão com gráficos de evolução de carga (Matplotlib) e análise com Pandas/NumPy.
- Futuramente: reescrita do projeto usando Programação Orientada a Objetos.

## Como rodar

```bash
python main.py
```

Requer apenas Python padrão (nenhuma biblioteca externa é usada na versão atual).