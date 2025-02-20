import cv2
import os

def encrypt_image(message, password):
    image_path = "mypic.jpeg"  # Default image path
    output_path = "encrypted_image.png"

    # Load the image
    img = cv2.imread("E:\Internship\AICTE internship by edunet\Stegnography Project by AICTE\mypic.jpg")

    if img is None:
        return "Error: Image not found or unable to read."

    # Dictionary to map characters to pixel values
    d = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0

    # Append a termination character to mark the end of the message
    message += "\0"

    for char in message:
        if n >= img.shape[0] or m >= img.shape[1]:  # Prevent out-of-bounds error
            break

        img[n, m, z] = d.get(char, 0)  # Store character value in pixel channel

        n += 1
        m += 1
        z = (z + 1) % 3  # Loop through color channels

    # Save the encrypted image
    cv2.imwrite(output_path, img)

    return f"Message encrypted successfully in {output_path}"

if __name__ == "__main__":
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    result = encrypt_image(message, password)
    print(result)
