import tkinter as tk


def criar_layout(janela):
    janela.title("Calculadora - INE5201")
    janela.resizable(False, False)
    janela.configure(bg="#1e1e1e")

    # Display da calculadora
    display = tk.Entry(
        janela,
        font=("Arial", 24, "bold"),
        bg="#2d2d2d",
        fg="#ffffff",
        bd=0,
        justify="right",
        state="readonly",
        readonlybackground="#2d2d2d",
    )
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=(15, 10), ipady=15, sticky="nsew")

    # Grade de botões (texto, linha, coluna)
    botoes = [
        ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
        ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
    ]

    for texto, linha, coluna in botoes:
        cor_fundo = "#3b3b3b"
        if texto in {"/", "*", "-", "+"}:
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
        )

        # Faz o botão '=' ocupar 2 colunas para fechar o alinhamento
        colspan = 2 if texto == "=" else 1
        btn.grid(row=linha, column=coluna, columnspan=colspan, padx=4, pady=4, sticky="nsew")

    return display


def main():
    janela = tk.Tk()
    criar_layout(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()