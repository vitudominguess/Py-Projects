def cifra(encrypt):
    mensagem = input(f"{'Encriptografar' if encrypt else 'Descriptografar'} a mensagem: ").upper()
    rot = int(input("Chave numérica: "))
    crctvalidos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    mensagem_criptografada = ''
    for i in mensagem:
        if i in crctvalidos:
            mensagem_criptografada += crctvalidos[(crctvalidos.index(i) + rot) % len(crctvalidos)] if encrypt else crctvalidos[(crctvalidos.index(i) - rot) % len(crctvalidos)]
        elif i == " ":
            mensagem_criptografada += i
        else:
            print("Mensagem Inválida!")
    print(mensagem_criptografada)
encrypt = int(input("Escolha um número para definir o que pretende fazer:\n   1 - Encriptografar\n   0 - Descriptografar\n"))

while 
if 1 != encrypt != 0:
    print("Entrada Inválida")
    cifra()
cifra(encrypt)