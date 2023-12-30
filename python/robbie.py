# ctrl + alt + L --> beautify
vitoria_garota = False
vitoria_robbie = False
soma_resultado = 0
lista_valores = []
cont_div = 0


def IsPrime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
           return True

    else:
        return False


while True:

    try:
        soma_resultado = 0

        line_read = input()

        if not line_read:
            break

        qtd_valores = int(line_read)

        for x in range(qtd_valores):
            valor_lido = int(input())
            lista_valores.append(valor_lido)

        passo = int(input())

        for y in range(0, qtd_valores):
            vi = ((qtd_valores - 1) - (y * passo))
            if vi >= 0:
                soma_resultado += lista_valores[vi]

        if IsPrime(soma_resultado):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")

        else:
            print("Bad boy! I’ll hit you.")

        soma_resultado = 0
        lista_valores.clear()
    except EOFError as e:
        break