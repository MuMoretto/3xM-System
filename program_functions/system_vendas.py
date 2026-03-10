import customtkinter as ctk

def abrir_vendas(janela_principal):

    janela_principal.withdraw()

    vendas = ctk.CTkToplevel()
    vendas.title("3xM System - Vendas")
    vendas.state("zoomed")

    # ---------- CONTAINER PRINCIPAL ----------

    container = ctk.CTkFrame(vendas, corner_radius=0)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------- TÍTULO ----------

    titulo = ctk.CTkLabel(
        container,
        text="🛒 Nova Venda",
        font=("Segoe UI", 28, "bold")
    )
    titulo.pack(pady=20)

    # ---------- BUSCA DE PRODUTO ----------

    frame_busca = ctk.CTkFrame(container)
    frame_busca.pack(fill="x", padx=50, pady=10)

    entry_produto = ctk.CTkEntry(
        frame_busca,
        placeholder_text="🔎 Digite o código ou nome do produto",
        height=40,
        font=("Segoe UI", 14)
    )
    entry_produto.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    botao_adicionar = ctk.CTkButton(
        frame_busca,
        text="Adicionar",
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold")
    )
    botao_adicionar.pack(side="left", padx=10)

    # ---------- LISTA DE PRODUTOS ----------

    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(fill="both", padx=50, pady=20)

    label_lista = ctk.CTkLabel(
        frame_lista,
        text="Produtos da Venda",
        font=("Segoe UI", 18, "bold")
    )
    label_lista.pack(pady=10)

    lista_produtos = ctk.CTkTextbox(
    frame_lista,
    height=250,
    font=("Consolas", 14)
    )
    lista_produtos.pack(fill="x", padx=20, pady=10)

    # ---------- TOTAL ----------

    frame_total = ctk.CTkFrame(container)
    frame_total.pack(fill="x", padx=50, pady=20)

    label_total = ctk.CTkLabel(
        frame_total,
        text="Total: R$ 0,00",
        font=("Segoe UI", 24, "bold")
    )
    label_total.pack(side="left", padx=20)

    # ---------- BOTÕES ----------

    frame_botoes = ctk.CTkFrame(container)
    frame_botoes.pack(pady=20)

    botao_finalizar = ctk.CTkButton(
        frame_botoes,
        text="Finalizar Venda",
        width=180,
        height=45,
        font=("Segoe UI", 16, "bold")
    )
    botao_finalizar.pack(side="left", padx=10)

    botao_cancelar = ctk.CTkButton(
        frame_botoes,
        text="Cancelar",
        width=140,
        height=45,
        fg_color="#E53935",
        hover_color="#C62828",
        font=("Segoe UI", 16, "bold")
    )
    botao_cancelar.pack(side="left", padx=10)

    botao_voltar = ctk.CTkButton(
        frame_botoes,
        text="Voltar",
        width=140,
        height=45,
        font=("Segoe UI", 16, "bold"),
        command=lambda: voltar(vendas, janela_principal)
)

    botao_voltar.pack(side="left", padx=10)

def voltar(vendas, janela_principal):
    vendas.destroy()
    janela_principal.deiconify()
    janela_principal.state("zoomed")