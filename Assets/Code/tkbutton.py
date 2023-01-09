import tkinter as tk
import tkinter.messagebox as messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a button and set its text to "Hello"
        helloButton = tk.Button(self, text="Hello", command=self.sayHello)
        helloButton.pack()

        # Set the window properties
        self.title("Hello Button")
        self.geometry("300x200")
        self.mainloop()

    def sayHello(self):
        # Display a message box with the "Hello" message
        messagebox.showinfo("Hello", "Hello World!")

if __name__ == "__main__":
    window = MainWindow()
