from cryptographyFramework import *
usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
mensagem1 = ""
mensagem2 = ""

def validaUsuario(usuario):
    while True:
        if len(usuario) > 30:
            usuario = input(("[ERRO] O seu nome de usuário deve ter no MÁXIMO 30 caracteres. Tente novamente: "))
        elif usuario[0].islower():
            usuario = input(("[ERRO] O primeiro caractere do nome de usuário deve ser maiúsculo. Tente novamente: "))
        elif not usuario.isalnum():
            usuario = input(("[ERRO] O nome de usuário NÃO deve conter caractere especial. Tente novamente: "))
        else:
            return ("O nome de usuário foi cadastrado!")
def validaSenha(senha):
    while True:
        if len(senha) <= 10:
            senha = input("[ERRO] A senha deve ter no mínimo 10 caracteres. Tente novamente: ")
        elif senha.isalnum():
            senha = input("[ERRO] A senha necessita um caractere especial (!@#$%¨¨&*). Tente novamente: ")
        elif senha.isalpha():
            senha = input("[ERRO] A senha necessita ter pelo menos um número. Tente novamente: ")
        elif senha.islower():
            senha = input("[ERRO] A senha deve ter pelo menos um caractere maiúsculo. Tente novamente: ")
        else:
            return ("Senha cadastrada!")
def pedirMensagem(mensagem1, mensagem2):
    mensagem1 = input("Digite a primeira mensagem: ")
    mensagem2 = input("Digite a segunda mensagem: ")
    print("Suas mensagens foram gravadas!")
def encripta():
    initializeWrite()
    encryptedText = encryptMessage(usuario, senha, mensagem1)
    saveNewLine(encryptedText)
    encryptedText = encryptMessage(usuario, senha, mensagem2)
    saveNewLine(encryptedText)
def exibir():
    initializeRead()
    line1 = readNextLine()
    print(line1)
    print(decryptMessage(usuario, senha, line1))
    line2 = readNextLine()
    print(line2)
    print(decryptMessage(usuario, senha, line2))

validaUsuario(usuario)
validaSenha(senha)
pedirMensagem(mensagem1, mensagem2)
encripta()
exibir()
