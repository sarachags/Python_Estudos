def imprime_nome(nome):
    i=0
    for x in nome:
        if x != ' ':
            i += 1
    print(f"LETRAS: {i}")
    print(f"AO CONTRÁRIO: {nome[::-1]}")

imprime_nome("Maeli")