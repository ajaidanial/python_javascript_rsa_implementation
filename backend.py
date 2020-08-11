import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

# public key
public_key_text = open("keys/public_key.pem", "rb").read()
public_key = RSA.importKey(public_key_text)

# private key
private_key_text = open("keys/private_key.pem", "rb").read()
private_key = RSA.importKey(private_key_text)


def encrypt(string_to_be_encrypted: str):
    """Encrypt's the given string input. The library works on bytes."""

    message_bytes = string_to_be_encrypted.encode("utf-8")
    cipher = PKCS1_v1_5.new(public_key)
    encrypted_bytes = base64.b64encode(cipher.encrypt(message_bytes))
    # convert the bytes to string and return
    return encrypted_bytes.decode("utf-8")


def decrypt(string_to_be_decrypted: str):
    """Decrypt's the given string input. The library works on bytes."""

    message_bytes = string_to_be_decrypted.encode("utf-8")
    cipher = PKCS1_v1_5.new(private_key)
    decrypted_bytes = cipher.decrypt(base64.b64decode(message_bytes), "dummy text")
    # convert the bytes to string and return
    return decrypted_bytes.decode("utf-8")


if __name__ == "__main__":
    # sample test
    dummy_data = "Hey, I am working"
    encrypted_data = encrypt(dummy_data)
    decrypted_data = decrypt(encrypted_data)
    print("Encrypted Data: ", encrypted_data)
    print("Decrypted Data: ", decrypted_data)
