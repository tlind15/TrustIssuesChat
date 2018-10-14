from src.encrypter.controller import EncryptionController
from src.message.message import PlaintextMessage

text = "My Name is Thomas"
controller = EncryptionController(PlaintextMessage(text), "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
encrypted_message = controller.encrypt_message()

print(encrypted_message.get_text())
print(encrypted_message.key_ciphertext)
print(encrypted_message.message_authentication_tag)

