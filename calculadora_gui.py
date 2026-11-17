import tkinter as tk

MAX_CARACTERES = 18
MAX_HISTORICO = 5
OPERADORES = {"+", "-", "*", "/"}


def atualizar_display(display, novo_texto):
    # Ajusta o tamanho da fonte se for uma mensagem de erro longa
    if novo_texto.startswith("Erro:"):
        display.config(font=("Arial", 16, "bold"))
    else:
        display.config(font=("Arial", 22, "bold"))

    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, novo_texto)
    display.config(state="readonly")


def tratar_erro(display, mensagem):
    atualizar_display(display, mensagem)


def adicionar_ao_historico(lista_historico, expressao, resultado):
    item = f"{expressao} = {resultado}"
    lista_historico.insert(0, item)

    # Mantém os cálculos mais recentes visíveis (mínimo 5 exigidos)
    if lista_historico.size() > 10:
        lista_historico.delete(10, tk.END)


def limpar_historico(lista_historico):
    lista_historico.delete(0, tk.END)


def calcular(expressao):
    if not expressao or expressao[-1] in OPERADORES:
        raise ValueError("Expressão incompleta")

    caracteres_validos = set("0123456789.+-*/")
    if any(ch not in caracteres_validos for ch in expressao):
        raise ValueError("Caracteres inválidos")

    try:
        resultado = eval(expressao)
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero")
    except Exception:
        raise ValueError("Expressão inválida")

    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))

    return str(round(resultado, 10))


def ao_clicar_botao(display, lista_historico, texto):
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
            adicionar_ao_historico(lista_historico, atual, resultado)
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

    # Frame esquerdo: Calculadora
    frame_calc = tk.Frame(janela, bg="#1e1e1e")
    frame_calc.grid(row=0, column=0, padx=10, pady=10)

    display = tk.Entry(
        frame_calc,
        font=("Arial", 22, "bold"),
        bg="#2d2d2d",
        fg="#ffffff",
        bd=0,
        justify="right",
        state="readonly",
        readonlybackground="#2d2d2d",
    )
    display.grid(row=0, column=0, columnspan=4, padx=4, pady=(5, 10), ipady=15, sticky="nsew")

    # Frame direito: Histórico de Cálculos
    frame_hist = tk.Frame(janela, bg="#252526", padx=10, pady=10)
    frame_hist.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nsew")

    lbl_hist = tk.Label(
        frame_hist,
        text="Histórico Recente",
        font=("Arial", 12, "bold"),
        bg="#252526",
        fg="#ffffff",
    )
    lbl_hist.pack(pady=(0, 8))

    lista_historico = tk.Listbox(
        frame_hist,
        font=("Arial", 11),
        bg="#2d2d2d",
        fg="#e0e0e0",
        bd=0,
        width=22,
        height=12,
        highlightthickness=0,
        selectbackground="#3b3b3b",
    )
    lista_historico.pack(fill="both", expand=True, pady=(0, 8))

    btn_limpar_hist = tk.Button(
        frame_hist,
        text="Limpar Histórico",
        font=("Arial", 10, "bold"),
        bg="#a5a5a5",
        fg="#ffffff",
        bd=0,
        pady=6,
        activebackground="#777777",
        activeforeground="#ffffff",
        command=lambda: limpar_historico(lista_historico),
    )
    btn_limpar_hist.pack(fill="x")

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
            frame_calc,
            text=texto,
            font=("Arial", 16, "bold"),
            bg=cor_fundo,
            fg="#ffffff",
            bd=0,
            width=5,
            height=2,
            activebackground="#555555",
            activeforeground="#ffffff",
            command=lambda t=texto: ao_clicar_botao(display, lista_historico, t),
        )

        colspan = 2 if texto == "=" else 1
        btn.grid(row=linha, column=coluna, columnspan=colspan, padx=4, pady=4, sticky="nsew")

    return display, lista_historico


def main():
    janela = tk.Tk()
    criar_layout(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()