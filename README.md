# Calculadora com Interface Gráfica (INE5201)

**Disciplina:** INE5201 / UFSC

**Aluno:** Vinicius Andreani

## Funcionalidades

- **Operações Básicas**: Adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`).
- **Suporte a Decimais**: Controle de ponto decimal (`.`) impedindo múltiplos pontos no mesmo número.
- **Controles de Edição**: Botão `C` para limpar todo o display e botão `⌫` (backspace) para apagar o último caractere.
- **Histórico de Cálculos**: Painel lateral exibindo os cálculos recentes (mínimo de 5 registros) com botão dedicado para limpar o histórico.
- **Tratamento de Erros e Validações**:
  - Exibição de `"Erro: Divisão por zero"` ao tentar dividir por zero.
  - Exibição de `"Erro: Expressão inválida"` para expressões incompletas ou malformadas.
  - Bloqueio de múltiplos operadores consecutivos.
  - Limite máximo de caracteres no display para evitar *overflow*.

## Como Executar

1. Certifique-se de ter o **Python 3** instalado (a biblioteca `tkinter` já acompanha a instalação padrão).
2. Clone este repositório:
   ```bash
   python calculadora_gui.py
