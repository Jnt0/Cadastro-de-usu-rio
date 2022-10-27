binario = ['01101010', '01101111', '01101110', '01100001']
chave =   ['01100001', '01110011', '01100100', '01100110']


def bin2xor(binario, chave):
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


xor = bin2xor(binario, chave)
#  ['00001011', '00011100', '00001010', '00000111'] 
#  ['01100001', '01110011', '01100100', '01100110']


def xor2bin(xor, chave):
    decifrado = ''
    
    for x,y in zip(xor, chave):  

        for i,j in zip(x, y):  

            bin = int(i) ^ int(j)  
        
            decifrado = decifrado + str(bin)  


    partes = []
    for index in range(0, len(decifrado), 8):
        partes.append(decifrado[index : index + 8])
    return partes

print('binario ',binario)
print('chave ', chave)
texto_escondido = bin2xor(binario, chave)
print('escondido ', texto_escondido)
print(xor2bin(texto_escondido, chave))
