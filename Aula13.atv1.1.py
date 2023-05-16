# def texto(t):
#
#     for y in range(len(texto) -1, -1, -1):
#         print(texto[y], end="")
#     i=0
#     for x in texto:
#         if x != ' ':
#             i += 1
#     print()
#     print(f"LETRAS: {i}")
#
# t("Sara doida")

def inverter(t):
    print(t[::-1])
    print(len(t)- t.count(' '))
    # count: Conta quantas vezes foi repetida
inverter("SARA")