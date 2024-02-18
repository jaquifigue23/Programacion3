function arreglo:
arr=[2,5,8,10,13,20,23,50,90]
x=23
print(binario(arr,x))





def binario (arr, x, inicio=0, fin=None):
    if(fin==None):
        fin=len(arr)-1
    mid=(inicio+fin)//2
    if(x==arr[mid]):
        print("Numero Encontrado")
        return mid
    elif(x< arr[mid]):
        return binario(arr,x,inicio,mid-1)
    else:
        return binario(arr,x,fin,mid+1)