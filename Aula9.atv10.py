eleitores = float(input("QUANTOS ELEITORES EXISTEM E SEU MUNICIPIO: "))
votos_brancos = float(input("QUANTOS VOTOS BRANCOS HÁ EM SEU MUNICIPIO: "))
votos_nulos = float(input("QUANTOS VOTOS NULOS HÁ EM SEU MUNICIPIO: "))
votos_validos = float(input("QUANTOS VOTOS VÁLIDOS HÁ EM SEU MUNICIPIO: "))

porc_brancos = (votos_brancos/eleitores) * 100
porc_nulos = (votos_nulos/eleitores) * 100
porc_validos = (votos_validos/eleitores) * 100

print("AS PORCENTAGENS SÃO:\n", "VOTOS BRANCOS:", porc_brancos, "\n VOTOS NULOS:", porc_nulos, "\n VOTOS VÁLIDOS:", porc_validos)
