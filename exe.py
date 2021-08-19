from tkinter import *
from tkinter import filedialog, ttk
from mainProgram import *

class Exe:
    def start(self):
        self.root = Tk()

        self.root.title("Launcher")
        self.root.geometry("600x155+600+200")
        self.docxLabel = Label(self.root, text="문서 위치",font=(15))
        self.docxLabel.place(x=15,y=20)
        self.saveLabel = Label(self.root, text="txt 위치",font=(15))
        self.saveLabel.place(x=15,y=60)
        self.docxEntry = Entry(self.root,width=50)
        self.docxEntry.place(x=100, y=20)
        self.saveEntry = Entry(self.root,width=50)
        self.saveEntry.place(x=100,y=60)
        self.docxButton = Button(self.root,text="문서 위치 설정",font=(15),width=12,command=self.add_docxPath)
        self.docxButton.place(x=460,y=15)
        self.saveButton = Button(self.root,text="txt 위치 설정",font=(15),width=12,command=self.add_savePath)
        self.saveButton.place(x=460,y=55)

        self.convertButton = Button(self.root, text="결과물 출력", font=(15),width=12,height=2,command=self.startProgram)
        self.convertButton.place(x=460,y=95)

        self.p_bar = DoubleVar()
        self.progressbar = ttk.Progressbar(self.root, maximum=39, length=430, variable=self.p_bar)
        self.progressbar.place(x=15,y=110)
        self.root.mainloop()

    def startProgram(self):
        if self.docxEntry.get() == "" or self.saveEntry.get() == "":
            print('경로 입력이 잘못 되었습니다.')
        else:
            main(self.docxEntry.get()+'/',self.saveEntry.get()+'/',exe)

    def add_docxPath(self):
        path = filedialog.askdirectory()
        if path is None:
            return
        self.docxEntry.delete(0,END)
        self.docxEntry.insert(0,path)
    
    def add_savePath(self):
        path = filedialog.askdirectory()
        if path is None:
            return
        self.saveEntry.delete(0,END)
        self.saveEntry.insert(0,path)

if __name__ == "__main__":
    exe = Exe()
    exe.start()