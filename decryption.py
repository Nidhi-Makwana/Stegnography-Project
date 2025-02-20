import cv2

def decrypt_image(stored_password, input_password):
    if stored_password != input_password:
        return "YOU ARE NOT AUTHORIZED"

    image_path = "encrypted_image.png"  # Default encrypted image path

    # Load the encrypted image
    img = cv2.imread(image_path)

    if img is None:
        return "Error: Image not found or unable to read."

    # Dictionary to map pixel values to characters
    c = {i: chr(i) for i in range(256)}

    message = ""
    n, m, z = 0, 0, 0

    while True:
        if n >= img.shape[0] or m >= img.shape[1]:  # Prevent out-of-bounds access
            break

        pixel_value = img[n, m, z]
        char = c.get(pixel_value, "")

        if char == "\0":  # Stop if termination character (null) is found
            break

        message += char
        n += 1
        m += 1
        z = (z + 1) % 3  # Loop through color channels

    return message

if __name__ == "__main__":
    stored_password = input("Enter a passcode: ")
    input_password = input("Enter passcode for Decryption: ")

    decrypted_message = decrypt_image(stored_password, input_password)
    print("Decryption message:", decrypted_message)
