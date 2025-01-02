import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        count = int(count_entry.get())
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        words = words_entry.get().split(',') if words_entry.get().strip() else []

        passwords_box.delete("1.0", tk.END)

        for _ in range(count):
            all_chars = string.ascii_letters + string.digits + string.punctuation

            # Generate random part of the password
            random_part = ''.join(random.choices(all_chars, k=length))

            # Process words to include parts of them
            word_parts = []
            for word in words:
                if len(word) > 0:
                    part_lengths = random.choices(range(1, len(word) + 1), k=random.randint(1, len(word)))
                    word_parts.extend(word[:l] for l in part_lengths)

            # Combine random part and word parts
            password_list = list(random_part) + word_parts
            random.shuffle(password_list)
            password = ''.join(password_list)[:length]

            passwords_box.insert(tk.END, password + '\n')

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_passwords():
    passwords = passwords_box.get("1.0", tk.END).strip()
    if not passwords:
        messagebox.showwarning("Warning", "No passwords to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(passwords)
        messagebox.showinfo("Success", f"Passwords saved to {file_path}")

# Create the GUI window
root = tk.Tk()
root.title("Password Generator")

# GUI Layout
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Password Length
length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="e")

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1)

# Number of Passwords
count_label = tk.Label(frame, text="Number of Passwords:")
count_label.grid(row=1, column=0, sticky="e")

count_entry = tk.Entry(frame)
count_entry.grid(row=1, column=1)

# Words
words_label = tk.Label(frame, text="Words (comma-separated):")
words_label.grid(row=2, column=0, sticky="e")

words_entry = tk.Entry(frame)
words_entry.grid(row=2, column=1)

# Generate Button
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=5)

# Passwords Output
passwords_box = tk.Text(root, width=50, height=10)
passwords_box.pack(padx=10, pady=10)

# Save Button
save_button = tk.Button(root, text="Save Passwords", command=save_passwords)
save_button.pack(pady=5)

# Start the application
root.mainloop()
