import cv2
import tkinter as tk
from tkinter import messagebox

# Encryption Function
def encrypt_image():
    message = message_entry.get()
    password = password_entry.get()

    if not message or not password:
        messagebox.showerror("Error", "Please enter both a message and a passcode!")
        return

    image_path = "E:\Internship\AICTE internship by edunet\Stegnography Project by AICTE\mypic.jpg"  # Input image
    output_path = "E:\Internship\AICTE internship by edunet\Stegnography Project by AICTE\encrypted_image.png"  # Encrypted image output

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Error loading image!")
        return

    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0

    message += "\0"  # End of message marker

    for char in message:
        if n >= img.shape[0] or m >= img.shape[1]:
            break
        img[n, m, z] = d.get(char, 0)
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", f"Message encrypted successfully in {output_path}")

# Decryption Function
def decrypt_image():
    stored_password = password_entry.get()
    input_password = decrypt_password_entry.get()

    if not stored_password or not input_password:
        messagebox.showerror("Error", "Please enter the passcode for decryption!")
        return

    if stored_password != input_password:
        messagebox.showerror("Error", "Incorrect passcode! Access Denied.")
        return

    image_path = "encrypted_image.png"
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Error loading encrypted image!")
        return

    c = {i: chr(i) for i in range(256)}
    message = ""
    n, m, z = 0, 0, 0

    while True:
        if n >= img.shape[0] or m >= img.shape[1]:
            break
        pixel_value = img[n, m, z]
        char = c.get(pixel_value, "")

        if char == "\0":
            break

        message += char
        n += 1
        m += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decryption Result", f"Decryption message: {message}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryption & Decryption")
root.geometry("400x350")

# Encryption Section
tk.Label(root, text="Enter Secret Message:").pack(pady=5)
message_entry = tk.Entry(root, width=40)
message_entry.pack()

tk.Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = tk.Entry(root, width=20, show="*")
password_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_image)
encrypt_button.pack(pady=10)

# Decryption Section
tk.Label(root, text="Enter Passcode for Decryption:").pack(pady=5)
decrypt_password_entry = tk.Entry(root, width=20, show="*")
decrypt_password_entry.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_image)
decrypt_button.pack(pady=10)

# Run GUI
root.mainloop()
