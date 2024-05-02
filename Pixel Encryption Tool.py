from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, save_path):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply encryption operation to each pixel
    encrypted_array = img_array ^ key

    # Create encrypted image from encrypted pixel array
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(save_path)
    print("Image encrypted and saved successfully!")

def decrypt_image(encrypted_image_path, key, save_path):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)

    # Apply decryption operation to each pixel
    decrypted_array = encrypted_array ^ key

    # Create decrypted image from decrypted pixel array
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(save_path)
    print("Image decrypted and saved successfully!")

while True:
    action = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
    
    if action == 'q':
        print("Exiting program...")
        break
    
    if action not in ['e', 'd']:
        print("Invalid input. Please enter 'e', 'd', or 'q'.")
        continue
    
    image_path = input("Enter the path to the image file: ")
    save_folder = input("Enter the folder path to save the result: ")
    save_name = input("Enter the name for the result file (with extension): ")
    save_path = os.path.join(save_folder, save_name)
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if action == 'e':
        encrypt_image(image_path, key, save_path)
    elif action == 'd':
        decrypt_image(image_path, key, save_path)
