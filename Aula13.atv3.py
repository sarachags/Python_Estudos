def numero_primo(n):
    for x in range(2, n):
        if n % x == 0:
            return f"{n} não é primo"

    if n != 1:
        return f"{n} é primo"

print(numero_primo(25))