import tkinter as tk
import client 
import scholars

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

#       Connects to server
        self.connect_server

        self.scholars = []

        # Perform first select query
        self.query_database("SELECT * FROM HallOfFame")

        # Receive the data
        self.get_scholars()


    def create_widgets(self):
        self.widgets = []
        for i, scholar in enumerate(self.scholars):
            self.widgets.append(tk.Label(self))
            self.widgets[i]['text'] = scholar

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def query_database(self, query):
        client.send_data(query)

    def connect_server(self):
        client.conect_server(client.HOST, client.PORT)
        pass

    def get_scholars(self):
        self.scholars = client.receive_data()



root = tk.Tk()
root.geometry("700x400")
root.title("Client end")
app = Application(master=root)
app.mainloop()