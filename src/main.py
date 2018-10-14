from src.encrypter.controller import EncryptionController

text = "My Name is Thomas"
controller = EncryptionController(text, "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
encrypted_message = controller.encrypt_message()

print(encrypted_message.get_text())
print(encrypted_message.key_ciphertext)
print(encrypted_message.message_authentication_tag)

