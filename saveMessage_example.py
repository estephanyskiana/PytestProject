from cryptographyFramework import *

initializeWrite()
user = "estephany"
password = "0110803"
encryptedText = encryptMessage(user, password, "Mensagem da Estephany!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda mensagem secreta!")
saveNewLine(encryptedText)

