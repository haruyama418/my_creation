import tkinter as tk

class Application(tk.Frame):
 def __init__(self,master):
    super().__init__(master)
    self.pack()

    #master.geometry("300x300")
    master.title("文字数カウント")
    self.input()


 def input(self):
    def getTextInput():
        result = self.textExample.get(1.0, tk.END + "-1c")
        print(len(result))

        self.word.forget()
        self.word = tk.Label(self.fr1, text="文字数は"+str(len(result))+"文字です。", bg='gray15',fg="snow3",font=("Arial", 25, "bold") )
        self.word.pack()
    self.fr1 = tk.Frame(self, bg="gray15", width=500, height=350, )
    self.fr1.propagate(False) # フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)
    self.fr1.pack()
    self.textExample=tk.Text(self.fr1, height=20,)
    self.textExample.pack()
    btnRead = tk.Button(self.fr1, height=1, width=10, text="Read",
    command=getTextInput)
    btnRead.pack()
    self.word = tk.Label(self.fr1, text="ここに文字数が表示されます。", bg='gray15',fg="snow3",font=("Arial", 25, "bold"))
    self.word.pack()

def main():
 win = tk.Tk()
 app = Application(master=win)
 app.mainloop()


if __name__ == "__main__":
 main()
