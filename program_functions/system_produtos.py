import customtkinter as ctk

def abrir_produtos(menuWindow):

    menuWindow.withdraw()

    produtos = ctk.CTkToplevel()
    produtos.title("3xM System - Produtos")
    produtos.state("zoomed")

    # ---------- CONTAINER PRINCIPAL ----------

    container = ctk.CTkFrame(produtos, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------- TÍTULO ----------

    titulo = ctk.CTkLabel(
        container,
        text="📦 Cadastro de Produtos",
        font=("Segoe UI", 28, "bold")
    )
    titulo.pack(pady=20)

    # ---------- FORMULÁRIO ----------

    frame_form = ctk.CTkFrame(container)
    frame_form.pack(fill="x", padx=50, pady=10)

    entry_nome = ctk.CTkEntry(
        frame_form,
        placeholder_text="Nome do Produto",
        width=250,
        height=40
    )
    entry_nome.pack(side="left", padx=10, pady=10)

    entry_codigo = ctk.CTkEntry(
        frame_form,
        placeholder_text="Código",
        width=150,
        height=40
    )
    entry_codigo.pack(side="left", padx=10)

    entry_preco = ctk.CTkEntry(
        frame_form,
        placeholder_text="Preço",
        width=150,
        height=40
    )
    entry_preco.pack(side="left", padx=10)

    entry_estoque = ctk.CTkEntry(
        frame_form,
        placeholder_text="Estoque",
        width=120,
        height=40
    )
    entry_estoque.pack(side="left", padx=10)

    botao_cadastrar = ctk.CTkButton(
        frame_form,
        text="Cadastrar",
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold")
    )
    botao_cadastrar.pack(side="left", padx=10)

    # ---------- LISTA DE PRODUTOS ----------

    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(fill="both", expand=True, padx=50, pady=20)

    label_lista = ctk.CTkLabel(
        frame_lista,
        text="Produtos Cadastrados",
        font=("Segoe UI", 18, "bold")
    )
    label_lista.pack(pady=10)

    lista_produtos = ctk.CTkTextbox(
        frame_lista,
        height=300,
        font=("Consolas", 14)
    )
    lista_produtos.pack(fill="both", expand=True, padx=20, pady=10)

    # ---------- BOTÕES ----------

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_editar = ctk.CTkButton(
        frame_botoes,
        text="Editar",
        width=150,
        height=40
    )
    botao_editar.pack(side="left", padx=10)

    botao_excluir = ctk.CTkButton(
        frame_botoes,
        text="Excluir",
        width=150,
        height=40,
        fg_color="#E53935",
        hover_color="#C62828"
    )
    botao_excluir.pack(side="left", padx=10)

    botao_voltar = ctk.CTkButton(
        frame_botoes,
        text="Voltar",
        width=150,
        height=40,
        command=lambda: voltar(produtos, menuWindow)
    )
    botao_voltar.pack(side="left", padx=10)


def voltar(produtos, janela_principal):
    produtos.destroy()
    janela_principal.deiconify()
    janela_principal.state("zoomed")