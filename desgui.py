import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to encrypt the text
def encrypt_text():
    try:
        key = key_entry.get().encode('utf-8')
        text = input_text.get("1.0", tk.END).strip()

        if len(key) != 8:
            messagebox.showerror("Error", "Kunci harus memiliki panjang 8 karakter.")
            return

        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(text.encode('utf-8'), DES.block_size))

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, ciphertext.hex())
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Function to decrypt the text
def decrypt_text():
    try:
        key = key_entry.get().encode('utf-8')
        ciphertext = bytes.fromhex(input_text.get("1.0", tk.END).strip())

        if len(key) != 8:
            messagebox.showerror("Error", "Kunci harus memiliki panjang 8 karakter.")
            return

        cipher = DES.new(key, DES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size).decode('utf-8')

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, plaintext)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("DES Encryption/Decryption")

# Create labels and entries
key_label = tk.Label(root, text="Kunci (8 karakter):")
key_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

key_entry = tk.Entry(root, width=20)
key_entry.grid(row=0, column=1, padx=10, pady=5)

input_label = tk.Label(root, text="Masukan Teks:")
input_label.grid(row=1, column=0, padx=10, pady=5, sticky="ne")

input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=1, column=1, padx=10, pady=5)

output_label = tk.Label(root, text="Hasil:")
output_label.grid(row=2, column=0, padx=10, pady=5, sticky="ne")

output_text = tk.Text(root, height=5, width=40)
output_text.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_text)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt_text)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
