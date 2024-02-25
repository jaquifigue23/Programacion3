def binario(numero):
    if numero == 0:
        return "0"
    else:
        return binario(numero // 2) + str(numero % 2)

print(binario(5))

