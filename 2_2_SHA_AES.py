from aes_cipher import DataEncrypter
from aes_cipher import DataDecrypter
import hashlib

key = b'cbc1bb49-c8e2-4b7e-bc7c-fe704f576981'

data_encrypter = DataEncrypter()
data_decrypter = DataDecrypter()

str = input('Qual a string para o hash?\n')


# hash source

hashOrigem = hashlib.sha256(str.encode()).hexdigest()

print('O resultado do hash na origem é: ')
print(hashOrigem, "\n")

mensagemHash = str + "***" + hashOrigem


# encrypt

data_encrypter.Encrypt(mensagemHash, '123', key)
enc_data = data_encrypter.GetEncryptedData()

print('Seu payload criptografado é: ')
print(enc_data, "\n")


# decrypt

data_decrypter.Decrypt(enc_data, '123', key)
dec_data = data_decrypter.GetDecryptedData()

print('Seu payload decriptografado é: ')
print(dec_data, '\n')

payloadRecebido = dec_data.split(b'***')


# hash destination

hashDestino = hashlib.sha256(payloadRecebido[0]).hexdigest()

print('O resultado do hash no destino é: ')
print(hashDestino, '\n')

if (hashDestino == payloadRecebido[1].decode()):
    print('Mensagem integra')