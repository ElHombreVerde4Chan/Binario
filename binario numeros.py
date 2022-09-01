#Codigo para pasar numeros a binarios

def binario(decimal):
    binario = ""
    #Codigo De Anananias
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal //2
        return str(decimal) + binario
    
numero = int(input("Introduce el numero que quieres convertir a binario: "))
print(binario(numero))