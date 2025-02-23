produto_nome = "Caneta"
produto_cor = "Azul"
produto_preco = 1.50
produto_em_estoque = True
produto_codigo = 2376
produto_dimensao_altura = 12.1
produto_demensao_largura = 1.1

compra = ("Alex", produto_nome, 3)

total_compra = compra[2] * produto_preco

print(
    f"O cliente {compra[0]} comprou {compra[2]} {compra[1]}"
    f" no valor de R${total_compra:.2f}"
)

