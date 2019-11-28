import tkinter as tk

class UsersRepo:
    @staticmethod
    def Autenticate(self, user:str, password:str):
        print(user)
        print(password)

root = tk.Tk()
root.title("Entrada por teclado")

lblUser = tk.Label(root, text="Ingrese su usuario")
lblUser.configure(fg="green", bg="lightgrey", font=("Cortana",11))
lblUser.pack()

inputUser = tk.Entry(root)
inputUser.config(justify="center")
inputUser.pack()

lblPass = tk.Label(root, text="Ingrese su clave")
lblPass.configure(fg="green", bg="lightgrey", font=("Cortana",11))
lblPass.pack()

inputPass = tk.Entry(root)
inputPass.config(justify="center", show="*")
inputPass.pack()

btnSend = tk.Button(root)
btnSend["text"] = "Entrar"
btnSend["command"] = UsersRepo.Autenticate("str", "str")

root.mainloop()