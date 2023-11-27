import secrets
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64


def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def encrypt_password(contraseña, clave_maestra):
    # Derivar una clave a partir de la clave maestra
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b"saltsalt",
        iterations=100000,
        length=32,
        backend=default_backend(),
    )
    clave_derivada = base64.urlsafe_b64encode(kdf.derive(clave_maestra.encode()))

    # Cifrar la contraseña
    cipher = Cipher(
        algorithms.AES(clave_derivada), modes.CFB8(), backend=default_backend()
    )
    encryptor = cipher.encryptor()
    contraseña_cifrada = encryptor.update(contraseña.encode()) + encryptor.finalize()

    return contraseña_cifrada


def guardar_contraseña_en_archivo(contraseña_cifrada, nombre_archivo):
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(contraseña_cifrada)


# Generar una contraseña
nueva_contraseña = generate_password()
print(f"Nueva Contraseña Generada: {nueva_contraseña}")

# Solicitar una clave maestra para cifrar la contraseña
clave_maestra = input("Introduce tu clave maestra: ")

# Cifrar la contraseña
contraseña_cifrada = encrypt_password(nueva_contraseña, clave_maestra)

# Guardar la contraseña cifrada en un archivo
nombre_archivo = "contraseña_cifrada.bin"
guardar_contraseña_en_archivo(contraseña_cifrada, nombre_archivo)

print(f"Contraseña cifrada guardada en {nombre_archivo}")
