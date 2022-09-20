from os import urandom
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.primitives.asymmetric import rsa , padding

class algo :    

    def aes_256_ctr_encrypt(text : bytes) -> tuple[bytes,bytes,bytes] :
        # AES block size is 128 bits == 16 bytes 
        key = urandom(32)    # random key of 256 bits == 32 bytes
        nonce = urandom(16)  # random initialization vector

        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce)) # cipher class
        encryptor = cipher.encryptor()    
        cipherText = encryptor.update(text) + encryptor.finalize()    
        return (cipherText,key,nonce)


    def aes_256_ctr_decrypt(cipherText : bytes, key : bytes, nonce : bytes) -> bytes :
        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce)) # cipher class
        decryptor = cipher.decryptor()
        plainText = decryptor.update(cipherText) + decryptor.finalize()
        return plainText


    def rsa_generate_keys(exponent : int, key_size : int) :
        algo.private_key = rsa.generate_private_key(
            public_exponent=exponent,
            key_size=key_size,
        )

    def rsa_encrypt(text : bytes) -> bytes:    
        cipherText = algo.private_key.public_key().encrypt(
            text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return cipherText


    def rsa_decrypt(cipherText : bytes) -> bytes:
        plaintext = algo.private_key.decrypt(
        cipherText,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        return plaintext

    def sha256(text : bytes) -> bytes :
        digest = hashes.Hash(hashes.SHA256())
        digest.update(text)
        return digest.finalize()
