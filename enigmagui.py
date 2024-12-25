import tkinter as tk
from tkinter import messagebox

# Simplified Enigma Cipher Implementation
class EnigmaMachine:
    def __init__(self):
        # Rotors and reflector (simplified)
        self.rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self.reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0

    def rotate(self):
        self.position1 = (self.position1 + 1) % 26
        if self.position1 == 0:
            self.position2 = (self.position2 + 1) % 26
            if self.position2 == 0:
                self.position3 = (self.position3 + 1) % 26

    def encrypt_character(self, char):
        if char not in self.alphabet:
            return char

        # Rotate rotors
        self.rotate()

        # Pass through rotors
        index = self.alphabet.index(char)
        index = (index + self.position1) % 26
        char = self.rotor1[index]
        index = (self.alphabet.index(char) + self.position2) % 26
        char = self.rotor2[index]
        index = (self.alphabet.index(char) + self.position3) % 26
        char = self.rotor3[index]

        # Reflector
        index = self.alphabet.index(char)
        char = self.reflector[index]

        # Pass back through rotors (in reverse)
        index = self.rotor3.index(char)
        char = self.alphabet[(index - self.position3) % 26]
        index = self.rotor2.index(char)
        char = self.alphabet[(index - self.position2) % 26]
        index = self.rotor1.index(char)
        char = self.alphabet[(index - self.position1) % 26]

        return char

    def encrypt_message(self, message):
        return ''.join(self.encrypt_character(char) for char in message.upper())

# GUI Implementation
def encrypt_message():
    message = input_text.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Masukan teks untuk dienkripsi.")
        return

    enigma = EnigmaMachine()
    encrypted_message = enigma.encrypt_message(message)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_message)

# Create the main window
root = tk.Tk()
root.title("Enigma Cipher")

# Create labels and text areas
input_label = tk.Label(root, text="Masukan Teks:")
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=10, pady=5)

output_label = tk.Label(root, text="Hasil Enkripsi:")
output_label.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=1, column=1, padx=10, pady=5)

# Create encrypt button
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_message)
encrypt_button.grid(row=2, column=1, pady=10)

# Run the application
root.mainloop()
