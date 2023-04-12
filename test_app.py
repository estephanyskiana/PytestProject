from validacoes import *
def test_validaUsuario():
    assert validaUsuario("estephany") == False
    assert validaUsuario("Estephanyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy") == False
    assert validaUsuario("Estephany#") == False
    assert validaUsuario("Estephany") == True
def teste_validaSenha():
    assert validaSenha("Teffy2#") == False
    assert validaSenha("Estephany3") == False
    assert validaSenha("Estephany#") == False
    assert validaSenha("estephany2003#") == False
    assert validaSenha("ESTEPHANY2003#") == False
    assert validaSenha("Estephany2003#") == True