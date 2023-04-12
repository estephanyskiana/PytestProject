def validaUsuario(usuario):
        if len(usuario) > 30:
            print("[ERRO] O seu nome de usuário deve ter no MÁXIMO 30 caracteres. Tente novamente.")
            return False
        elif usuario[0].islower():
            print("[ERRO] O primeiro caractere do nome de usuário deve ser maiúsculo. Tente novamente.")
            return False
        elif not usuario.isalnum():
            print("[ERRO] O nome de usuário NÃO deve conter caractere especial. Tente novamente.")
            return False
        else:
            print("O nome de usuário foi cadastrado!")
            return True
def validaSenha(senha):
    while True:
        if len(senha) <= 10:
            print("[ERRO] A senha deve ter no mínimo 10 caracteres. Tente novamente.")
            return False
        elif senha.isalnum():
            print("[ERRO] A senha necessita um caractere especial (!@#$%¨¨&*). Tente novamente.")
            return False
        elif senha.isalpha():
            print("[ERRO] A senha necessita ter pelo menos um número. Tente novamente.")
            return False
        elif senha.islower():
            print("[ERRO] A senha deve ter pelo menos um caractere maiúsculo. Tente novamente.")
            return False
        elif senha.isupper():
            print("[ERRO] A senha deve ter pelo menos um caractere maiúsculo. Tente novamente.")
            return False
        else:
            print("A senha de usuário foi cadastrada!")
            return True