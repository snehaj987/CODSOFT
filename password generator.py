import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" The Password Generator")

        self.create_widgets()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 6:
                messagebox.showerror("Error", "Password length should be at least 6 characters.")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                include_digits = self.include_digits_var.get()
                include_punctuation = self.include_punctuation_var.get()
                user_name = self.name_entry.get()

                if include_digits:
                    characters += string.digits
                if include_punctuation:
                    characters += string.punctuation

                password = self.generate_password_with_name(user_name, length, characters)
                self.add_password_entry(user_name, password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

    def generate_password_with_name(self, user_name, length, characters):
        random_chars = random.choices(characters, k=length - len(user_name))
        password = user_name + ''.join(random_chars)
        return password

    def add_password_entry(self, user_name, password):
        entry = f"Username: {user_name} | Password: {password}"
        self.password_listbox.insert(tk.END, entry)

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Enter Your Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.length_label = tk.Label(self.root, text="Enter Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        self.include_digits_var = tk.BooleanVar()
        self.include_digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits_var)
        self.include_digits_check.pack()

        self.include_punctuation_var = tk.BooleanVar()
        self.include_punctuation_check = tk.Checkbutton(self.root, text="Include Punctuation", variable=self.include_punctuation_var)
        self.include_punctuation_check.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_listbox = tk.Listbox(self.root, width=50, height=15)
        self.password_listbox.pack()

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
