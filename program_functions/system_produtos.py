import customtkinter as ctk
from tkinter import Listbox
from program_functions.system_dados import produtos


def abrir_produtos(menuWindow):

    menuWindow.withdraw()

    janela_produtos = ctk.CTkToplevel()
    janela_produtos.title("3xM System - Produtos")
    janela_produtos.state("zoomed")

    produto_selecionado = None

    def atualizar_lista():

        lista_produtos.delete(0, "end")

        for produto in produtos:
            texto = f"{produto['codigo']} | {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}"
            lista_produtos.insert("end", texto)

    def cadastrar():

        nome = entry_nome.get()
        codigo = entry_codigo.get()
        preco = entry_preco.get()
        estoque = entry_estoque.get()

        if nome == "" or codigo == "":
            return

        produto = {
            "nome": nome,
            "codigo": codigo,
            "preco": preco,
            "estoque": estoque
        }

        produtos.append(produto)

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

    def editar():

        nonlocal produto_selecionado

        if produto_selecionado is None:
            return

        produtos[produto_selecionado]["nome"] = entry_nome.get()
        produtos[produto_selecionado]["codigo"] = entry_codigo.get()
        produtos[produto_selecionado]["preco"] = entry_preco.get()
        produtos[produto_selecionado]["estoque"] = entry_estoque.get()

        atualizar_lista()

    def excluir():

        nonlocal produto_selecionado

        if produto_selecionado is None:
            return

        produtos.pop(produto_selecionado)

        produto_selecionado = None

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

    def selecionar_produto(event):

        nonlocal produto_selecionado

        selecionado = lista_produtos.curselection()

        if not selecionado:
            return

        produto_selecionado = selecionado[0]

        produto = produtos[produto_selecionado]

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

        entry_nome.insert(0, produto["nome"])
        entry_codigo.insert(0, produto["codigo"])
        entry_preco.insert(0, produto["preco"])
        entry_estoque.insert(0, produto["estoque"])

    container = ctk.CTkFrame(janela_produtos, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ctk.CTkLabel(
        container,
        text="📦 Cadastro de Produtos",
        font=("Segoe UI", 28, "bold")
    )
    titulo.pack(pady=20)

    frame_form = ctk.CTkFrame(container)
    frame_form.pack(fill="x", padx=50, pady=10)

    entry_nome = ctk.CTkEntry(frame_form, placeholder_text="Nome do Produto", width=250, height=40)
    entry_nome.pack(side="left", padx=10, pady=10)

    entry_codigo = ctk.CTkEntry(frame_form, placeholder_text="Código", width=150, height=40)
    entry_codigo.pack(side="left", padx=10)

    entry_preco = ctk.CTkEntry(frame_form, placeholder_text="Preço", width=150, height=40)
    entry_preco.pack(side="left", padx=10)

    entry_estoque = ctk.CTkEntry(frame_form, placeholder_text="Estoque", width=120, height=40)
    entry_estoque.pack(side="left", padx=10)

    botao_cadastrar = ctk.CTkButton(
        frame_form,
        text="Cadastrar",
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold"),
        command=cadastrar
    )
    botao_cadastrar.pack(side="left", padx=10)

    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(fill="both", expand=True, padx=50, pady=20)

    label_lista = ctk.CTkLabel(
        frame_lista,
        text="Produtos Cadastrados",
        font=("Segoe UI", 18, "bold")
    )
    label_lista.pack(pady=10)

    lista_produtos = Listbox(
        frame_lista,
        height=12,
        font=("Segoe UI", 13)
    )
    lista_produtos.pack(fill="both", padx=20, pady=10)

    lista_produtos.bind("<ButtonRelease-1>", selecionar_produto)

    atualizar_lista()

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_editar = ctk.CTkButton(frame_botoes, text="Editar", width=150, height=40, command=editar)
    botao_editar.pack(side="left", padx=10)

    botao_excluir = ctk.CTkButton(
        frame_botoes,
        text="Excluir",
        width=150,
        height=40,
        fg_color="#E53935",
        hover_color="#C62828",
        command=excluir
    )
    botao_excluir.pack(side="left", padx=10)

    botao_voltar = ctk.CTkButton(
        frame_botoes,
        text="Voltar",
        width=150,
        height=40,
        command=lambda: voltar(janela_produtos, menuWindow)
    )
    botao_voltar.pack(side="left", padx=10)


def voltar(janela, janela_principal):
    janela.destroy()
    janela_principal.deiconify()
    janela_principal.state("zoomed")