import tkinter as tk
import client 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = "Connect server"
        # self.hi_there["command"] = self.say_hi()
        self.languages = tk.Listbox(self)
        self.languages.insert(1, self.hi_there)
        self.languages.insert(2)
        self.languages.insert(3)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def query_database(self, query):
        client.send_data(query)

    def connect_server(self):
        client.conect_server(client.HOST, client.PORT)
        pass

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("700x400")
root.title("Client end")
app = Application(master=root)
app.mainloop()