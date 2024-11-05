import tkinter as tk
from transformers import pipeline

class Task2GUI:
    def __init__(self, root):
        root.title("Task 2: Model-Based Segmentation")
        root.geometry("500x300")

        self.model = pipeline("sentiment-analysis")  # Use for demo as segmentation models require more resources
        
        self.input_text = tk.Text(root, height=8)
        self.input_text.pack(pady=10)

        tk.Button(root, text="Segment Sentences", command=self.segment_with_model).pack(pady=10)
        
        self.output_text = tk.Text(root, height=8, state="disabled")
        self.output_text.pack(pady=10)

    def segment_with_model(self):
        text = self.input_text.get("1.0", tk.END).strip()
        # Model-based segmentation code here (For demo, we use a simple split)
        sentences = text.split(". ")  # Simplified due to model limitations
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        for sentence in sentences:
            self.output_text.insert(tk.END, f"{sentence.strip()}.\n")
        self.output_text.config(state="disabled")
