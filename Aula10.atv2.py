reco = 'sim'
while reco == 'sim':
    fh = int(input("DIGITE O VALOR EM FAHRENHEIT: "))
    c = ((fh - 32)/9)*5
    print("ESSA TEMPERATURA EM CELSIUS É", c,"ºC")
    reco = input("DESEJA RECOMEÇAR? ")
else:
    print("FIM DO CALCULO.")