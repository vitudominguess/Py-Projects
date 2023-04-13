# Equipe: 27
# Eduardo Pozzobom/183178/3°SI
# Elthon Migotto/193046/3°SI
# Matheus Sordi/182483/3°SI
# Guilherme Nunes/192582/3°SI
# Guilherme Ruhan/197191/1°EC
# Vitor Pessoa/185467/3°SI
# Kaique Cardoso/196432/1°EC
# Joyce Barros/059339/5°SI
# Thales Sforni/194826/1°SI
# 12/04/2023

import string

def cifra(encrypt):
    crctinvalidos = string.punctuation
    crctvalidos = string.ascii_uppercase + string.digits
    
    while True:
        mensagem = input(f"{'Encriptografar' if encrypt else 'Descriptografar'} a mensagem: ")
        count_invalidos = [letra for letra in mensagem if letra in crctinvalidos or letra.islower()]
        if len(count_invalidos) != 0:
            print("Mensagem Inválida!")
        else:
            break

    while True:
        rot = input("Chave numérica: ")
        if rot.isdigit() == False or rot == '0':
            print("Chave inválida. Digite um valor numérico válido!")
        else:
            rot = int(rot)
            break

    mensagem_criptografada = ''
    for i in mensagem:
        if i in crctvalidos:
            mensagem_criptografada += crctvalidos[(crctvalidos.index(i) + rot) % len(crctvalidos)] if encrypt else crctvalidos[(crctvalidos.index(i) - rot) % len(crctvalidos)]
        elif i == " ":
            mensagem_criptografada += i

    print(mensagem_criptografada)
    input("Digite algo para sair ")
    
while True:
    encrypt = input("Escolha um número para definir o que pretende fazer:\n   1 - Encriptografar\n   0 - Descriptografar\n")
    if not encrypt.isdigit():
        print("Entrada inválida!")
    elif encrypt != "1" and encrypt != "0":
        print("Entrada inválida!")
    else:
        break
cifra(int(encrypt))