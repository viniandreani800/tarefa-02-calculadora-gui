import tkinter as tk

MAX_CARACTERES = 18
OPERADORES = {"+", "-", "*", "/"}


def atualizar_display(display, novo_texto):
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, novo_texto)
    display.config(state="readonly")


def tratar_erro(display, mensagem):
    atualizar_display(display, mensagem)


def calcular(expressao):
    if not expressao or expressao[-1] in OPERADORES:
        raise ValueError("Expressão incompleta")

    # Validação de caracteres permitidos antes de avaliar
    caracteres_validos = set("0123456789.+-*/")
    if any(ch not in caracteres_validos for ch in expressao):
        raise ValueError("Caracteres inválidos")

    try:
        resultado = eval(expressao)
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero")
    except Exception:
        raise ValueError("Expressão inválida")

    # Formata para remover '.0' desnecessário em resultados inteiros
    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))

    return str(round(resultado, 10))


def ao_clicar_botao(display, texto):
    atual = display.get()

    if atual.startswith("Erro:"):
        atual = ""

    if texto == "C":
        atualizar_display(display, "")
        return

    if texto == "⌫":
        atualizar_display(display, atual[:-1])
        return

    if texto == "=":
        if not atual:
            return
        try:
            resultado = calcular(atual)
            atualizar_display(display, resultado)
        except ZeroDivisionError:
            tratar_erro(display, "Erro: Divisão por zero")
        except ValueError:
            tratar_erro(display, "Erro: Expressão inválida")
        return

    if len(atual) >= MAX_CARACTERES:
        return

    if texto in OPERADORES:
        if not atual:
            if texto == "-":
                atualizar_display(display, texto)
            return
        if atual[-1] in OPERADORES:
            atualizar_display(display, atual[:-1] + texto)
            return

    if texto == ".":
        partes = atual.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()
        ultimo_numero = partes[-1] if partes else ""
        if "." in ultimo_numero:
            return
        if not ultimo_numero or atual[-1] in OPERADORES:
            texto = "0."

    atualizar_display(display, atual + texto)


def criar_layout(janela):
    janela.title("Calculadora - INE5201")
    janela.resizable(False, False)
    janela.configure(bg="#1e1e1e")

    display = tk.Entry(
        janela,
        font=("Arial", 22, "bold"),
        bg="#2d2d2d",
        fg="#ffffff",
        bd=0,
        justify="right",
        state="readonly",
        readonlybackground="#2d2d2d",
    )
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=(15, 10), ipady=15, sticky="nsew")

    botoes = [
        ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
        ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
    ]

    for texto, linha, coluna in botoes:
        cor_fundo = "#3b3b3b"
        if texto in OPERADORES:
            cor_fundo = "#ff9500"
        elif texto in {"C", "⌫"}:
            cor_fundo = "#a5a5a5"
        elif texto == "=":
            cor_fundo = "#28a745"

        btn = tk.Button(
            janela,
            text=texto,
            font=("Arial", 16, "bold"),
            bg=cor_fundo,
            fg="#ffffff",
            bd=0,
            width=5,
            height=2,
            activebackground="#555555",
            activeforeground="#ffffff",
            command=lambda t=texto: ao_clicar_botao(display, t),
        )

        colspan = 2 if texto == "=" else 1
        btn.grid(row=linha, column=coluna, columnspan=colspan, padx=4, pady=4, sticky="nsew")

    return display


def main():
    janela = tk.Tk()
    criar_layout(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()