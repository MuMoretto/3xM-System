import customtkinter as ctk
from tkinter import Listbox
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="sistema_3xm"
    )


def abrir_clientes(janela_principal):

    janela_principal.withdraw()

    janela_clientes = ctk.CTkToplevel()
    janela_clientes.title("3xM System - Clientes")
    janela_clientes.state("zoomed")

    cliente_selecionado = None

    conn = conectar()
    cursor = conn.cursor()

    def atualizar_lista():

        lista_clientes.delete(0, "end")

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        for cliente in clientes:
            texto = f"{cliente[1]} | {cliente[2]} | {cliente[3]}"
            lista_clientes.insert("end", texto)

    def cadastrar():

        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        if nome == "":
            return

        sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s,%s,%s)"
        cursor.execute(sql, (nome, telefone, email))
        conn.commit()

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_telefone.delete(0, "end")
        entry_email.delete(0, "end")

    def editar():

        nonlocal cliente_selecionado

        if cliente_selecionado is None:
            return

        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        cursor.execute("SELECT id FROM clientes")
        ids = cursor.fetchall()

        id_cliente = ids[cliente_selecionado][0]

        sql = """
        UPDATE clientes
        SET nome=%s, telefone=%s, email=%s
        WHERE id=%s
        """

        cursor.execute(sql, (nome, telefone, email, id_cliente))
        conn.commit()

        atualizar_lista()

    def excluir():

        nonlocal cliente_selecionado

        if cliente_selecionado is None:
            return

        cursor.execute("SELECT id FROM clientes")
        ids = cursor.fetchall()

        id_cliente = ids[cliente_selecionado][0]

        cursor.execute("DELETE FROM clientes WHERE id=%s", (id_cliente,))
        conn.commit()

        cliente_selecionado = None

        atualizar_lista()

        entry_nome.delete(0, "end")
        entry_telefone.delete(0, "end")
        entry_email.delete(0, "end")

    def selecionar_cliente(event):

        nonlocal cliente_selecionado

        selecionado = lista_clientes.curselection()

        if not selecionado:
            return

        cliente_selecionado = selecionado[0]

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        cliente = clientes[cliente_selecionado]

        entry_nome.delete(0, "end")
        entry_telefone.delete(0, "end")
        entry_email.delete(0, "end")

        entry_nome.insert(0, cliente[1])
        entry_telefone.insert(0, cliente[2])
        entry_email.insert(0, cliente[3])

    def voltar():

        janela_clientes.destroy()
        janela_principal.deiconify()
        janela_principal.state("zoomed")

    container = ctk.CTkFrame(janela_clientes, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ctk.CTkLabel(
        container,
        text="👥 Cadastro de Clientes",
        font=("Segoe UI", 28, "bold")
    )
    titulo.pack(pady=20)

    frame_form = ctk.CTkFrame(container)
    frame_form.pack(fill="x", padx=50, pady=10)

    entry_nome = ctk.CTkEntry(
        frame_form,
        placeholder_text="Nome do Cliente",
        width=250,
        height=40
    )
    entry_nome.pack(side="left", padx=10, pady=10)

    entry_telefone = ctk.CTkEntry(
        frame_form,
        placeholder_text="Telefone",
        width=200,
        height=40
    )
    entry_telefone.pack(side="left", padx=10)

    entry_email = ctk.CTkEntry(
        frame_form,
        placeholder_text="Email",
        width=250,
        height=40
    )
    entry_email.pack(side="left", padx=10)

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
        text="Clientes Cadastrados",
        font=("Segoe UI", 18, "bold")
    )
    label_lista.pack(pady=10)

    lista_clientes = Listbox(
        frame_lista,
        height=12,
        font=("Segoe UI", 13)
    )
    lista_clientes.pack(fill="both", padx=20, pady=10)

    lista_clientes.bind("<ButtonRelease-1>", selecionar_cliente)

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_editar = ctk.CTkButton(
        frame_botoes,
        text="Editar",
        width=150,
        height=40,
        command=editar
    )
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
        command=voltar
    )
    botao_voltar.pack(side="left", padx=10)

    atualizar_lista()