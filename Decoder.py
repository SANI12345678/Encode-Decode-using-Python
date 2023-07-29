import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def on_encrypt():
    plaintext = entry.get()
    shift_value = int(shift.get())
    encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)
    output_label.config(text=f"Encrypted Text: {encrypted_text}")

def on_decrypt():
    ciphertext = entry.get()
    shift_value = int(shift.get())
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift_value)
    output_label.config(text=f"Decrypted Text: {decrypted_text}")

# Create the main application window
root = tk.Tk()
root.title("Simple Encoder-Decoder")
root.geometry("400x300")

bg_image_path = "background_image.jpg"

# Load and set the background image
bg_image = Image.open(bg_image_path)  # Replace "background_image.jpg" with your own image file path
bg_image = bg_image.resize((400, 300), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create input elements
input_frame = ttk.Frame(root, width=300, height=100, style="Input.TFrame")
input_frame.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

label = ttk.Label(input_frame, text="Enter text:", font=("Helvetica", 14))
label.pack(pady=5)

entry = ttk.Entry(input_frame, font=("Helvetica", 14))
entry.pack(pady=5)

shift_label = ttk.Label(input_frame, text="Enter shift value:", font=("Helvetica", 14))
shift_label.pack(pady=5)

shift = ttk.Entry(input_frame, font=("Helvetica", 14))
shift.pack(pady=5)

# Create buttons for encryption and decryption
button_frame = ttk.Frame(root, style="Button.TFrame")
button_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

encrypt_button = ttk.Button(button_frame, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = ttk.Button(button_frame, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=0, column=1, padx=10)

# Create output label
output_label = ttk.Label(root, text="", font=("Helvetica", 14, "bold"))
output_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Apply custom styles for widgets
style = ttk.Style()
style.configure("Input.TFrame", background="white", borderwidth=3, relief=tk.RAISED)
style.configure("Button.TFrame", background="white")
style.configure("TButton", font=("Helvetica", 12), background="#4CAF50", foreground="white")

# Start the main event loop
root.mainloop()