import tkinter as tk
import re

class Task1GUI:
    def __init__(self, root):
        root.title("Task 1: Basic Sentence Segmentation")
        root.geometry("500x300")

        self.input_text = tk.Text(root, height=8)
        self.input_text.pack(pady=10)

        tk.Button(root, text="Segment Sentences", command=self.segment_sentences).pack(pady=10)
        
        self.output_text = tk.Text(root, height=8, state="disabled")
        self.output_text.pack(pady=10)

    def segment_sentences(self):
        text = self.input_text.get("1.0", tk.END).strip()
        sentences = re.split(r'(?<=[.!?]) +', text)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        for sentence in sentences:
            self.output_text.insert(tk.END, f"{sentence}\n")
        self.output_text.config(state="disabled")
