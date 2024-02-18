def binario(numero):
    if(numero==0):
        return ""
    else:
        return binario(numero//2)+str(numero/2)
print (binario(5))