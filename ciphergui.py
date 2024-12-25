import customtkinter as ctk
from tkinter import messagebox

# Fungsi Caesar Cipher untuk enkripsi dan dekripsi
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

# Fungsi untuk menangani tombol Enkripsi
def encrypt_text():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher(text, shift, mode="encrypt")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka")

# Fungsi untuk menangani tombol Dekripsi
def decrypt_text():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
        decrypted_text = caesar_cipher(text, shift, mode="decrypt")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka")

# Pengaturan GUI menggunakan customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Caesar Cipher")
root.geometry("400x550")

# Label Title
title_label = ctk.CTkLabel(root, text="Caesar Cipher Encrypt & Decrypt", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Frame untuk Input Teks
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(input_frame, text="Masukkan teks:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
input_text = ctk.CTkTextbox(input_frame, height=100, width=360, font=("Arial", 10))
input_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Frame untuk Pengaturan Shift
shift_frame = ctk.CTkFrame(root)
shift_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(shift_frame, text="Shift:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
shift_entry = ctk.CTkEntry(shift_frame, font=("Arial", 10), width=50)
shift_entry.grid(row=0, column=1, padx=5, pady=5)

# Frame untuk Tombol Enkripsi dan Dekripsi
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)
encrypt_button = ctk.CTkButton(button_frame, text="Enkripsi", font=("Arial", 12, "bold"), fg_color="#0984e3", text_color="white", width=140, corner_radius=20, command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=10, pady=10)

decrypt_button = ctk.CTkButton(button_frame, text="Dekripsi", font=("Arial", 12, "bold"), fg_color="#d63031", text_color="white", width=140, corner_radius=20, command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10, pady=10)

# Frame untuk Output Hasil
output_frame = ctk.CTkFrame(root)
output_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(output_frame, text="Hasil:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
output_text = ctk.CTkTextbox(output_frame, height=100, width=360, font=("Arial", 10))
output_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Jalankan loop GUI
root.mainloop()
