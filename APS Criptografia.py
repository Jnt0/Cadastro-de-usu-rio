def expansaoTexto(texto):
    #  Expansão de texto para 128 bytes
    txt = texto + 'ç' * (128 - len(texto))
    return txt

def expansaoChave(chave):
    #  Expansão de chave para 128 bytes
    key = chave + 'ç' * (128 - len(chave))
    return key


def reducaoString(txt):
    for x in range(len(txt)):
        string = string.replace(txt[x],"")
    return string


def paraBinario(txt):
    """Converte texto para binarios"""

    valores_individuais, valores_binarios = [], []

    for letra in txt:
        valores_individuais.append(ord(letra))
    for letra in valores_individuais:
        valores_binarios.append(bin(letra)[2:])
    binario = []
    for i in valores_binarios:
        binario.append(i.zfill(8))
    return binario


def paraString(binario):
    """Coverte binarios para string"""

    string = ''
    for i in binario:
        decimal = int(i, 2)
        string = string + chr(decimal)
    return string


def bin_xor(binario, chave):
    cifrado = ''
    for x,y in zip(binario, chave):  # Percorre cada posição da lista de binarios.
        for i,j in zip(x, y):  # Percorre cada posição de binarios individualmente.
            xor = int(i) ^ int(j)  # Calcula o xor
            cifrado = cifrado + str(xor)  # Concatena o resultado
    # distribui os binarios em uma lista
    partes = []
    for index in range(0, len(cifrado), 8):
        partes.append(cifrado[index : index + 8])
    return partes


def xor_bin(xor, chave):
    decifrado = ''
    for x,y in zip(xor, chave):  
        for i,j in zip(x, y):  
            bin = int(i) ^ int(j)  
            decifrado = decifrado + str(bin)  
    partes = []
    for index in range(0, len(decifrado), 8):
        partes.append(decifrado[index : index + 8])
    return partes


texto = 'jonathan'
key = input("Digite uma chave de até 16 caracteres: ")

chave = expansaoChave(key)
txt = expansaoTexto(texto)

binario_txt = paraBinario(txt)
print('binario_txt: ', binario_txt)

binario_chave = paraBinario(chave)
print('binario_chave: ', binario_chave)

xor = bin_xor(binario_txt, binario_chave)
print('texto codificado:', xor)


