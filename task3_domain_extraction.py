import tkinter as tk
import re

class Task3GUI:
    def __init__(self, root):
        root.title("Task 3: Domain-Specific Extraction")
        root.geometry("500x300")

        self.input_text = tk.Text(root, height=8)
        self.input_text.pack(pady=10)

        tk.Button(root, text="Extract Information", command=self.extract_info).pack(pady=10)
        
        self.output_text = tk.Text(root, height=8, state="disabled")
        self.output_text.pack(pady=10)

    def extract_info(self):
        text = self.input_text.get("1.0", tk.END).strip()
        names = re.findall(r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b', text)
        phone_numbers = re.findall(r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', text)
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Names:\n" + ", ".join(names) + "\n\n")
        self.output_text.insert(tk.END, "Phone Numbers:\n" + ", ".join(phone_numbers))
        self.output_text.config(state="disabled")
