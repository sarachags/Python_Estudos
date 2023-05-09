def valor_estoque(nome, quantidade, valor_unitario):
    valor_do_estoque = quantidade + valor_unitario
    return nome, valor_do_estoque

v1 = valor_estoque ("Garrafa Termica", 550, 125)

valor_total_estoque=v1
print(valor_total_estoque)