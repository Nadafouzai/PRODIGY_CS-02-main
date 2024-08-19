from PIL import Image

def xor_encrypt_decrypt(pixel, key):
    # Appliquer XOR sur chaque canal de couleur
    r, g, b = pixel
    return (r ^ key, g ^ key, b ^ key)

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            # Chiffrer chaque pixel avec la clé XOR
            pixels[i, j] = xor_encrypt_decrypt(pixels[i, j], key)

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    # Déchiffrer en appliquant à nouveau l'opération XOR
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            pixels[i, j] = xor_encrypt_decrypt(pixels[i, j], key)

    img.save(output_path)
    print("Image decrypted successfully!")

# Chemins des images
input_image = r"C:\Users\nada\Downloads\INFOPRODIGY\PRODIGY_CS-02-main\input.jpg"
encrypted_image = r"C:\Users\nada\Downloads\INFOPRODIGY\PRODIGY_CS-02-main\encrypted_image.jpg"
decrypted_image = r"C:\Users\nada\Downloads\INFOPRODIGY\PRODIGY_CS-02-main\decrypted_image.jpg"

# Clé de chiffrement (doit être entre 0 et 255)
encryption_key = 123

# Chiffrer l'image
encrypt_image(input_image, encrypted_image, encryption_key)

# Déchiffrer l'image
decrypt_image(encrypted_image, decrypted_image, encryption_key)
