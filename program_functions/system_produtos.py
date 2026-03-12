import customtkinter as ctk
from tkinter import Listbox
from connection_bd.sql_bd import conectar_bancodedados


def abrir_produtos(menuWindow):

    menuWindow.withdraw()

    janela_produtos = ctk.CTkToplevel()
    janela_produtos.title("3xM System - Produtos")
    janela_produtos.state("zoomed")

    produto_selecionado = None

    # ----------------------------
    # CARREGAR PRODUTOS DO BANCO
    # ----------------------------

    def carregar_produtos():

        conn = conectar_bancodedados()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM produtos")

        dados = cursor.fetchall()

        conn.close()

        return dados

    # ----------------------------
    # ATUALIZAR LISTA
    # ----------------------------

    def atualizar_lista():

        lista_produtos.delete(0, "end")

        produtos = carregar_produtos()

        for produto in produtos:

            texto = f"{produto['codigo']} | {produto['nome']} | R$ {produto['preco']} | Estoque: {produto['estoque']}"

            lista_produtos.insert("end", texto)

    # ----------------------------
    # CADASTRAR
    # ----------------------------

    def cadastrar():

        nome = entry_nome.get()
        codigo = entry_codigo.get()
        preco = entry_preco.get()
        estoque = entry_estoque.get()

        conn = conectar_bancodedados()
        cursor = conn.cursor()

        sql = """
        INSERT INTO produtos (codigo, nome, preco, estoque)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (codigo, nome, preco, estoque))

        conn.commit()
        conn.close()

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

    # ----------------------------
    # EDITAR
    # ----------------------------

    def editar():

        nonlocal produto_selecionado

        if produto_selecionado is None:
            return

        nome = entry_nome.get()
        codigo = entry_codigo.get()
        preco = entry_preco.get()
        estoque = entry_estoque.get()

        conn = conectar_bancodedados()
        cursor = conn.cursor()

        sql = """
        UPDATE produtos
        SET nome=%s, preco=%s, estoque=%s
        WHERE codigo=%s
        """

        cursor.execute(sql, (nome, preco, estoque, codigo))

        conn.commit()
        conn.close()

        atualizar_lista()

    # ----------------------------
    # EXCLUIR
    # ----------------------------

    def excluir():

        nonlocal produto_selecionado

        if produto_selecionado is None:
            return

        codigo = entry_codigo.get()

        conn = conectar_bancodedados()
        cursor = conn.cursor()

        sql = "DELETE FROM produtos WHERE codigo=%s"

        cursor.execute(sql, (codigo,))

        conn.commit()
        conn.close()

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

    # ----------------------------
    # SELECIONAR PRODUTO
    # ----------------------------

    def selecionar_produto(event):

        selecionado = lista_produtos.curselection()

        if not selecionado:
            return

        texto = lista_produtos.get(selecionado)

        dados = texto.split("|")

        codigo = dados[0].strip()
        nome = dados[1].strip()
        preco = dados[2].replace("R$", "").strip()
        estoque = dados[3].replace("Estoque:", "").strip()

        entry_nome.delete(0, "end")
        entry_codigo.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_estoque.delete(0, "end")

        entry_nome.insert(0, nome)
        entry_codigo.insert(0, codigo)
        entry_preco.insert(0, preco)
        entry_estoque.insert(0, estoque)

    # ----------------------------
    # INTERFACE
    # ----------------------------

    container = ctk.CTkFrame(janela_produtos, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ctk.CTkLabel(container, text="📦 Cadastro de Produtos", font=("Segoe UI", 28, "bold"))
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

    botao_cadastrar = ctk.CTkButton(frame_form, text="Cadastrar", width=140, height=40, command=cadastrar)
    botao_cadastrar.pack(side="left", padx=10)

    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(fill="both", expand=True, padx=50, pady=20)

    lista_produtos = Listbox(frame_lista, height=12, font=("Segoe UI", 13))
    lista_produtos.pack(fill="both", padx=20, pady=10)

    lista_produtos.bind("<ButtonRelease-1>", selecionar_produto)

    atualizar_lista()

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_editar = ctk.CTkButton(frame_botoes, text="Editar", width=150, height=40, command=editar)
    botao_editar.pack(side="left", padx=10)

    botao_excluir = ctk.CTkButton(frame_botoes, text="Excluir", width=150, height=40, command=excluir)
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