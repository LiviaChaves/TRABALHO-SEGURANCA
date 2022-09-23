from aes_cipher import DataEncrypter
from aes_cipher import DataDecrypter

data = input('Digite o texto a ser criptografado:\n')
key = b'cbc1bb49-c8e2-4b7e-bc7c-fe704f576981' 


#criptografar
data_encrypter = DataEncrypter() 
data_encrypter.Encrypt(data, "123", key) #dado a ser criptografado recebe o dado como parametro e a chave a ser utilizada
enc_data = data_encrypter.GetEncryptedData() #atribui ao enc_Data a mensagem criptografada

print()
print('Seu texto criptografado é: ')
print(enc_data, '\n') #chama a função de criptografia


#descriptografar
data_decrypter = DataDecrypter()
data_decrypter.Decrypt(enc_data, '123', key) #dado a ser descriptografado recebe o dado como parametro e a chave a ser utilizada
dec_data = data_decrypter.GetDecryptedData() #atribui ao dec_Data a mensagem descriptografada

print('Seu texto decriptografado é: ')
print(dec_data, '\n') #chama a função de descriptografar