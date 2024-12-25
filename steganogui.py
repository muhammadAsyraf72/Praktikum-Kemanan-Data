import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Steganography Functions
def encode_message(image_path, message, output_path):
    try:
        image = Image.open(image_path)
        encoded_image = image.copy()

        width, height = image.size
        pixels = encoded_image.load()

        binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

        data_index = 0
        for y in range(height):
            for x in range(width):
                if data_index < len(binary_message):
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | int(binary_message[data_index])
                    pixels[x, y] = (r, g, b)
                    data_index += 1

        encoded_image.save(output_path)
        messagebox.showinfo("Success", "Pesan berhasil disisipkan dan gambar disimpan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def decode_message(image_path):
    try:
        image = Image.open(image_path)
        pixels = image.load()

        binary_message = ""
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = pixels[x, y]
                binary_message += str(r & 1)

                if binary_message[-16:] == '1111111111111110':
                    binary_message = binary_message[:-16]
                    return ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

        messagebox.showinfo("Info", "Tidak ditemukan pesan dalam gambar.")
        return ""
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        return ""

# GUI Functions
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    if file_path:
        input_image_path.set(file_path)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        output_image_path.set(file_path)

def encode():
    image_path = input_image_path.get()
    message = message_text.get("1.0", tk.END).strip()
    output_path = output_image_path.get()

    if not image_path or not message or not output_path:
        messagebox.showerror("Error", "Semua kolom harus diisi.")
        return

    encode_message(image_path, message, output_path)

def decode():
    image_path = input_image_path.get()

    if not image_path:
        messagebox.showerror("Error", "Pilih gambar terlebih dahulu.")
        return

    message = decode_message(image_path)
    if message:
        message_text.delete("1.0", tk.END)
        message_text.insert(tk.END, message)

# GUI Setup
root = tk.Tk()
root.title("Steganography App")

input_image_path = tk.StringVar()
output_image_path = tk.StringVar()

# Input Image Selection
input_label = tk.Label(root, text="Pilih Gambar Input:")
input_label.grid(row=0, column=0, padx=10, pady=5)

input_entry = tk.Entry(root, textvariable=input_image_path, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)

input_button = tk.Button(root, text="Pilih", command=open_image)
input_button.grid(row=0, column=2, padx=10, pady=5)

# Output Image Selection
output_label = tk.Label(root, text="Pilih Gambar Output:")
output_label.grid(row=1, column=0, padx=10, pady=5)

output_entry = tk.Entry(root, textvariable=output_image_path, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

output_button = tk.Button(root, text="Simpan", command=save_image)
output_button.grid(row=1, column=2, padx=10, pady=5)

# Message Input/Output
message_label = tk.Label(root, text="Pesan:")
message_label.grid(row=2, column=0, padx=10, pady=5, sticky="n")

message_text = tk.Text(root, height=10, width=50)
message_text.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

# Encode and Decode Buttons
encode_button = tk.Button(root, text="Sisipkan Pesan", command=encode)
encode_button.grid(row=3, column=0, padx=10, pady=10)

decode_button = tk.Button(root, text="Ambil Pesan", command=decode)
decode_button.grid(row=3, column=1, padx=10, pady=10)

# Run Application
root.mainloop()
