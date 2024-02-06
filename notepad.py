import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand="yes", fill="both")

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Simple Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.root.title(f"Simple Notepad - {file_path}")

    def save_file(self):
        if hasattr(self, 'file_path'):
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
                self.file_path = file_path
                self.root.title(f"Simple Notepad - {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.geometry("600x400")
    root.mainloop()
