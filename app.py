from cryptographyFramework import *
from validacoes import *
usuario = ""
senha = ""
mensagem1 = ""
mensagem2 = ""

def solicitaUsuario():
    while True:
        usuario = input("Digite seu nome de usuário: ")
        if validaUsuario(usuario):
            break
def solicitaSenha():
    while True:
        senha = input("Digite sua senha: ")
        if validaSenha(senha):
            break
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

solicitaUsuario()
solicitaSenha()
pedirMensagem(mensagem1, mensagem2)
encripta()
exibir()