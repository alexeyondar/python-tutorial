import tkinter as tk

root = tk.Tk()
root.title("Mi primer Frame")

# El frame permite incluir otros componentes en su interior
frame = tk.Frame(root)
frame.configure(bg="blue", width=400, height=300)
frame.pack() # Apilo el frame en el master o raiz

root.mainloop()