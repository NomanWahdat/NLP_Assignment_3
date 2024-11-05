import tkinter as tk
from task1_basic_segmentation import Task1GUI
from task2_model_segmentation import Task2GUI
from task3_domain_extraction import Task3GUI

class MainApp:
    def __init__(self, root):
        root.title("Assignment 3: Sentence Segmentation")
        root.geometry("500x400")
        
        tk.Label(root, text="Choose a Task", font=("Arial", 16)).pack(pady=20)
        
        # Task Buttons
        tk.Button(root, text="Task 1: Basic Segmentation", command=self.open_task1, width=30).pack(pady=10)
        tk.Button(root, text="Task 2: Model-Based Segmentation", command=self.open_task2, width=30).pack(pady=10)
        tk.Button(root, text="Task 3: Domain Extraction", command=self.open_task3, width=30).pack(pady=10)

    def open_task1(self):
        Task1GUI(tk.Toplevel())

    def open_task2(self):
        Task2GUI(tk.Toplevel())

    def open_task3(self):
        Task3GUI(tk.Toplevel())

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
